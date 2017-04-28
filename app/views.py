from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect    
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import GenericData, Data, BatteryStatus, BatteryHealth, BatteryLevel, BatteryTemperature
from rest_framework import viewsets
from .serializers import GenericDataSerializer, UserSerializer, GroupSerializer, DataSerializer
from .serializers import BatteryStatusSerializer, BatteryHealthSerializer, BatteryLevelSerializer, BatteryTemperatureSerializer,MultBatteryStatusSerializer
from django.contrib.auth.models import User, Group
import requests
from django.contrib.auth.decorators import login_required
from .forms import GenericDataForm
from django.utils import timezone
import json

from drf_multiple_model.views import MultipleModelAPIView
from rest_framework.decorators import api_view
from rest_framework import routers

from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.mixins import CreateModelMixin
from rest_framework.renderers import JSONRenderer
# Create your views here.
#@ensure_csrf_cookie
def index(request):
	if (request.method == "GET"):
		#data = request.GET.get('username')
		try:
			last = json.loads(GenericData.objects.all()[GenericData.objects.count()-1].jsondata)
	#return render(request, 'index.html', data)''

			return (HttpResponse("last field:" + last['field']))
			#return HttpResponse(json.dumps(last))
		except:
			return HttpResponse("Hello! You're at the Android Diagnosis index. No data to show yet or Exception happened.")
	else:	
	    return HttpResponse("Hello! You're at the Android Diagnosis index. No data to show yet.")
	   # context = {'foo': 'bar'}
	    #return render(request, 'index.html', context)
#@ensure_csrf_cookie
@csrf_exempt
@api_view(['POST'])
def postdata(request):
	if (request.method == "POST"):
		
		#return HttpResponse(request.POST.getlist('battery_status')[0])
		serialized = MultBatteryStatusSerializer(data=request.data, many=True)
		if serialized.is_valid():
			serialized.save()
			jsondata = JSONRenderer().render(serialized.data)
			return HttpResponse(dict(request.data.getlist('tracks')), status=201)
		jsond = json.dumps(request.POST.getlist('tracks'))
		return HttpResponse(jsond, status=400)


		#data = request.GET.get('username')
		#return HttpResponse(request.POST.get('jsondata'))
		#generic = GenericData.objects.create(jsondata =request.POST.get('jsondata'))
		#statusdatas = json.loads(request.POST.get('batterystatus'))
		# healthdatas = request.POST['batterystatus'].getList("value")
		# for healthdata in healthdatas:
		# 	print (healthdata)

		# return HttpResponse(healthdatas)
	# 	form = GenericDataForm(request.POST)
	# #return render(request, 'index.html', data)
	# 	if form.is_valid:
	# 		generic = GenericData.objects.create(jsondata =request.POST.get('jsondata'))
	# 		return HttpResponse(generic.jsondata)
	# 	else:
	# 		return HttpResponse('not valid form')
	# else:
	# 	form = GenericDataForm()
	# return render(request, 'index.html', {'form': form})
	else:
		return HttpResponse("NOT POST")


class CreateListModelMixin(object):
    
	def get_serializer(self, *args, **kwargs):
		if isinstance(kwargs.get('data',{}),list):
			kwargs['many'] = True
		return super(self).get_serializer(*args,**kwargs)



class BatteryStatusViewSet(viewsets.ModelViewSet):

	queryset = BatteryStatus.objects.all()
	serializer_class= BatteryStatusSerializer

	# def get_serializer(self, instance=None, data=None, many=False, partial=False):
	# 	return super(BatteryStatusViewSet,self).get_serializer(instance=instance, data=data, many=True, partial=partial)

	# def get_serializer(self, *args, **kwargs):
	# 	if isinstance(kwargs.get('data',{}),list):
	# 		kwargs['many'] = True
	# 	return super(CreateListModelMixin,self).get_serializer(*args,**kwargs)


	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['battery_status']
			mylist = json.loads(listOfThings)
			print(listOfThings)
			serializer = self.get_serializer(data=mylist, many= True)
		except KeyError:
			mylist = request.data
			serializer = self.get_serializer(data=mylist)

		if serializer.is_valid():
			serializer.save()
			return HttpResponse("created",status=201)
        
		return HttpResponse(request.data,status=404)

	# def create(self, request, *args, **kwargs):
	# 	serializer = self.get_serializer(data=request.data, many=True)
	# 	serializer.is_valid(raise_exception=True)
	# 	for batterystatus_data in serializer.validated_data:
	# 	    obj = BatteryStatus.objects.create(time= batterystatus_data['time'], value = batterystatus_data['value'])
	# 	    obj.save()
	# 	    return HttpResponse("hey")

	# 	return HttpResponse(serializer)


class BatteryHealthViewSet(viewsets.ModelViewSet):

	queryset = BatteryHealth.objects.all()
	serializer_class= BatteryHealthSerializer

class BatteryLevelViewSet(viewsets.ModelViewSet):

	queryset = BatteryLevel.objects.all()
	serializer_class= BatteryLevelSerializer

class BatteryTemperatureViewSet(viewsets.ModelViewSet):

	queryset = BatteryTemperature.objects.all()
	serializer_class= BatteryTemperatureSerializer


class DataViewSet(viewsets.ModelViewSet):

	queryset = Data.objects.all()
	serializer_class= DataSerializer

class GenericDataViewSet(viewsets.ModelViewSet):

	queryset = GenericData.objects.all()
	serializer_class= GenericDataSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		#return HttpResponse(serializer.data, status=status.HTTP_201_CREATED,headers=headers)
		return HttpResponse("created")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer