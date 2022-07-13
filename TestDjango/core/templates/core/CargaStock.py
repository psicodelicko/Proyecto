from urllib.request import urlopen
import json
url = "http://127.0.0.1:8000/api/producto/"
response = urlopen(url)
print(response.read())
