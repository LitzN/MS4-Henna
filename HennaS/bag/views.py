from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ View to return shopping bag """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    colour = None
    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']

    bag = request.session.get('bag', {})

    if colour:
        if item_id in list(bag.keys()):
            if colour in bag[item_id]['items_by_colour'].keys():
                bag[item_id]['items_by_colour'][colour] += quantity
            else:
                bag[item_id]['items_by_colour'][colour] = quantity
        else:
            bag[item_id] = {'items_by_colour': {colour: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ """
    quantity = int(request.POST.get('quantity'))
    colour = None
    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']

    bag = request.session.get('bag', {})

    if colour:
        if quantity > 0:
            bag[item_id]['items_by_colour'][colour] = quantity
        else:
            del bag[item_id]['items_by_colour'][colour]
            if not bag[item_id]['items_by_colour']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ """
    try:
        colour = None
        if 'product_colour' in request.POST:
            colour = request.POST['product_colour']

        bag = request.session.get('bag', {})

        if colour:
            del bag[item_id]['items_by_colour'][colour]
            if not bag[item_id]['items_by_colour']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
