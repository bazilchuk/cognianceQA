import requests

url = "http://qainterview.cogniance.com/candidates"

payload = '{' \
          '"name": "Andrew",' \
          '"position": "QA"' \
          '}'

headers = {
    'Content-Type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
