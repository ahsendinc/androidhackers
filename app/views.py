from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect    
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import GenericData, Data, BatteryStatus, BatteryHealth, BatteryLevel, BatteryTemperature, CPUTotal, CPUUser, CPUKernel, CPULoad1, CPULoad2, CPULoad3, CPUHog1, CPUHog2, CPUHog3, CPUHog4, CPUHog5, MemInfoTotalRam, MemInfoFreeRam, MemInfoUsedRam
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

from .serializers import CPUTotalSerializer, CPUUserSerializer, CPUKernelSerializer, CPULoad1Serializer, CPULoad2Serializer,CPULoad3Serializer, CPUHog1Serializer, CPUHog2Serializer, CPUHog3Serializer, CPUHog4Serializer, CPUHog5Serializer, MemInfoTotalRamSerializer, MemInfoFreeRamSerializer, MemInfoUsedRamSerializer
from .models import TestInfo
from .serializers import TestInfoSerializer
# Create your views here.
#@ensure_csrf_cookie
def index(request):
	if (request.method == "GET"):
		#data = request.GET.get('username')
	# 	try:
		lasthealth = BatteryHealth.objects.all()[BatteryHealth.objects.count()-1].value
		laststatus = BatteryStatus.objects.all()[BatteryStatus.objects.count()-1].value
		lastlevel = BatteryLevel.objects.all()[BatteryLevel.objects.count()-1].value
		lasttemperature = BatteryTemperature.objects.all()[BatteryTemperature.objects.count()-1].value
		lastcpu = CPUTotal.objects.all()[CPUTotal.objects.count()-1].value
		lastram = MemInfoFreeRam.objects.all()[MemInfoFreeRam.objects.count()-1].value

		allbatterylevel = BatteryLevel.objects.all()

		#for battery_level in allbatterylevel:

	# #return render(request, 'index.html', data)''

	# 		return (HttpResponse("last field:" + last['field']))
	# 		#return HttpResponse(json.dumps(last))
	# 	except:
	# 		return HttpResponse("Hello! You're at the Android Diagnosis index. No data to show yet or Exception happened.")
		return render(request, 'battery.html', {'lasthealth':lasthealth, 'laststatus':laststatus, 'lastlevel':lastlevel,'lasttemperature':lasttemperature/10,'lastcpu':lastcpu, 'lastram':lastram/1000, 'allbatterylevel':allbatterylevel})
	else:	
	    return HttpResponse("Hello! You're at the Android Diagnosis index. Not allowed action.")
	   # context = {'foo': 'bar'}
	    #return render(request, 'index.html', context)


def indexcpu(request):
	if (request.method == "GET"):
		lasthealth = BatteryHealth.objects.all()[BatteryHealth.objects.count()-1].value
		laststatus = BatteryStatus.objects.all()[BatteryStatus.objects.count()-1].value
		lastlevel = BatteryLevel.objects.all()[BatteryLevel.objects.count()-1].value
		lasttemperature = BatteryTemperature.objects.all()[BatteryTemperature.objects.count()-1].value
		lastcpu = CPUTotal.objects.all()[CPUTotal.objects.count()-1].value
		
		lastcpuhog1 = CPUHog1.objects.all()[CPUHog1.objects.count()-1]
		lastcpuhog2 = CPUHog2.objects.all()[CPUHog2.objects.count()-1]
		lastcpuhog3 = CPUHog3.objects.all()[CPUHog3.objects.count()-1]
		lastcpuhog4 = CPUHog4.objects.all()[CPUHog4.objects.count()-1]
		lastcpuhog5 = CPUHog5.objects.all()[CPUHog5.objects.count()-1]

		lastramfree = MemInfoFreeRam.objects.all()[MemInfoFreeRam.objects.count()-1].value
		lastramtotal = MemInfoTotalRam.objects.all()[MemInfoTotalRam.objects.count()-1].value
		lastramused = MemInfoUsedRam.objects.all()[MemInfoUsedRam.objects.count()-1].value

		ramfree_percent = (lastramfree/lastramtotal)*100
		ramused_percent = (lastramused/lastramtotal)*100

		return render(request, 'cpu.html',{'lasthealth':lasthealth, 'laststatus':laststatus, 'lastlevel':lastlevel,'lasttemperature':lasttemperature/10,'lastcpu':lastcpu, 'lastram':lastramfree/1000, 'cpuhog1':lastcpuhog1, 'cpuhog2':lastcpuhog2, 'cpuhog3':lastcpuhog3, 'cpuhog4':lastcpuhog4, 'cpuhog5':lastcpuhog5, 'lastramfree':lastramfree, 'lastramused':lastramused, 'lastramtotal':lastramtotal, 'ramfree_percent':ramfree_percent, 'ramused_percent':ramused_percent})
	else:	
	    return HttpResponse("Hello! You're at the Android Diagnosis index. Not allowed action.")

