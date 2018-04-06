from django.conf.urls import url

from . import views

# be careful its a list [] not { }
# http://127.0.0.1:8000/mainstore/index/
# http://127.0.0.1:8000/mainstore/product/
# http://127.0.0.1:8000/mainstore/detail/
# Add a namespace so Django knows what directory to load
# if another app has views with the same name

app_name = 'mainstore'

urlpatterns = [


    url(r'^start/(?P<catalog_slug_s>[-\w]+)?/$', views.start_, name='start_'), #need ? -->[-\w]+)?
    url(r'^start/$', views.start_, name='start_'),
    url(r'^(?P<catalog_slug>[-\w]+)/$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<p_id>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^detail/(?P<p_id>[0-9]+)/(?P<p_slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^search/(?P<catalog_slug>[-\w]+)?/$', views.search, name='search'),
    url(r'^search/$', views.search, name='search'),


]

