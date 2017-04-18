from django.conf.urls import url

from . import views

urlpatterns = [
		url(r'^dashboard$', views.index),
		url(r'^postdata$', views.postdata, name = 'postdata'),
]