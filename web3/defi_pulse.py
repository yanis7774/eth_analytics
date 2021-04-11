import requests 
import json 


# input your token here
api_key = ''

url = 'https://data-api.defipulse.com/api/v1/defipulse/api/GetHistory?api-key=' + api_key
response = requests.get(url)
result = json.loads(response.text)
print(result[0]['tvlUSD'])

