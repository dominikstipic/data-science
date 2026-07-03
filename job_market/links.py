from bs4 import BeautifulSoup
import re

with open("a.html") as fp:
    text = fp.readlines()
text = "\n".join(text)

bs = BeautifulSoup(text, "html.parser")
results = []
print(bs)


for s in bs.body:
    break
    href = s.get("src")
    if s.get("src"):
        results.append(href)
    else:
        text = s.text
        links = re.findall("https.+", text)
        results += links

for r in results:
    print(r)
