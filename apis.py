import requests
import json
responses= requests.get("https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow")
for data in responses.json()['items']:
    print(data['title'])
    print(data['link'])
    print()