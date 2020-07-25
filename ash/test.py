import requests

url = "https://googles.p.rapidapi.com/breweries"

headers = {
    'x-rapidapi-host': "googles.p.rapidapi.com",
    'x-rapidapi-key': "9ac03de5b2msh3509d8b0173771bp17e801jsn1977f19b9d85"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)