from flask import Flask, render_template, request
import pandas as pd
import requests as rq

app = Flask(__name__)

api_key = 'fXEzJ1nKIxwyo9y2PBVAoQ'
url = 'https://www.carboninterface.com/api/v1/estimates'

@app.route('/', methods=['GET', 'POST'])
def calculate_emissions():
    if request.method == 'POST':
        departure_airport1 = request.form['departure_airport1']
        destination_airport1 = request.form['destination_airport1']
        departure_airport2 = request.form['departure_airport2']
        destination_airport2 = request.form['destination_airport2']

        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        data = {
            "type": "flight",
            "passengers": 2,
            "legs": [
                {"departure_airport": departure_airport1, "destination_airport": destination_airport1},
                {"departure_airport": departure_airport2, "destination_airport": destination_airport2}
            ]
        }

        response = rq.post(url, headers=headers, json=data)
        result = response.json()
        data = result['data']['attributes']

        df = pd.DataFrame(data=data)

        carbon_emission_flight = df['carbon_g'][0]
        carbon_emission_return = df['carbon_g'][1]

        return render_template('index.html', carbon_emission_flight=carbon_emission_flight, carbon_emission_return=carbon_emission_return)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port = 5500, host = '127.0.0.1')