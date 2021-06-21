from django.views import generic
from .models import Product
from .forms import AddToCartForm
from .utils import get_or_set_order_session
from django.shortcuts import get_object_or_404, reverse

class ProductListView(generic.ListView):
    template_name = 'cart/product_list.html'
    queryset = Product.objects.all()

class ProductDetailView(generic.FormView):
    template_name = 'cart/product_detail.html'
    form_class = AddToCartForm
    
    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs["slug"]) #kwargs = keyword arguments
    
    def get_success_url(self):
        return reverse("home") #TODO eventually redirect to the cart.
    
    def form_valid(self, form):
        order = get_or_set_order_session(self.request)
        product = self.get_object()
        
        #When adding an item (using the form), check to see if the product is already in the cart. If it is, increase the quantity. If not, add to cart.
        item_filter = order.items.filter(product=product)
        if item_filter.exists():
            item = item_filter.first()
            item.quantity = int(form.cleaned_data['quantity'])
            item.save()
        
        else:
            new_item = form.save(commit=False) #Store the data, but don't commit it yet.
            new_item.product = product
            new_item.order = order
            new_item.save()
            
        return super(ProductDetailView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        #Pass in context from the product because FormView does not automatically receive that information, such as the photo of the product.
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product'] = self.get_object()
        return context