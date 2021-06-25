from django.urls import path
from . import views

app_name = 'cart' #urls will begin with cart/
urlpatterns = [
    
    #Render Views
    path('', views.CartView.as_view(), name='summary'),
    path('shop', views.ProductListView.as_view(), name='product-list'),
    path('shop/<slug>/', views.ProductDetailView.as_view(), name='product-detail'),
    
    #Cart-Specific Views
    path('increase-quantity/<pk>/', views.IncreaseQuantityView.as_view(), name='increase-quantity'),
    path('decrease-quantity/<pk>/', views.DecreaseQuantityView.as_view(), name='decrease-quantity'),
]