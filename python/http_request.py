# making HTTP request
import json
from urllib.request import urlopen

def send_request(key):
    base_url = 'https://jsonmock.hackerrank.com/api/moviesdata/search/?Title='
    api_url = f'{base_url}{key}'
    print(api_url)
    # body = urlopen(api_url).read()
    with urlopen(api_url) as response:
        body = response.read()

    data = json.loads(body)

    print(data['data'])

send_request('maze')
