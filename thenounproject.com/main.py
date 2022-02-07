"""
Save picture from API

"""

import requests
import os
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
from urllib.parse import urljoin    # parse urls pathes


load_dotenv()

# auth = OAuth1(os.getenv('KEY'), os.getenv('SECRET'))
# endpoint = "http://api.thenounproject.com/icon/1"
#
# response = requests.get(endpoint, auth=auth)

# response.content  - vozvrashaet sostoyanie v vide byitov
# print(response.content)

# po json ydobno smotret result cherez debugger postaviv tochky ostanovki na printe resulta
# result = response.json()
# print(result)

# icon_url = result['icon']['icon_url']
# print(icon_url)


class IconGetter:
    def __init__(self):
        self._auth = OAuth1(os.getenv('KEY'), os.getenv('SECRET'))
        self._endpoint = "http://api.thenounproject.com/icon/"
        self.icon = None

    def get_icon(self, icon_id):
        url = urljoin(self._endpoint, str(icon_id))     # sostavlyaem pravilno url path
        response = requests.get(url, auth=self._auth)
        result = response.json()
        icon_url = result['icon']['icon_url']
        self.icon = self._get_icon(icon_url)

    def _get_icon(self, icon_url):
        response = requests.get(icon_url)
        return response.content

    def write_icon(self, filename):
        with open(filename, 'wb') as file:
            file.write(self.icon)


icon_getter = IconGetter()
icon_getter.get_icon("sun")    # icon_getter.get_icon(23)
icon_getter.write_icon('img/image.svg')
