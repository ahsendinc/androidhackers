from django.conf.urls import url

from . import views

urlpatterns = [
		url(r'^gettest/$', views.gettestinfo),
		url(r'^posttest/$', views.posttestinfo),
		url(r'^about/$', views.indexproject),
		url(r'^about/report/$', views.indexreport),
		url(r'^about/contacts/$', views.indexcontacts),
		url(r'^dashboard/$', views.index),
		url(r'^dashboard/cpu/$', views.indexcpu),
		url(r'^dashboard/test/$', views.indexremotetest),
		url(r'^dashboard/test/runbattery/$', views.runbattery),
		url(r'^dashboard/test/runbatterystatus/$', views.runbatterystatus),
		url(r'^dashboard/test/runbluetooth/$', views.runbluetooth),
		url(r'^dashboard/test/runspeed/$', views.runspeed),
		url(r'^postdata/$', views.postdata, name = 'postdata'),
]