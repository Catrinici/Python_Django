from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^$', views.index),
    url(r'^add_words$', views.add_words),
    url(r'^clear$', views.clear)

]                            

