from django.shortcuts import render, redirect

from cart.cart import Cart
from order.forms import OrderCreateForm
from order.models import OrderItem
from order.task import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            order_created(order.id)
            # print("-------------order id is {}---------------:".format(order.id))

            request.session['order_id'] = order.id

            return redirect('payment:process')
    else:
        form = OrderCreateForm()
    context = {
        'cart': cart,
        'form': form
    }
    return render(request, 'order/create.html', context)
