from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag right now!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Mc8VxBKNsKphDUQ5hCvCC4nWcODe66BYUit8e4KcCEKEnVFN4BGRFxK4inBNfY15RSz5ZBgXZutnxWSNCktnok2006ICJp4n5',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
