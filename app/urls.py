from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.room_list, name='room_list'),
    url(r'^room/(?P<pk>\d+)/$', views.room_detail, name='room_detail'),
    url(r'^room/new/$', views.room_new, name='room_new'),
    url(r'^room/(?P<pk>\d+)/edit/$', views.room_edit, name='room_edit'),
]
