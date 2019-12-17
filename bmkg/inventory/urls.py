from django.conf.urls import url, include

from .views import *
from .models import *

urlpatterns = [

    #ROUTING DISPLAY 
    url(r'^$', index, name='index'),
#    url(r'^export_kelembaban$', export_kelembaban, name='export_kelembaban'),

    url(r'^kelembaban$', view_kelembaban, name='view_kelembaban'),
    url(r'^suhu$', view_suhu, name='view_suhu'),
    url(r'^tekanan$', view_tekanan, name='view_tekanan'),
    url(r'^angin$', view_angin, name='view_angin'),
    url(r'^radiasi$', view_radiasi, name='view_radiasi'),

    #ROUTING TAMBAH
    url(r'^add_kelembaban$', add_kelembaban, name='add_kelembaban'),
    url(r'^add_suhu$', add_suhu, name='add_suhu'),
    url(r'^add_tekanan$', add_tekanan, name='add_tekanan'),
    url(r'^add_angin$', add_angin, name='add_angin'),
    url(r'^add_radiasi$', add_radiasi, name='add_radiasi'),

    #ROUTING EDIT
    url(r'^kelembaban/edit_data/(?P<pk>\d+)$', edit_kelembaban, name="edit_kelembaban"),
    url(r'^suhu/edit_data/(?P<pk>\d+)$', edit_suhu, name='edit_suhu'),
    url(r'^tekanan/edit_data/(?P<pk>\d+)$', edit_tekanan, name='edit_tekanan'),
    url(r'^angin/edit_data/(?P<pk>\d+)$', edit_angin, name='edit_angin'),
    url(r'^radiasi/edit_data/(?P<pk>\d+)$', edit_radiasi, name='edit_radiasi'),

    #ROUTING DELETE
    url(r'^kelembaban/delete/(?P<pk>\d+)$', delete_kelembaban, name="delete_kelembaban"),
    url(r'^suhu/delete/(?P<pk>\d+)$', delete_suhu, name='delete_suhu'),
    url(r'^tekanan/delete/(?P<pk>\d+)$', delete_tekanan, name='delete_tekanan'),
    url(r'^angin/delete/(?P<pk>\d+)$', delete_angin, name='delete_angin'),
    url(r'^radiasi/delete/(?P<pk>\d+)$', delete_radiasi, name='delete_radiasi'),

]
