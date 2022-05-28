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

def lin(req,a):
	return HttpResponse('<h1>Hi welcome <span style=color:red>{}</span></h1>'.format(a))

def htm(request):
	return HttpResponse("<html><head><title>Welcome Page</title><style>p{color:yellow}</style></head><body><p>Hello User Welcome</p></body></html>")

def alt(request):
	return HttpResponse("<script>alert('Hi')</script><p>Hello</p>")

def home(request):
	return render(request,'home.html')

def abt(request):
	return render(request,'html/about.html')

def register(request):
	if request.method == "POST":
		a = request.POST['sn']
		b = request.POST['sa']
		c = request.POST['sb']
		return render(request,'html/display.html',{'sna':a,'sta':b,'snb':c})
	return render(request,'html/regi.html')


def bthm(request):
	return render(request,'html/bth.html')

def btrg(request):
	return render(request,'html/btreg.html')

def about(request):
	return render(request,'html/abt.html')

def mwk(request):
	return render(request,'html/worklg.html')


