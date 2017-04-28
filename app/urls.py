from django.conf.urls import url

from . import views

urlpatterns = [
		url(r'^dashboard/$', views.index),
		url(r'^dashboard/cpu/$', views.indexcpu),
		url(r'^dashboard/test/$', views.indexremotetest),
		url(r'^dashboard/test/runbattery/$', views.runbattery),
		url(r'^postdata/$', views.postdata, name = 'postdata'),
]