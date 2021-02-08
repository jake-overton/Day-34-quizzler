import requests

params = {"amount": 10}
response = requests.get("https://opentdb.com/api.php", params=params)
response.raise_for_status()
question_data = response.json()["results"]
