from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^course$',views.addCourse),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name = "destroy"),
    url(r'^confirmDestroy/(?P<id>\d+)$', views.confirmDestroy, name = 'confirm')
]
