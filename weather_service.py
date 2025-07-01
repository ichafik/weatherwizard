import os
import requests
import logging
from typing import List, Dict, Optional

class WeatherService:
    """Service class for interacting with Foreca Weather API"""
    
    def __init__(self):
        # Get JWT token from environment or use the provided one
        self.api_token = os.getenv("FORECA_API_TOKEN", 
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9wZmEuZm9yZWNhLmNvbVwvYXV0aG9yaXplXC90b2tlbiIsImlhdCI6MTc1MTM1NDAyMCwiZXhwIjo5OTk5OTk5OTk5LCJuYmYiOjE3NTEzNTQwMjAsImp0aSI6IjMyZjkxNDI1OTMxN2RjYjciLCJzdWIiOiJpbXJhbmUtY2hhZmlrIiwiZm10IjoiWERjT2hqQzQwK0FMamxZVHRqYk9pQT09In0.wavsO4zvQFWtxeARcElkCHG-rJFBJw3w5dNO1quuiE8")
        
        self.base_url = "https://pfa.foreca.com/api/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        
    def search_location(self, query: str) -> List[Dict]:
        """
        Search for locations matching the query
        
        Args:
            query: City name or location query
            
        Returns:
            List of location dictionaries
        """
        try:
            url = f"{self.base_url}/location/search/{query}"
            params = {
                "lang": "en"
            }
            
            logging.debug(f"Searching location: {url}")
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                locations = data.get('locations', [])
                logging.debug(f"Found {len(locations)} locations for query: {query}")
                return locations
            else:
                logging.error(f"Location search failed with status {response.status_code}: {response.text}")
                return []
                
        except requests.exceptions.Timeout:
            logging.error("Location search timed out")
            return []
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error in location search: {str(e)}")
            return []
        except Exception as e:
            logging.error(f"Unexpected error in location search: {str(e)}")
            return []
    
    def get_current_weather(self, location_id: int) -> Optional[Dict]:
        """
        Get current weather for a location ID
        
        Args:
            location_id: Location identifier from search results
            
        Returns:
            Weather data dictionary or None if failed
        """
        try:
            url = f"{self.base_url}/current/{location_id}"
            params = {
                "tempunit": "C",
                "windunit": "MS",
                "lang": "en"
            }
            
            logging.debug(f"Getting current weather: {url}")
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                current_weather = data.get('current', {})
                logging.debug(f"Successfully retrieved weather data for location {location_id}")
                return current_weather
            else:
                logging.error(f"Current weather request failed with status {response.status_code}: {response.text}")
                return None
                
        except requests.exceptions.Timeout:
            logging.error("Current weather request timed out")
            return None
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error in current weather: {str(e)}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error in current weather: {str(e)}")
            return None
    
    def get_weather_icon_class(self, symbol: str) -> str:
        """
        Convert Foreca weather symbol to appropriate icon class
        
        Args:
            symbol: Foreca weather symbol code (e.g., 'd000', 'n421')
            
        Returns:
            CSS class for weather icon
        """
        if not symbol:
            return "fas fa-question"
        
        # Extract the numeric part
        code = symbol[1:] if len(symbol) > 1 else "000"
        
        # Map Foreca symbols to Font Awesome icons
        icon_mapping = {
            "000": "fas fa-sun",           # Clear
            "100": "fas fa-cloud-sun",     # Partly cloudy
            "200": "fas fa-cloud",         # Cloudy
            "300": "fas fa-cloud-rain",    # Light rain
            "400": "fas fa-cloud-rain",    # Rain
            "500": "fas fa-cloud-rain",    # Heavy rain
            "600": "fas fa-snowflake",     # Snow
            "700": "fas fa-bolt",          # Thunderstorm
            "800": "fas fa-smog",          # Fog
        }
        
        # Find the best match
        for key, icon in icon_mapping.items():
            if code.startswith(key[0]):
                return icon
        
        return "fas fa-cloud"  # Default icon
