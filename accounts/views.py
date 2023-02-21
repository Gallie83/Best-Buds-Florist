from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


def account(request):
    """ Displays users account """

    account = get_object_or_404(UserProfile, user=request.user)
    orders = account.orders.all()

    form = UserProfileForm(instance=account)

    context = {
        'orders': orders,
        'form': form,
    }

    return render(request, 'accounts/account.html', context)
