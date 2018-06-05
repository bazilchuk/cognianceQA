import requests

url = "http://qainterview.cogniance.com/candidates"
id = "127"

response = requests.get(url + "/" + id)

print(response.text)
print(response.status_code)