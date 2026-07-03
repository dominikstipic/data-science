from bs4 import BeautifulSoup
import re

with open("a.html") as fp:
    text = fp.readlines()
text = "\n".join(text)

bs = BeautifulSoup(text, "html.parser")
text = bs.body
import pdb; pdb.set_trace()
print(text.split())
