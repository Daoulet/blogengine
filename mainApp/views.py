from django.shortcuts import render

def index(request):
	return render(request, 'mainApp/index.html')

def location(request):
	return render(request, 'mainApp/location.html')

