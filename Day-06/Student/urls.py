from django.urls import path
from Student import views
from django.contrib.auth import views as av


urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('reg/',views.register,name="rg"),
	path('log/',av.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('lgt/',av.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
	path('ds/',views.dashboard,name="dsh"),
]