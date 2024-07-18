"""from flask import Flask, render_template, request
import requests
import json
app= Flask(__name__)

from datetime import datetime

def timestamp_to_time(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%H:%M %p')

app.jinja_env.filters['timestamp_to_time'] = timestamp_to_time

@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello, World!'

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    api_key = '85464607a6a195b33d858a2b7bcda284'  
    weather_data = get_weather(city, api_key)
    if weather_data.get('cod') != 200:
        error_message = weather_data.get('message', 'City not found')
        return render_template('error.html', error_message=error_message)
    return render_template('weather.html', weather=weather_data)

    return render_template('weather.html', weather=weather_data)

def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
   app.run(debug=True)"""

from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

from datetime import datetime

def timestamp_to_time(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%H:%M %p')

app.jinja_env.filters['timestamp_to_time'] = timestamp_to_time

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        api_key = '85464607a6a195b33d858a2b7bcda284'
        weather_data = get_weather(city, api_key)
        if weather_data.get('cod') != 200:
            error_message = weather_data.get('message', 'City not found')
            return render_template('index.html', error_message=error_message)
        return render_template('index.html', weather=weather_data)
    return render_template('index.html')

def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    app.run(debug=True)
