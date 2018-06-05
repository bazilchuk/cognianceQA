import requests

response = requests.get("http://qainterview.cogniance.com/candidates")

print(response.text)
print(response.status_code)