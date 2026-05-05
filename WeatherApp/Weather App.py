import requests

def get_coordinates(city, state):
    """Get latitude and longitude using Open-Meteo Geocoding API"""
    try:
        url = "https://geocoding-api.open-meteo.com/v1/search"
        params = {
            "name": city,
            "count": 10,
            "country": "US",
            "format": "json"
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "results" not in data:
            return None

        # Match both city and state
        for result in data["results"]:
            if result.get("admin1", "").lower() == state.lower():
                return {
                    "lat": result["latitude"],
                    "lon": result["longitude"],
                    "city": result["name"],
                    "state": result["admin1"]
                }

        return None

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving location data: {e}")
        return None


def get_forecast(lat, lon):
    """Get 10-day forecast from Open-Meteo"""
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "daily": [
                "temperature_2m_max",
                "temperature_2m_min",
                "precipitation_sum"
            ],
            "temperature_unit": "fahrenheit",
            "precipitation_unit": "inch",
            "forecast_days": 10,
            "timezone": "auto"
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving weather data: {e}")
        return None


def display_forecast(user_city, user_state, location, data):
    """Display forecast in table format"""

    print("\n==============================================")
    print("        10-Day Weather Forecast")
    print("==============================================")

    # Show both user input and matched location
    print(f"Requested Location : {user_city}, {user_state}")
    print(f"Forecast Location  : {location['city']}, {location['state']}")
    print("----------------------------------------------")

    print("Date | Max Temp | Min Temp | Rain")
    print("-" * 50)

    daily = data["daily"]

    for i in range(len(daily["time"])):
        date = daily["time"][i]
        max_temp = daily["temperature_2m_max"][i]
        min_temp = daily["temperature_2m_min"][i]
        rain = daily["precipitation_sum"][i]

        print(f"{date} | {max_temp:.1f}°F | {min_temp:.1f}°F | {rain:.3f} inch")


def main():
    print("=== 10-Day Weather Forecast ===")

    user_city = input("Enter city: ").strip()
    user_state = input("Enter state (full name): ").strip()

    # Step 1: Get coordinates
    location = get_coordinates(user_city, user_state)

    if not location:
        print("Location not found. Please check the city and state.")
        return

    # Step 2: Get forecast
    forecast = get_forecast(location["lat"], location["lon"])

    if not forecast:
        print("Could not retrieve forecast data.")
        return

    # Step 3: Display results
    display_forecast(user_city, user_state, location, forecast)


if __name__ == "__main__":
    main()