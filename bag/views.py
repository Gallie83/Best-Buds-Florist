from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
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
        bag[item_id] = int(quantity)
        messages.success(
            request, f'Updated {product.name} quantity in cart!')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Removes items in users bag """
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.info(request, f'Removed {product.name} from your cart!')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
