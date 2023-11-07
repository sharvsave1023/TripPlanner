from flask import Flask, request, render_template
import pandas as pd
import requests as rq

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_emissions():
    if request.method == 'POST':
        api_key = 'YOUR_API_KEY'  # Replace with your Carbon Interface API key
        url = 'https://www.carboninterface.com/api/v1/estimates'

        departure_airport1 = request.form['departure_airport1']
        destination_airport1 = request.form['destination_airport1']

        departure_airport2 = request.form['departure_airport2']
        destination_airport2 = request.form['destination_airport2']

        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
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

        df = pd.DataFrame(data=[data])

        carbon_emissions1 = df['carbon_g'][0]
        carbon_emissions2 = df['carbon_g'][1]

        return render_template('result.html', carbon_emissions1=carbon_emissions1, carbon_emissions2=carbon_emissions2)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
