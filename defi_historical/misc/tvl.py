import requests
import json 


# get all protocols supported by DeFi Llama
llama_project_names = requests.get('https://api.llama.fi/protocols')
llama_project_names = llama_project_names.json()

# throw all the protocol names in a list 
project_names = []
for x in llama_project_names: 
    project_names.append(x['name'])

# iterate over list of projects to retrieve TVL history 
for y in project_names:
    tvl = requests.get('https://api.llama.fi/protocol/' + y.replace(" ", "-"))
    tvl = tvl.json()
    print(tvl)
