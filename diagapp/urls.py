"""diagapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from app import views

router = routers.DefaultRouter() 
router.register(r'genericdata',views.GenericDataViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'data',views.DataViewSet)
router.register(r'batteryhealth',views.BatteryHealthViewSet)
router.register(r'batterylevel',views.BatteryLevelViewSet)
router.register(r'batterystatus',views.BatteryStatusViewSet)
router.register(r'batterytemperature',views.BatteryTemperatureViewSet)
router.register(r'cputotal',views.CPUTotalViewSet)
router.register(r'cpuuser',views.CPUUserViewSet)
router.register(r'cpukernel',views.CPUKernelViewSet)
router.register(r'cpuload1',views.CPULoad1ViewSet)
router.register(r'cpuload2',views.CPULoad2ViewSet)
router.register(r'cpuload3',views.CPULoad3ViewSet)
router.register(r'cpuhog1',views.CPUHog1ViewSet)
router.register(r'cpuhog2',views.CPUHog2ViewSet)
router.register(r'cpuhog3',views.CPUHog3ViewSet)
router.register(r'cpuhog4',views.CPUHog4ViewSet)
router.register(r'cpuhog5',views.CPUHog5ViewSet)
# router = routers.SimpleRouter()
# router.register('texts', TextAPIView, base_name='texts')

urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^app/', include('app.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
