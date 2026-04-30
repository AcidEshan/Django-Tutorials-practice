"""
URL configuration for practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from Machine_learning import views as ml
from Blogs import views as b
from Deep_learning import views as dlp
from Data_Analysis.views import data_analysis
from Data_Analysis.views import ai_engineering  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ml.machine_learning),
    path('dl/', ml.deep_learning),
    path('about/', ml.about_us),
    path('blogs/', b.blog_list),
    path('deep/', dlp.deep_learning),
    path('data/', data_analysis),
    path('ai/', ai_engineering), 
]

