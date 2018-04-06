from django.conf.urls import url

from . import views

# be careful its a list [] not { }
# Add a namespace so Django knows what directory to load
# if another app has views with the same name

app_name = 'myprofile'

urlpatterns = [
    # url(r'^$', views.showuser, name='showuser'),
    url(r'^login/$', views.my_login, name='my_login'),
    url(r'^logout/$', views.my_logout, name='my_logout'),
    # url(r'^mytest/$', views.mytest, name='mytest'),
    url(r'^signup/$', views.signup, name='signup'),

]
