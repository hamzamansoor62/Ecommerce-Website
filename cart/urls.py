from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cart'

urlpatterns = [
    path('cart',views.finalcart,name='finalcart'),
    path('invoice',views.invoice,name='invoice'),
    path('cart/dele/<int:id>',views.dele,name='dele'),
    path('index',views.index,name='index')
]
