from django.http import HttpResponse

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product

from accounts.models import UserProfile

import json
import time
import stripe


class StripeWH_Handler:
    """ Handles Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ Sends user confirmation email """

        print("Conf")

        cust_email = order.email

        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})

        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """ Handles unknown/unexpected webhook event """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handles payment_intent.succeeded webhook """

        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details  # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)  # updated

        # Cleans data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # If save-info is checked, updates the account
        account = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            account = UserProfile.objects.get(user__username=username)
            if save_info:
                account.default_phone_number = shipping_details.phone
                account.default_country = shipping_details.address.country
                account.default_postcode = shipping_details.address.postal_code
                account.default_town_or_city = shipping_details.address.city
                account.default_street_address1 = shipping_details.address.line1
                account.default_street_address2 = shipping_details.address.line2
                account.default_county = shipping_details.address.state
                account.save()
        order_exists = False
        attempt = 1
        # Checks 5 times if order exists
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                # If order is found, breaks the loop with success message
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            # Confirmation email
            self._send_confirmation_email(order)
            print("Well")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=account,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        # Sends confirmation email if webhook handler creates order
        self._send_confirmation_email(order)
        print("bottom")
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_failed(self, event):
        """ Handles payment_intent.payment_failed webhook """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
