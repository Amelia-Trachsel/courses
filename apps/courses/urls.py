from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add_course),
    url(r'^delete/(?P<number>\d+)$', views.delete),
    url(r'^courses/destroy/(?P<number>\d+)$', views.destroy)
]