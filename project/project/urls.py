"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import index
from app import views as v1
from app1 import views as v2
from app2 import views as v3

urlpatterns = [
    path('admin/', admin.site.urls),
   # path("",index,name="views")
    path("home/",index,name="index"),
    path("home/",v1.index,name="index1"),
    path("home/",v2.index,name="index2"),
    path("home/",v3.index,name="index3")
]
