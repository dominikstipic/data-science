import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.bing.com/jobs?q=Internal+Audit%2C++Frankfurt&go=Search&qs=ds&form=JOBL2P&scp=0&c=1")
text = html.text

bs = BeautifulSoup(text, "html.parser")
import pdb; pdb.set_trace()