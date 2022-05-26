from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample(request):
	return HttpResponse('Hello')

def printname(req,z):
	return HttpResponse("Hello Welcome {}".format(z))

def pn(t,n,a):
	return HttpResponse("Hi {} your age is: {}".format(n,a))

def ht(request,r):
	return HttpResponse("<h5>Your Age is: {}</h5>".format(r))