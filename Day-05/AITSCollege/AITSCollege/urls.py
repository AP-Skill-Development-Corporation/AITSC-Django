"""AITSCollege URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CSEC import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('k/',views.sample),
    path('s/<str:z>/',views.printname),
    path('d/<int:a>/<str:n>/',views.pn),
    path('w/<int:r>/',views.ht),
    path('z/<str:a>/',views.lin),
    path('rt/',views.htm),
    path('js/',views.alt),
    path('hm/',views.home),
    path('ab/',views.abt),
    path('rg/',views.register),
    path('',views.bthm,name="hm"),
    path('rgb/',views.btrg),
    path('abt/',views.about,name="ab"),
    path('wk/',views.mwk,name="mk"),
    path('hu/<int:k>/',views.lup,name="up"),
    path('fr/<int:w>/',views.dlt,name="d"),
]
