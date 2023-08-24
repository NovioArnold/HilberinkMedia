import requests

url = "https://go-train-delay.p.rapidapi.com/date/_search"

payload = { "query": { "must": { "ranges": [{ "date": {
						"gte": "2021-10-02",
						"lte": "2021-10-05"
					} }] } } }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "go-train-delay.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
