from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="City Temperature Web Service")

@app.get("/weather")
def get_temperature(city: pune):
    """
    Fetches the current temperature for a given city name.
    """
    if not city:
        raise HTTPException(status_code=400, detail="City parameter is required.")
        
    # Step 1: Convert city name to latitude and longitude coordinates
    geo_url = f"https://open-meteo.com{city}&count=1&language=en&format=json"
    geo_response = requests.get(geo_url).json()
    
    if not geo_response.get("results"):
        raise HTTPException(status_code=404, detail=f"City '{city}' not found.")
        
    location = geo_response["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]
    city_name = location["name"]
    country = location.get("country", "")

    # Step 2: Fetch current temperature from Open-Meteo API
    weather_url = f"https://open-meteo.com{lat}&longitude={lon}&current=temperature_2m"
    weather_response = requests.get(weather_url).json()
    
    if "current" not in weather_response:
        raise HTTPException(status_code=500, detail="Failed to fetch weather data.")
        
    temp_celsius = weather_response["current"]["temperature_2m"]

    # Step 3: Return the combined information
    return {
        "city": city_name,
        "country": country,
        "latitude": lat,
        "longitude": lon,
        "temperature_celsius": temp_celsius,
        "temperature_fahrenheit": round((temp_celsius * 9/5) + 32, 2)
    }
