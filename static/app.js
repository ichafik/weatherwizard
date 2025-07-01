// Weather App JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('weatherForm');
    const searchBtn = document.getElementById('searchBtn');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const cityInput = document.getElementById('cityInput');

    // Handle form submission
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            // Show loading indicator
            showLoading();
            
            // Disable search button to prevent double submission
            if (searchBtn) {
                searchBtn.disabled = true;
                searchBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Searching...';
            }
        });
    }

    // Handle input focus
    if (cityInput) {
        cityInput.addEventListener('focus', function() {
            this.select(); // Select all text when focused
        });

        // Handle Enter key press
        cityInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                searchForm.submit();
            }
        });
    }

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Add some interactive features
    addWeatherCardAnimations();
    
    function showLoading() {
        if (loadingIndicator) {
            loadingIndicator.classList.remove('d-none');
        }
    }

    function hideLoading() {
        if (loadingIndicator) {
            loadingIndicator.classList.add('d-none');
        }
        
        // Reset search button
        if (searchBtn) {
            searchBtn.disabled = false;
            searchBtn.innerHTML = '<i class="fas fa-search me-2"></i>Search';
        }
    }

    function addWeatherCardAnimations() {
        const weatherCard = document.querySelector('.weather-card');
        if (weatherCard) {
            // Add fade-in animation
            weatherCard.style.opacity = '0';
            weatherCard.style.transform = 'translateY(20px)';
            
            setTimeout(function() {
                weatherCard.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                weatherCard.style.opacity = '1';
                weatherCard.style.transform = 'translateY(0)';
            }, 100);

            // Add hover effects to detail items
            const detailItems = document.querySelectorAll('.detail-item');
            detailItems.forEach(function(item) {
                item.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateX(5px)';
                    this.style.transition = 'transform 0.2s ease';
                });
                
                item.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateX(0)';
                });
            });
        }
    }

    // Add weather icon animations
    const weatherIcon = document.querySelector('.weather-icon');
    if (weatherIcon) {
        weatherIcon.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1) rotate(5deg)';
            this.style.transition = 'transform 0.3s ease';
        });
        
        weatherIcon.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1) rotate(0deg)';
        });
    }

    // Add temperature animation
    const temperature = document.querySelector('.temperature');
    if (temperature) {
        let originalText = temperature.textContent;
        
        // Animate the temperature number counting up
        let currentTemp = 0;
        let targetTemp = parseFloat(originalText);
        
        if (!isNaN(targetTemp)) {
            temperature.textContent = '0°C';
            
            let increment = targetTemp / 30; // 30 steps
            let counter = setInterval(function() {
                currentTemp += increment;
                if ((increment > 0 && currentTemp >= targetTemp) || 
                    (increment < 0 && currentTemp <= targetTemp)) {
                    currentTemp = targetTemp;
                    clearInterval(counter);
                }
                temperature.textContent = currentTemp.toFixed(1) + '°C';
            }, 50);
        }
    }

    // Hide loading indicator when page loads (in case of page refresh)
    hideLoading();
});

// Utility function to format wind direction
function getWindDirectionText(degrees) {
    const directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 
                       'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'];
    const index = Math.round(degrees / 22.5) % 16;
    return directions[index];
}

// Utility function to get weather description
function getWeatherDescription(symbol) {
    const descriptions = {
        'd000': 'Clear sky',
        'n000': 'Clear sky',
        'd100': 'Partly cloudy',
        'n100': 'Partly cloudy',
        'd200': 'Cloudy',
        'n200': 'Cloudy',
        'd300': 'Light rain',
        'n300': 'Light rain',
        'd400': 'Rain',
        'n400': 'Rain',
        'd500': 'Heavy rain',
        'n500': 'Heavy rain',
        'd600': 'Snow',
        'n600': 'Snow',
        'd700': 'Thunderstorm',
        'n700': 'Thunderstorm'
    };
    
    return descriptions[symbol] || 'Unknown conditions';
}
