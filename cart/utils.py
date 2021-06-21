from .models import Order

#Code for utilizing session with our order
def get_or_set_order_session(request):
    order_id = request.session.get('order_id', None)
    
    #If there is no order_id stored in session, set it to refer to the current order.
    if order_id is None:
        order = Order()
        order.save()
        request.session['order_id'] = order.id

    #Also make sure that if there IS an order, it has not already been paid for. If not, set the current order to session.
    else: 
        try:  
            order = Order.objects.get(id=order_id, ordered=False)
        except Order.DoesNotExist:
            order = Order()
            order.save()
            request.session['order_id'] = order.id
    
    #if the current user has no order associated with him/her, associate the user with the current order. 
    #This lets the user interact with the website and add items to the cart without being logged in.
    if request.user.is_authenticated and order.user is None:
        order.user = request.user
        order.save()
    return order
