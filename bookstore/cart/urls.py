from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.cart_detail, name='cart_detail'),
    re_path(r'^add/(?P<book_id>\d+)/$', views.cart_add, name='cart_add'),
    re_path(r'^remove/(?P<book_id>\d+)/$', views.cart_remove, name='cart_remove'),
]