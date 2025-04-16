# Weather API Demo

A simple weather API built with FastAPI that demonstrates basic CRUD operations.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

- `GET /`: Welcome message
- `POST /weather/{city}`: Report weather for a city
- `GET /weather/{city}`: Get weather data for a city

## Example Usage

1. Report weather for London:
   ```bash
   curl -X POST "http://localhost:8000/weather/london" \
        -H "Content-Type: application/json" \
        -d '{"temperature": 20.5, "humidity": 65, "conditions": "Partly cloudy"}'
   ```

2. Get weather for London:
   ```bash
   curl "http://localhost:8000/weather/london"
   ```