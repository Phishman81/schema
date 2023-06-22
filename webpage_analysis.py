# webpage_analysis.py

import extruct
import requests
from bs4 import BeautifulSoup
from openai import ChatCompletion

def analyze_webpage(url, openai):
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html.parser")
    webpage_text = soup.get_text()

    current_schema = extruct.extract(html)

    # Create GPT-4 prompt to generate schema markup based on webpage content
    prompt = f"Generate a schema markup for a webpage with the following content: {webpage_text}"
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1000)
    new_schema = response.choices[0].text.strip()

    return webpage_text, current_schema, new_schema
