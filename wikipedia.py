import requests
import json

query = 'format=json&action=query&titles=United%20Kingdom&prop=revisions&rvprop=content'
request = requests.get('http://en.wikipedia.org/w/api.php?' + query)

pageid = request.json()['query']['pages'].keys()[0]
print request.json()['query']['pages'][pageid]['revisions'][0]['*']