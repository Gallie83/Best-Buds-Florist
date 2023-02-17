from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag right now!")
        return redirect(reverse('products'))

    # Returns current bags grand total
    current_bag = bag_contents(request)
    total = current_bag['grand_total']

    # Converts to Integer for Stripe
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Mc8VxBKNsKphDUQ5hCvCC4nWcODe66BYUit8e4KcCEKEnVFN4BGRFxK4inBNfY15RSz5ZBgXZutnxWSNCktnok2006ICJp4n5',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