def indexremotetest(request):
	if (request.method == "GET"):
		query = TestInfo.objects.all().order_by('-id')
		return render(request, 'remote_testing.html',{"query":query})
	else:	
	    return HttpResponse("Hello! You're at the Android Diagnosis index. Not allowed action.")

def indexproject(request):
	if (request.method == "GET"):
		return render(request, 'project_details.html')
	else:	
	    return HttpResponse("Hello! You're at the Android Diagnosis index. Not allowed action.")

def indexreport(request):
	if (request.method == "GET"):
		return render(request, 'report.html')
	else:	
	    return HttpResponse("Hello! You're at the Android Diagnosis index. Not allowed action.")

def indexcontacts(request):
	if (request.method == "GET"):
		return render(request, 'contacts.html')
	else:	
	    return HttpResponse("Hello! You're at the Android Diagnosis index. Not allowed action.")

def gettestinfo(request):
	if request.method == "GET":
		test = TestInfo.objects.filter(status="Pending").first()
		try:
			myresponse = {"id": test.idnum , "name" : test.name }
			return HttpResponse(json.dumps(myresponse))
		
		except Exception:
			myresponse = {"id": -1, "name": "not pending"}
			return HttpResponse(json.dumps(myresponse))

	else:
		return HttpResponse("action not allowed.")
@csrf_exempt
@api_view(['POST'])
def posttestinfo(request):
	if request.method == "POST":
		data = request.data
		test = TestInfo.objects.filter(idnum=data["id"]).first()
		test.status = data["status"]
		test.message = data["message"]
		test.save(update_fields=["status","message"])
		return HttpResponse(test.message)
	else:
		return HttpResponse("not allowed action")

def runbattery(request):
	if request.method == "GET":
		test = TestInfo.objects.create(idnum=TestInfo.objects.count()+1, name = "Low Battery", status = "Pending", message="...")
		test.save()
		return HttpResponseRedirect("..")

def runbatterystatus(request):
	if request.method == "GET":
		test = TestInfo.objects.create(idnum=TestInfo.objects.count()+1, name = "Battery Status", status = "Pending", message="...")
		test.save()
		return HttpResponseRedirect("..")

def runbluetooth(request):
	if request.method == "GET":
		test = TestInfo.objects.create(idnum=TestInfo.objects.count()+1, name = "Bluetooth", status = "Pending", message="...")
		test.save()
		return HttpResponseRedirect("..")

def runspeed(request):
	if request.method == "GET":
		test = TestInfo.objects.create(idnum=TestInfo.objects.count()+1, name = "Speed", status = "Pending", message="...")
		test.save()
		return HttpResponseRedirect("..")

#@ensure_csrf_cookie
@csrf_exempt
@api_view(['POST'])
def postdata(request):
	if (request.method == "POST"):
		
		#return HttpResponse(request.POST.getlist('battery_status')[0])
		try:
			listOfThings = request.data['battery_status']
			mylist = json.loads(listOfThings)
			serialized = BatteryStatusSerializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()

			listOfThings = request.data['battery_level']
			mylist = json.loads(listOfThings)
			serialized = BatteryLevelSerializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()

			listOfThings = request.data['battery_temperature']
			mylist = json.loads(listOfThings)
			serialized = BatteryTemperatureSerializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()

			listOfThings = request.data['battery_health']
			mylist = json.loads(listOfThings)
			serialized = BatteryHealthSerializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()
				#jsondata = JSONRenderer().render(serialized.data)

			listOfThings = request.data['cpu_total']
			mylist = json.loads(listOfThings)
			serialized = CPUTotalSerializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()
#deletedcpukernel
			# listOfThings = request.data['cpu_kernel']
			# mylist = json.loads(listOfThings)
			# serialized = CPUKernelSerializer(data=mylist, many=True)
			# if serialized.is_valid():
			# 	serialized.save()
