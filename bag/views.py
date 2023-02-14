from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    """ Returns shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Adds item to users bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Added another {product.name} to cart!')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to cart!')

    request.session['bag'] = bag

    return redirect(redirect_url)


def update_bag(request, item_id):
    """Updates items in users bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} in cart!')
    else:
        bag.pop[item_id]
        messages.error(request, f'Added {product.name} to cart!')

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))
