import requests
from bs4 import BeautifulSoup

html = requests.get("https://burzarada.hzz.hr/Posloprimac_RadnaMjesta.aspx?AspxAutoDetectCookieSupport=1")
text = html.text

bs = BeautifulSoup(text, "html.parser")
trs = bs.find("table").find_all("tr")[0]

import pdb; pdb.set_trace()


# time till elections for each state
# Local 
# National

# Prompt: 

# Current ruling party. 

# Ownership and control of labour

# LLMS
# https://duck.ai/chat?ia=chat&origin=funnel_home_searchresults&t=ffab&duckai=1&home=1&prompt=1
# https://copilot.microsoft.com/?intent=bing&showconv=1
# https://github.com/eugeneyan/open-llms
# Negotiate the search.

# JOB MARKETS
# Kosovo: https://kosovajob.com/
# Austria: https://bund.jobboerse.gv.at/sap/bc/jobs/
# Slovenia: 
# China: 
# 

# There are disrepencies
# Europen Union: https://europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=10&orderBy=BEST_MATCH&locationCodes=hr&lang=en


# Send an email to political studies