from bs4 import BeautifulSoup
import requests

req = requests.get("https://www.ycombinator.com/jobs")
html = req.text
bs = BeautifulSoup(html)
body = bs.body
import pdb; pdb.set_trace()
print(body.find_all("li"))