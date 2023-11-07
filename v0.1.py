import pandas as pd
import requests as rq
import PySimpleGUI as sg

api_key = 'fXEzJ1nKIxwyo9y2PBVAoQ'
url = 'https://www.carboninterface.com/api/v1/estimates'

# Define the layout for the GUI
layout = [
    [sg.Text("Departing Airport 1:"), sg.InputText(key='departure_airport1')],
    [sg.Text("Destination Airport 1:"), sg.InputText(key='destination_airport1')],
    [sg.Text("Departing Airport 2:"), sg.InputText(key='departure_airport2')],
    [sg.Text("Destination Airport 2:"), sg.InputText(key='destination_airport2')],
    [sg.Button("Calculate Carbon Emissions")],
    [sg.Text("", size=(30, 2), key='emissions_result')],
]

# Create the window
window = sg.Window("Carbon Emissions Calculator", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "Calculate Carbon Emissions":
        departure_airport1 = values['departure_airport1']
        destination_airport1 = values['destination_airport1']
        departure_airport2 = values['departure_airport2']
        destination_airport2 = values['destination_airport2']

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

        df = pd.DataFrame(data=[data])

        emissions_result = f"Carbon Emissions Outbound Flight (Grams): {df['carbon_g'][0]}\n"
        emissions_result += f"Carbon Emissions Return Flight (Grams): {df['carbon_g'][1]}"
        window['emissions_result'].update(emissions_result)

# Close the window
window.close()