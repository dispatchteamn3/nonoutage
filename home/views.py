from django.shortcuts import render
from django.http import HttpResponse

def Breaker(request):
	return render(request,'home/Breaker.html')

def Home(request):
	return render(request,'home/Home.html')