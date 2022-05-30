from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Work
from django.contrib import messages

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
	g = Work.objects.all()
	if request.method=="POST":
		a = request.POST['sub']
		b = request.POST['titl']
		c = request.POST['desc']
		r = Work(sb=a,title=b,des=c)
		messages.success(request,'{} added successfully'.format(a))
		r.save()
		return render(request,'html/worklg.html',{'lg':g})
	return render(request,'html/worklg.html',{'lg':g})

def lup(request,k):
	t = Work.objects.get(id=k)
	if request.method=="POST":
		a = request.POST['s']
		b = request.POST['t']
		c = request.POST['d']
		t.sb = a
		t.title = b
		t.des = c
		messages.warning(request,"{} is Updated successfully".format(t.sb))
		t.save()
		return redirect('/wk')
	return render(request,'html/wrkup.html',{'p':t})

def dlt(request,w):
	j = Work.objects.get(id=w)
	if request.method == "POST":
		messages.info(request,'{} Deleted Successfully'.format(j.sb))
		j.delete()
		return redirect('/wk')
	return render(request,'html/wrkdlt.html',{'s':j})
