from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def account(request):
    """ Displays users account """

    account = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
        else:
            messages.error(
                request, 'Failed to update profile! Ensure the form is valid')
    else:
        form = UserProfileForm(insance=account)

    orders = account.orders.all()

    form = UserProfileForm(instance=account)

    context = {
        'orders': orders,
        'form': form,
        'on_account_page': True,
    }

    return render(request, 'accounts/account.html', context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the day the order was made.'
    ))

    context = {
        'order': order,
        'from_account': True,
    }

    return render(request, 'checkout/checkout_success.html', context)
