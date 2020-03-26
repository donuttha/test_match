from django.conf.urls import url, include

from . import views

urlpatterns = [
    # url('', views.index, name='index'),
    url('get_data/', views.get_data, name='getdata'),
]