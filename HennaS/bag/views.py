from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    """ View to return shopping bag """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ """

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

    request.session['bag'] = bag
    return redirect(redirect_url)
