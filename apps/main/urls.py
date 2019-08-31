from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^purchase-page$', views.purchase_page),
    url(r'^order$', views.order),
    url(r'^shopping-cart/(?P<order_id>\d+)', views.cart),    
    url(r'^order/edit/(?P<order_id>\d+)/$', views.edit_order),
    url(r'^order/update/(?P<order_id>\d+)/$', views.update),

]