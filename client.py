import json
import requests

data = {
    "features": [1,2,3,4]
}

url = 'http://0.0.0.0:8000/predict/'

data = json.dumps(data)

response = requests.post(url, data)

print(response.json())