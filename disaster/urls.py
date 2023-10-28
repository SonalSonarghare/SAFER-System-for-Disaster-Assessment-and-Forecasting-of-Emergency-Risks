"""
URL configuration for disaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from disaster import views
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage),
    path('home/',views.Home),
    path('flood/',views.flood),
    path('cyclone/',views.cyclone),
    path('drought/',views.drought),
    path('FloodAssessment/',views.FloodAssessment),  
    path('map_drought/', views.map_drought, name='map_drought'),
    path('map/', views.map, name='map_view'),
    path('UP/', views.UP),
    path('Gorakhpur/',views.Gorakhpur,name='Gorakhpur'),
    path('SiddharthNagar/',views.SiddharthNagar,name='SiddharthNagar'),
    path('Kullu/',views.Kullu,name='Kullu'),
    path('Solan/',views.Solan,name='Solan'),
    path('Idukki/',views.Idukki,name='Idukki'),
    path('Palakkad/',views.Palakkad,name='Palakkad'),
    path('Darrang/',views.Darrang,name='Darrang'),
    path('Marigaon/',views.Marigaon,name='Marigaon'),
    path('EastSikkim/',views.EastSikkim,name='EastSikkim'),
    path('NorthSikkim/',views.NorthSikkim,name='NorthSikkim'),
    path('Anantapur/',views.Anantapur,name='Anantapur'),
    path('Kurnool/',views.Kurnool,name='Kurnool'),
    path('Bhagalpur/',views.Bhagalpur,name='Bhagalpur'),
    path('Katihar/',views.Katihar,name='Katihar'),
    path('Kendrapara/',views.Kendrapara,name='Kendrapara'),
    path('Puri/',views.Puri,name='Puri'),
    path('beed/',views.beed,name='beed'),
    path('jalna/',views.jalna,name='jalna'),
    path('belgaum/',views.belgaum,name='belgaum'),
    path('bagalkot/',views.bagalkot,name='bagalkot'),
    path('Dharam/',views.Dharam,name='Dharam'),
    path('Tiru/',views.Tiru,name='Tiru'),
    path('Tika/',views.Tika,name='Tika'),
    path('Predict/',views.Predict,name='Predict'),
    path('floodpredict/',views.floodpredict,name='floodpredict'),
    path('droughtpredict/',views.droughtpredict,name='droughtpredict'),
    
    path('Bharuch/',views.Bharuch,name='Bharuch'),
    path('aurang/',views.aurang,name='aurang'),
  
    


    path('WindyCyclone/', views.WindyCyclone, name='WindyCyclone'),

    
    path('course/<int:courseid>',views.courseDetails),
]
