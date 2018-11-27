
import requests
import os

host = os.getenv('DASHBOARD_HOST')

url = "http://{host}"
page = requests.get(url)
assert page.status == 200
