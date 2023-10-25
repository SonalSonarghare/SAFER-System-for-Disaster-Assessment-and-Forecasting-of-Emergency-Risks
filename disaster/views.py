import requests
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
import folium
import requests
WINDY_API_KEY = 'qEGKjsz7ZvXcp7Fy3L0y9wwlNzZaHx57'

def get_windy_forecast():
    url = f'https://api.windy.com/map-forecast/forecast/v2?latitude=37.7833&longitude=-122.4167'
    headers = {'Authorization': WINDY_API_KEY}
    response = requests.get(url, headers=headers)
    
    print(response.text)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def homePage(request):
    data={
        'title':'Home Page',
        'bdata':'Welcome to SAFER',
        'clist':['PHP','JAVA','Django'],
        'student_details':[
            {'name':'sonal','phone':9341278567},
            {'name':'testing','phone':9671254907},
        ]
        
    }
    return render(request,"index.html",data)

def Home(request):
    return render(request,"home.html")
def drought(request):
    return render(request,"drought.html")
def flood(request):
    return render(request,"flood.html")
def cyclone(request):
    return render(request,"cyclone.html")
def FloodAssessment(request):
    return render(request,"FloodAssessment.html")
def map(request):
    return render(request,"map.html")
def UP(request):
    return render(request,"UP.html")
def Gorakhpur(request):
    return render(request,"Floods-Maps/Gorakhpur.html")
def SiddharthNagar(request):
    return render(request,"Floods-Maps/SiddharthNagar.html")
def Kullu(request):
    return render(request,"Floods-Maps/Kullu.html")
def Solan(request):
    return render(request,"Floods-Maps/Solan.html")
def Idukki(request):
    return render(request,"Floods-Maps/Idukki.html")
def Palakkad(request):
    return render(request,"Floods-Maps/Palakkad.html")
def Darrang(request):
    return render(request,"Floods-Maps/Darrang.html")
def Marigaon(request):
    return render(request,"Floods-Maps/Marigaon.html")
def EastSikkim(request):
    return render(request,"Floods-Maps/East Sikkim.html")
def NorthSikkim(request):
    return render(request,"Floods-Maps/North Sikkim.html")
def Anantapur(request):
    return render(request,"Floods-Maps/Anantapur.html")
def Kurnool(request):
    return render(request,"Floods-Maps/Kurnool.html")
def Katihar(request):
    return render(request,"Floods-Maps/Katihar.html")
def Bhagalpur(request):
    return render(request,"Floods-Maps/Bhagalpur.html")
def Puri(request):
    return render(request,"Floods-Maps/Puri.html")
def Kendrapara(request):
    return render(request,"Floods-Maps/Kendrapara.html")
def Predict(request):
    return render(request,"Predict.html")








def WindyCyclone(request):
    forecast_data = get_windy_forecast()
    return render(request,"WindyCyclone.html", {'forecast_data': forecast_data})
    













def course(request):
    return HttpResponse("<b>Welcome to course")


def courseDetails(request,courseid):
    return HttpResponse(courseid)
    