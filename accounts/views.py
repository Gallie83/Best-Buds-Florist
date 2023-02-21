from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def account(request):
    """ Displays users account """

    account = get_object_or_404(UserProfile, user=request.user)

    context = {'account': account, }

    return render(request, 'accounts/account.html', context)
