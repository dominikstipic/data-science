from bs4 import BeautifulSoup
import re

with open("a.html") as fp:
    text = fp.readlines()
text = "\n".join(text)

bs = BeautifulSoup(text, "html.parser")
scripts = bs.find_all("script")
results = []

for s in scripts:
    href = s.get("src")
    if s.get("src"):
        results.append(href)
    else:
        text = s.text
        links = re.findall("https.+", text)
        results += links


