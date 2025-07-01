# Weather App

## Overview

This is a Flask-based weather application that provides current weather conditions for cities worldwide. The application uses the Foreca Weather API to fetch real-time weather data and presents it through a clean, responsive web interface with Bootstrap styling and dark theme support.

## System Architecture

The application follows a simple three-tier architecture:

1. **Presentation Layer**: HTML templates with Bootstrap CSS and JavaScript for user interaction
2. **Application Layer**: Flask web framework handling HTTP requests and business logic
3. **Data Layer**: External API integration with Foreca Weather service

The architecture is designed for simplicity and ease of deployment, making it suitable for educational purposes and small-scale applications.

## Key Components

### Backend Components

- **Flask Application (`app.py`)**: Main web application with route handlers for the home page and weather search functionality
- **Weather Service (`weather_service.py`)**: Service class that encapsulates all interactions with the Foreca Weather API
- **Main Entry Point (`main.py`)**: Simple module that imports the Flask app for deployment

### Frontend Components

- **HTML Templates (`templates/index.html`)**: Single-page template that handles both the search form and weather results display
- **CSS Styling (`static/style.css`)**: Custom styles for weather cards, gradients, and responsive design elements
- **JavaScript (`static/app.js`)**: Client-side functionality for form handling, loading states, and UI interactions

### External Dependencies

- **Foreca Weather API**: Primary data source for weather information
- **Bootstrap 5**: CSS framework for responsive design and dark theme
- **Font Awesome**: Icon library for weather and UI icons

## Data Flow

1. User enters a city name in the search form
2. Form submission triggers a POST request to `/search` endpoint
3. Flask app extracts city name and calls WeatherService
4. WeatherService searches for locations matching the city name
5. If locations found, service fetches current weather for the first match
6. Weather data is passed to the template for rendering
7. User sees weather information or error messages via flash notifications

## External Dependencies

### API Services
- **Foreca Weather API**: Provides location search and current weather data
  - Authentication: JWT Bearer token
  - Endpoints: Location search and current weather
  - Rate limiting: Handled by API provider

### Frontend Libraries
- **Bootstrap 5**: UI framework with dark theme support
- **Font Awesome 6**: Icon library for weather symbols and UI elements

### Python Packages
- **Flask**: Web framework for routing and templating
- **requests**: HTTP client for API calls
- **logging**: Built-in logging for debugging and monitoring

## Deployment Strategy

The application is designed for simple deployment with minimal configuration:

- **Environment Variables**: 
  - `FORECA_API_TOKEN`: Optional API token override
  - `SESSION_SECRET`: Flask session security key
- **Static Files**: Served directly by Flask for development
- **Production Considerations**: Would benefit from reverse proxy and static file CDN

## Changelog

- July 01, 2025. Initial setup

## User Preferences

Preferred communication style: Simple, everyday language.