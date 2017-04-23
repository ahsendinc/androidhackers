from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect    
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import GenericData, Data
from rest_framework import viewsets
from .serializers import GenericDataSerializer, UserSerializer, GroupSerializer, DataSerializer
from django.contrib.auth.models import User, Group
import requests
from django.contrib.auth.decorators import login_required
from .forms import GenericDataForm
from django.utils import timezone
import json
# Create your views here.
#@ensure_csrf_cookie
def index(request):
	if (request.method == "GET"):
		#data = request.GET.get('username')
		try:
			last = json.loads(GenericData.objects.all()[GenericData.objects.count()-1].jsondata)
	#return render(request, 'index.html', data)''

			#return (HttpResponse("last field:" + last['field']))
			return HttpResponse(json.dumps(last))
		except:
			return HttpResponse("Hello! You're at the Android Diagnosis index. No data to show yet or Exception happened.")
	else:	
	    return HttpResponse("Hello! You're at the Android Diagnosis index. No data to show yet.")
	   # context = {'foo': 'bar'}
	    #return render(request, 'index.html', context)
def postdata(request):
	if (request.method == "POST"):
		#data = request.GET.get('username')
		form = GenericDataForm(request.POST)
	#return render(request, 'index.html', data)
		if form.is_valid:
			generic = GenericData.objects.create(jsondata =request.GET.get('jsondata'), pubdata = timezone.now())
			return HttpResponse(generic.jsondata)
		else:
			return HttpResponse('not valid form')
	else:
		form = GenericDataForm()
	return render(request, 'index.html', {'form': form})
	
class DataViewSet(viewsets.ModelViewSet):

	queryset = Data.objects.all()
	serializer_class= DataSerializer

class GenericDataViewSet(viewsets.ModelViewSet):

	queryset = GenericData.objects.all()
	serializer_class= GenericDataSerializer

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