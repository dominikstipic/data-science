from PyPDF2 import PdfReader
import requests
import fitz
from llm import deepseek_input, deepseek_input_prompt

url = "https://optiver.com/wp-content/uploads/2022/10/220928_Optiver-privacy-policy_Sep2022_FINAL.pdf"
response = requests.get(url)
data = response.content

pdf_doc = fitz.open(stream=data, filetype="pdf")
full_text = ""
for page in pdf_doc:
    full_text += page.get_text()
pdf_doc.close()




out = deepseek_input_prompt("Create a table which shows the personal data which company collects", 
                     full_text)
print(out)

#text = data.decode("utf-32")
#print(text)

