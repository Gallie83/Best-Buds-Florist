from django.shortcuts import render


def handle_not_found(request, exception):
    """ Handles unrecognised URLS """

    return render(request, 'home/not-found.html')


def handle_server_error(request):
    """ Handles error pages """

    return render(request, 'home/server-error.html')
