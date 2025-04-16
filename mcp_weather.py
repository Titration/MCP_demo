from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
import requests

app = FastAPI()

NWS_API_BASE = "https://api.weather.gov"
HEADERS = {
    "User-Agent": "(WeatherMCPDemo, contact@example.com)",
    "Accept": "application/json"
}

@app.get("/")
def read_root():
    return {"message": "Weather MCP Service"}

@app.get("/weather/{lat}/{lon}", operation_id="get_weather_location_lat_lon")
def get_weather(lat: float, lon: float):
    try:
        # Get the forecast office and grid coordinates
        points_url = f"{NWS_API_BASE}/points/{lat},{lon}"
        points_response = requests.get(points_url, headers=HEADERS)
        points_data = points_response.json()

        # Get the forecast
        forecast_url = points_data['properties']['forecast']
        forecast_response = requests.get(forecast_url, headers=HEADERS)
        forecast_data = forecast_response.json()

        # Return simplified weather data
        current_period = forecast_data['properties']['periods'][0]
        return {
            "location": {
                "city": points_data['properties']['relativeLocation']['properties']['city'],
                "state": points_data['properties']['relativeLocation']['properties']['state']
            },
            "current": {
                "temperature": current_period['temperature'],
                "temperature_unit": current_period['temperatureUnit'],
                "forecast": current_period['shortForecast']
            }
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/alerts/{lat}/{lon}", operation_id="get_alerts_location_lat_lon")
def get_alerts(lat: float, lon: float):
    try:
        alerts_url = f"{NWS_API_BASE}/alerts/active"
        response = requests.get(
            alerts_url,
            params={"point": f"{lat},{lon}"},
            headers=HEADERS
        )
        alerts_data = response.json()
        
        return {
            "alerts": [
                {
                    "event": alert['properties']['event'],
                    "severity": alert['properties']['severity'],
                    "headline": alert['properties']['headline']
                }
                for alert in alerts_data['features']
            ] if alerts_data.get('features') else []
        }
    except Exception as e:
        return {"error": str(e)}
    


# Add the MCP server to your FastAPI app
mcp = FastApiMCP(
    app,  
    name="My API MCP",  # Name for your MCP server
    description="MCP server for my API",  # Description
    base_url="http://localhost:8000"  # Where your API is running
)

# Mount the MCP server to your FastAPI app
mcp.mount()

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
