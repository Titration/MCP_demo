# Weather Service MCP Demo

A FastAPI-based weather service that provides current weather conditions and alerts using the National Weather Service (NWS) API. This service is integrated with MCP (Multi-Client Protocol) for easy access through Cursor.

## Features

- Get current weather conditions by latitude and longitude
- Get active weather alerts for any US location
- No API key required
- Real-time data from the National Weather Service
- Simple and easy-to-use MCP integration

## Prerequisites
- uv
- Python 3.13.3
- FastAPI
- Requests
- Uvicorn

## Setup
Run the server:
   ```bash
   uvicorn main:app --reload
   ```

## Usage

### Through MCP in Cursor

```python
# Get weather for a location (e.g., New York City)
weather = await mcp_My_First_MCP_server_get_weather_location_lat_lon(
    lat=40.7128,
    lon=-74.0060
)
print(weather)

# Get weather alerts
alerts = await mcp_My_First_MCP_server_get_alerts_location_lat_lon(
    lat=40.7128,
    lon=-74.0060
)
print(alerts)
```

### Example Response

```json
{
  "location": {
    "city": "New York",
    "state": "NY"
  },
  "current": {
    "temperature": 52,
    "temperature_unit": "F",
    "forecast": "Mostly Cloudy"
  }
}
```

### Common Test Locations

- New York City: 40.7128, -74.0060
- Los Angeles: 34.0522, -118.2437
- Chicago: 41.8781, -87.6298
- Miami: 25.7617, -80.1918

## API Endpoints

### Get Weather
- Endpoint: `/weather/{lat}/{lon}`
- Method: GET
- Parameters:
  - lat: Latitude (float)
  - lon: Longitude (float)
- Returns: Current weather conditions including temperature and forecast

### Get Alerts
- Endpoint: `/alerts/{lat}/{lon}`
- Method: GET
- Parameters:
  - lat: Latitude (float)
  - lon: Longitude (float)
- Returns: List of active weather alerts for the location

## Limitations

- Only works for locations within the United States (uses NWS API)
- Requires valid latitude and longitude coordinates
- Rate limited by the National Weather Service API

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- National Weather Service (NWS) for providing the weather data API
- FastAPI for the web framework
- MCP for the integration capabilities
