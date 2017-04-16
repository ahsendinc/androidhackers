from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	if (request.method == "POST"):
		data = request.GET.get('')
		return (HttpResponse(data))
    return HttpResponse("Hello! You're at the Android Diagnosis index. No data to show yet.")