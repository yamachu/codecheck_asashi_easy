import requests

class AsahiNewsAPI:
    BASE_URL = 'http://54.92.123.84/search'

    def __init__(self, access_key = None):
        self.access_key = access_key


    def search(self, query='*:*', sort=None, start=1, rows=10, wt='json'):
        response = requests.get(
            self.BASE_URL,
            params={
                'q': query,
                'sort': sort,
                'start': start,
                'rows': rows,
                'wt': wt,
                'ackey': self.access_key
            })
        
        return response.json()