from django.conf.urls import url

from . import views

app_name='order'

urlpatterns = [
    url(r'^create_order/$', views.order_create,name='order_create'),
]