import requests
from pprint import pprint

sentiment_uri = "http://localhost:5000/text/analytics/v3.0/sentiment"

documents = {'documents' : [
  {'id': '1', 'language': 'fr', 'text': 'Nous sommes tres content du service fourni par le prestataire du diner'},
  {'id': '2', 'language': 'fr', 'text': 'La prestation est passable. '},  
  
]}

response  = requests.post(sentiment_uri, json=documents)
languages = response.json()

pprint(languages)