import json
from  urllib.request import Request, urlopen

def getCases():

    url = 'https://corona.lmao.ninja/countries'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    data = json.loads(webpage)
    for country in data:
        if country['country'] == 'Brazil':
            return country
    