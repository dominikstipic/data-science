# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
import random
import argparse
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
import requests
import fitz
from llm import deepseek_input, deepseek_input_prompt


def process_pdf(url):
    response = requests.get(url)
    data = response.content

    pdf_doc = fitz.open(stream=data, filetype="pdf")
    full_text = ""
    for page in pdf_doc:
        full_text += page.get_text()
    pdf_doc.close()
    out = deepseek_input_prompt("Create a bullet point dataframe table which shows the personal data which company collects. The name of column should be personal details.", 
                        full_text)
    return out



def process_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:149.0) Gecko/20100101 Firefox/149.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    response = requests.get(url, headers=headers)
    data = response.text

    out = deepseek_input_prompt(
        "Create a table which shows the personal data which company collects", 
        data)
    import pdb; pdb.set_trace()
    
    return out


parser = argparse.ArgumentParser("Privacy Tabel")
parser.add_argument("url")
args = parser.parse_args()
url = args.url
out = process_pdf(url)
print(out)

# parser = argparse.ArgumentParser(description="Deep Seek")
# parser.add_argument("url")
# args = parser.parse_args()
# url = args.url

# text = requests.get(url).text
# body = BeautifulSoup(text, "html.parser").body


# url = "https://optiver.com/wp-content/uploads/2022/10/220928_Optiver-privacy-policy_Sep2022_FINAL.pdf"
# print(url)

# #client = OpenAI(api_key="sk-c5b69a2435a54546815200ab6652903a", base_url="https://api.deepseek.com")



# https://api-docs.deepseek.com/quick_start/parameter_settings
# random_seed = random.randint(1, 1000000)
# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "user", "content": message},
#     ],
#     stream=False, 
#     max_tokens=100, 
#     temperature=1.3, 
#     seed=random_seed
# )
