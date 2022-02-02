import requests
import os
from requests_oauthlib import OAuth1
from dotenv import load_dotenv

load_dotenv()
my_key = os.getenv('KEY')
my_secret = os.getenv('SECRET')

auth = OAuth1(my_key, my_secret)
endpoint = "http://api.thenounproject.com/icon/1"

response = requests.get(endpoint, auth=auth)
print(response.content)
