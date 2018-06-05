import requests

url = "http://qainterview.cogniance.com/candidates"

response = requests.delete(url + "/" + "1395")

print(response.text)
