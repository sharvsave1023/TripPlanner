import pandas as pd
import numpy as np
import requests as rq

api_key = 'fXEzJ1nKIxwyo9y2PBVAoQ'
url = 'https://www.carboninterface.com/api/v1/estimates'

departure_airport1 = input("Enter Departing Airport 1: ")
destination_airport1 = input("Enter Destination Airport 1: ")

departure_airport2 = input("Enter Departing Airport 2: ")
destination_airport2 = input("Enter Destination Airport 2: ")

headers = {
    'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'
}

data = {"type": "flight","passengers": 2,"legs": [{"departure_airport": departure_airport1, "destination_airport": destination_airport1},
        {"departure_airport": departure_airport2, "destination_airport": destination_airport2}
    ]
}

response = rq.post(url, headers=headers, json=data)
result = response.json()

data = result['data']['attributes']

df = pd.DataFrame(data = data)

print("Carbon Emissions To Flight (Grams): ", df['carbon_g'][0])
print("Carbon Emissions Return Flight (Grams): ", df['carbon_g'][1])