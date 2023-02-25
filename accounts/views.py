from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile, ProfilePicture
from .forms import UserProfileForm, ImageForm

from django.contrib.auth.decorators import login_required

from checkout.models import Order


@login_required
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
        form = UserProfileForm(instance=account)

    orders = account.orders.all()

    form = UserProfileForm(instance=account)

    context = {
        'orders': orders,
        'form': form,
        'on_account_page': True,
    }

    return render(request, 'accounts/account.html', context)


def profile_picture(request):
    account = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get("picture")
            obj = ProfilePicture.objects.create(
                user=account,
                picture=picture
            )
            obj.save()
            messages.success(request, 'Photo updated!')
        else:
            print(form.errors)
            messages.error(
                request, 'Failed to update photo! Ensure the form is valid')
    else:
        form = ImageForm()

    form = ImageForm()

    context = {
        'form': form,
        'on_account_page': True,
    }

    return render(request, 'accounts/profile_picture.html', context)


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
