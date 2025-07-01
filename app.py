import os
import logging
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from weather_service import WeatherService

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "your-secret-key-here")

# Initialize weather service
weather_service = WeatherService()

@app.route('/')
def index():
    """Main page with search form"""
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_weather():
    """Handle weather search requests"""
    try:
        city = request.form.get('city', '').strip()
        
        if not city:
            flash('Please enter a city name', 'error')
            return redirect(url_for('index'))
        
        # Search for location
        locations = weather_service.search_location(city)
        
        if not locations:
            flash(f'No locations found for "{city}". Please try a different city name.', 'error')
            return redirect(url_for('index'))
        
        # Use the first location found
        location = locations[0]
        location_id = location['id']
        
        # Get current weather
        current_weather = weather_service.get_current_weather(location_id)
        
        if not current_weather:
            flash(f'Unable to get weather data for {location["name"]}. Please try again later.', 'error')
            return redirect(url_for('index'))
        
        return render_template('index.html', 
                             weather=current_weather, 
                             location=location,
                             search_query=city)
        
    except Exception as e:
        logging.error(f"Error in search_weather: {str(e)}")
        flash('An error occurred while fetching weather data. Please try again.', 'error')
        return redirect(url_for('index'))

@app.route('/api/search', methods=['POST'])
def api_search():
    """API endpoint for AJAX weather searches"""
    try:
        data = request.get_json()
        city = data.get('city', '').strip()
        
        if not city:
            return jsonify({'error': 'City name is required'}), 400
        
        # Search for location
        locations = weather_service.search_location(city)
        
        if not locations:
            return jsonify({'error': f'No locations found for "{city}"'}), 404
        
        # Use the first location found
        location = locations[0]
        location_id = location['id']
        
        # Get current weather
        current_weather = weather_service.get_current_weather(location_id)
        
        if not current_weather:
            return jsonify({'error': f'Unable to get weather data for {location["name"]}'}), 500
        
        return jsonify({
            'weather': current_weather,
            'location': location
        })
        
    except Exception as e:
        logging.error(f"Error in api_search: {str(e)}")
        return jsonify({'error': 'An error occurred while fetching weather data'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
