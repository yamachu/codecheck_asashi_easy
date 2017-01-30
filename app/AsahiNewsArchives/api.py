# -*- coding: utf-8 -*-
import urllib.request, urllib.parse
import json

class AsahiNewsAPI:
    BASE_URL = 'http://54.92.123.84/search'

    def __init__(self, access_key = None):
        self.access_key = access_key


    def search(self, query='*:*', sort=None, start=1, rows=10, wt='json'):
        params = {
            'q': query.encode('utf-8', 'surrogateescape').decode('utf-8', 'surrogateescape'),
            # 'sort': sort, -> 今後対応
            'start': start,
            'rows': rows,
            'wt': wt,
            'ackey': self.access_key
        }
        encoded_params = urllib.parse.urlencode(params, safe = ':')
        get_url = self.BASE_URL + '?' + encoded_params

        with urllib.request.urlopen(get_url) as resp:
            body = resp.read().decode('utf-8')
            return json.loads(body)
        