#deletecpuuser
			# listOfThings = request.data['cpu_user']
			# mylist = json.loads(listOfThings)
			# serialized = CPUUserSerializer(data=mylist, many=True)
			# if serialized.is_valid():
			# 	serialized.save()

			listOfThings = request.data['cpu_load1']
			mylist = json.loads(listOfThings)
			serialized = CPULoad1Serializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()	

			listOfThings = request.data['cpu_load2']
			mylist = json.loads(listOfThings)
			serialized = CPULoad2Serializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()

			listOfThings = request.data['cpu_load3']
			mylist = json.loads(listOfThings)
			serialized = CPULoad3Serializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()

			listOfThings = request.data['cpu_hog1']
			mylist = json.loads(listOfThings)
			serialized = CPUHog1Serializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()

			listOfThings = request.data['cpu_hog2']
			mylist = json.loads(listOfThings)
			serialized = CPUHog2Serializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()

			listOfThings = request.data['cpu_hog3']
			mylist = json.loads(listOfThings)
			serialized = CPUHog3Serializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()

			listOfThings = request.data['cpu_hog4']
			mylist = json.loads(listOfThings)
			serialized = CPUHog4Serializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()

			listOfThings = request.data['cpu_hog5']
			mylist = json.loads(listOfThings)
			serialized = CPUHog5Serializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()

			listOfThings = request.data['ram_total']
			mylist = json.loads(listOfThings)
			serialized = MemInfoTotalRamSerializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()

			listOfThings = request.data['ram_free']
			mylist = json.loads(listOfThings)
			serialized = MemInfoFreeRamSerializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()

			listOfThings = request.data['ram_used']
			mylist = json.loads(listOfThings)
			serialized = MemInfoUsedRamSerializer(data=mylist, many=True)
			if serialized.is_valid():
				serialized.save()

				return HttpResponse(('created'), status=201)

		except:
				return HttpResponse('notcreated', status=500)
		#jsond = json.dumps(request.POST.getlist('tracks'))
		return HttpResponse('notcreated', status=400)

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
		return HttpResponse("This api is only for POST", status=400)


# class CreateListModelMixin(object):
    
# 	def get_serializer(self, *args, **kwargs):
# 		if isinstance(kwargs.get('data',{}),list):
# 			kwargs['many'] = True
# 		return super(self).get_serializer(*args,**kwargs)



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

class TestInfoViewSet(viewsets.ModelViewSet):
	queryset = TestInfo.objects.all()
	serializer_class = TestInfoSerializer

class BatteryHealthViewSet(viewsets.ModelViewSet):

	queryset = BatteryHealth.objects.all()
	serializer_class= BatteryHealthSerializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['battery_health']
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

class BatteryLevelViewSet(viewsets.ModelViewSet):

	queryset = BatteryLevel.objects.all()
	serializer_class= BatteryLevelSerializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['battery_level']
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

class BatteryTemperatureViewSet(viewsets.ModelViewSet):

	queryset = BatteryTemperature.objects.all()
	serializer_class= BatteryTemperatureSerializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['battery_temperature']
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

class CPUTotalViewSet(viewsets.ModelViewSet):

	queryset = CPUTotal.objects.all()
	serializer_class= CPUTotalSerializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['cpu_total']
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

class CPUUserViewSet(viewsets.ModelViewSet):

	queryset = CPUUser.objects.all()
	serializer_class= CPUUserSerializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['cpu_user']
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

class CPUKernelViewSet(viewsets.ModelViewSet):

	queryset = CPUKernel.objects.all()
	serializer_class= CPUKernelSerializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['cpu_kernel']
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

class CPULoad1ViewSet(viewsets.ModelViewSet):

	queryset = CPULoad1.objects.all()
	serializer_class= CPULoad1Serializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['cpu_load1']
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

class CPULoad2ViewSet(viewsets.ModelViewSet):

	queryset = CPULoad2.objects.all()
	serializer_class= CPULoad2Serializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['cpu_load2']
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

class CPULoad3ViewSet(viewsets.ModelViewSet):

	queryset = CPULoad3.objects.all()
	serializer_class= CPULoad3Serializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['cpu_load3']
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

class CPUHog1ViewSet(viewsets.ModelViewSet):

	queryset = CPUHog1.objects.all()
	serializer_class= CPUHog1Serializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['cpu_hog1']
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

class CPUHog2ViewSet(viewsets.ModelViewSet):

	queryset = CPUHog2.objects.all()
	serializer_class= CPUHog2Serializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['cpu_hog2']
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

class CPUHog3ViewSet(viewsets.ModelViewSet):

	queryset = CPUHog3.objects.all()
	serializer_class= CPUHog3Serializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['cpu_hog3']
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

class CPUHog4ViewSet(viewsets.ModelViewSet):

	queryset = CPUHog4.objects.all()
	serializer_class= CPUHog4Serializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['cpu_hog4']
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

class CPUHog5ViewSet(viewsets.ModelViewSet):

	queryset = CPUHog5.objects.all()
	serializer_class= CPUHog5Serializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['cpu_hog5']
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


class MemInfoTotalRamViewSet(viewsets.ModelViewSet):

	queryset = MemInfoTotalRam.objects.all()
	serializer_class= MemInfoTotalRamSerializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['meminfo_totalram']
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

class MemInfoFreeRamViewSet(viewsets.ModelViewSet):

	queryset = MemInfoFreeRam.objects.all()
	serializer_class= MemInfoFreeRamSerializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['meminfo_freeram']
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

class MemInfoUsedRamViewSet(viewsets.ModelViewSet):

	queryset = MemInfoUsedRam.objects.all()
	serializer_class= MemInfoUsedRamSerializer

	def create(self, request, *args, **kwargs):
		try:
			listOfThings = request.data['meminfo_usedram']
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