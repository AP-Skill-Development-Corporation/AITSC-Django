from django.shortcuts import render,redirect
from .forms import Usreg
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def register(request):
	if request.method == "POST":
		f = Usreg(request.POST)
		if f.is_valid():
			f.save()
			return redirect('/log')
	f = Usreg()
	return render(request,'html/regis.html',{'y':f})

@login_required
def dashboard(request):
	return render(request,'html/dashboard.html')
	