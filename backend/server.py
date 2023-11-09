#from flask import Flask, render_template, request
import pandas as pd
import requests as rq

from flask import Flask, abort, current_app, request, render_template
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api_key = 'fXEzJ1nKIxwyo9y2PBVAoQ'
url = 'https://www.carboninterface.com/api/v1/estimates'

@app.route('/', methods=['POST'])
def calculate_emissions():
    data = request.get_json()
    airport_1 = data['airport_1']
    airport_2 = data['airport_2']

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    data = {"type": "flight","passengers": 2,"legs": [{"departure_airport": airport_1, "destination_airport": airport_2}]
}
    response = rq.post(url, headers=headers, json=data)
    result = response.json()

    data = result['data']['attributes']
    df = pd.DataFrame(data = data)
    carbon_emission_flight = "Carbon Emissions (grams): " + str(df['carbon_g'][0])

    # Convert the dictionary to a JSON-formatted string
    json_data = json.dumps(carbon_emission_flight)

        # Set the appropriate response headers for JSON data
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )

    return response

    

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5500, debug = True)
