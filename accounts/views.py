from django.shortcuts import render


def account(request):
    """ Displays users account """
    context = {}

    return render(request, 'accounts/account.html', context)
