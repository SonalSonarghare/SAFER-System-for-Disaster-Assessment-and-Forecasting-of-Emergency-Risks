import requests
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
import folium
import requests
from django.http import HttpResponse
from django.shortcuts import render
import requests
WINDY_API_KEY = 'qEGKjsz7ZvXcp7Fy3L0y9wwlNzZaHx57'

def WindyCyclone():
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
def drought(request):
    return render(request,"drought.html")
def FloodAssessment(request):
    return render(request,"FloodAssessment.html")
def map(request):
    return render(request,"map.html")
def map_drought(request):
    return render(request,"map_drought.html")
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
def Bharuch(request):
    return render(request,"Floods-Maps/Bharuch.html")
def aurang(request):
    return render(request,"Floods-Maps/aurang.html")
def beed(request):
    return render(request,"Floods-Maps/beed.html")
def jalna(request):
    return render(request,"Floods-Maps/jalna.html")
def belgaum(request):
    return render(request,"Floods-Maps/belgaum.html")
def bagalkot(request):
    return render(request,"Floods-Maps/bagalkot.html")
def Tiru(request):
    return render(request,"Floods-Maps/Tiru.html")
def Tika(request):
    return render(request,"Floods-Maps/Tika.html")
def Dharam(request):
    return render(request,"Floods-Maps/Dharm.html")
import requests
from django.http import HttpResponse
from django.shortcuts import render

# Define a function to fetch latitude and longitude from OpenCage Geocoding API
def get_lat_lng_from_place(Place, api_key):
    geocode_url = f'https://api.opencagedata.com/geocode/v1/json?q={Place}&key={api_key}'
    response = requests.get(geocode_url)

    if response.status_code == 200:
        data = response.json()
        if 'results' in data and len(data['results']) > 0:
            location = data['results'][0]['geometry']
            latitude = location['lat']
            longitude = location['lng']
            return latitude, longitude
    return None, None

# Modify your floodpredict function to use the retrieved coordinates
def floodpredict(request):
    if request.method == 'POST':
        place_name = request.POST.get('Place')  # Get the place name from the form
        api_key = '4b31dcc6fdca4338abc5e717396a40e9'  # Replace with your OpenCage API key
        latitude, longitude = get_lat_lng_from_place(place_name, api_key)

        if latitude is not None and longitude is not None:
            # Fetch river discharge data and rainfall data using the latitude and longitude
            river_discharge_api_url = f'https://flood-api.open-meteo.com/v1/flood?latitude={latitude}&longitude={longitude}&daily=river_discharge&past_days=31&forecast_days=7'
            river_discharge_response = requests.get(river_discharge_api_url)

            # Fetch current and hourly rainfall data using the provided API
            rainfall_api_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=rain&hourly=rain&timezone=auto&past_days=31'
            rainfall_response = requests.get(rainfall_api_url)

            # Your existing code for processing the data here
            if river_discharge_response.status_code == 200 and rainfall_response.status_code == 200:
                # Extract the current river discharge and current rainfall
                try:
                    current_river_discharge = float(river_discharge_response.json()['daily'][0]['river_discharge'])
                except KeyError:
                    current_river_discharge = None
                current_rainfall = float(rainfall_response.json()['current']['rain'])

                # Extract hourly rainfall data for the next few hours
                hourly_rainfall = rainfall_response.json()['hourly']['rain']

                # Calculate cumulative rainfall over the past few hours
                cumulative_rainfall = sum(hourly_rainfall)

                # Define flood thresholds
                river_discharge_threshold = 1.5  # Example threshold for river discharge
                rainfall_threshold = 50.0  # Example threshold for cumulative rainfall (adjust as needed)

                # Check if there might be a flood
                if current_river_discharge is not None and (current_river_discharge > river_discharge_threshold or cumulative_rainfall > rainfall_threshold):
                    result = "FLOOD"
                else:
                    result = "NO FLOOD"
            else:
                result = "Failed to fetch data. Status codes: River Discharge - " + str(river_discharge_response.status_code) + ", Rainfall - " + str(rainfall_response.status_code)
            # ...

            # Return the result
            return render(request, 'response.html', {'result': result}) # You can return the result as a response

        else:
            result = "Failed to fetch coordinates from the OpenCage Geocoding API."

    return render(request, 'floodpredict.html')  # Create a template for the form


def get_weather_data(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,soil_temperature_18cm,soil_moisture_9_to_27cm,relativehumidity_2m,precipitation,evapotranspiration,windspeed_10m&timezone=auto&past_days=14"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def predict_drought(weather_data):
    temperature_data = weather_data.get('hourly', {}).get('temperature_2m', [])
    soil_temperature_data = weather_data.get('hourly', {}).get('soil_temperature_18cm', [])
    soil_moisture_data = weather_data.get('hourly', {}).get('soil_moisture_9_to_27cm', [])
    relative_humidity_data = weather_data.get('hourly', {}).get('relativehumidity_2m', [])
    precipitation_data = weather_data.get('hourly', {}).get('precipitation', [])
    evapotranspiration_data = weather_data.get('hourly', {}).get('evapotranspiration', [])
    windspeed_data = weather_data.get('hourly', {}).get('windspeed_10m', [])

    # Your drought prediction logic here
    # You can analyze all the data to make predictions

    # For simplicity, let's assume a basic condition for drought
    if all(temperature > 35 for temperature in temperature_data) and \
       all(soil_temperature > 30 for soil_temperature in soil_temperature_data) and \
       all(moisture < 0.6 for moisture in soil_moisture_data) and \
       all(relative_humidity < 60 for relative_humidity in relative_humidity_data) and \
       all(precipitation < 2 for precipitation in precipitation_data) and \
       all(evapotranspiration > 0.5 for evapotranspiration in evapotranspiration_data) and \
       all(windspeed < 10 for windspeed in windspeed_data):
        return "Drought conditions are likely."
    else:
        return "No drought conditions detected."

def droughtpredict(request):
    if request.method == 'POST':
        place_name = request.POST.get('Place')  # Get the place name from the form
        api_key = '4b31dcc6fdca4338abc5e717396a40e9'  # Replace with your OpenCage API key
        latitude, longitude = get_lat_lng_from_place(place_name, api_key)

        if latitude is not None and longitude is not None:
            weather_data = get_weather_data(latitude, longitude)

            if weather_data:
                drought_prediction = predict_drought(weather_data)
                return render(request, 'response1.html', {'drought_prediction': drought_prediction})
            else:
                error_message = "Failed to fetch weather data. Please check the coordinates."
                return render(request, 'response1.html', {'error_message': error_message})
        else:
            error_message = "Failed to fetch coordinates from the OpenCage Geocoding API."
            return render(request, 'response1.html', {'error_message': error_message})


    return render(request, 'droughtpredict.html')



def WindyCyclone(request):
    forecast_data = get_windy_forecast()
    return render(request,"WindyCyclone.html", {'forecast_data': forecast_data})
    













def course(request):
    return HttpResponse("<b>Welcome to course")


def courseDetails(request,courseid):
    return HttpResponse(courseid)
    