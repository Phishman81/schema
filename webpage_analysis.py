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

def merge_schemas(old_schema, new_schema, openai):
    prompt = f"I have two schema markups from the same webpage. The first one is: {old_schema}. The second one is: {new_schema}. Please merge these two schemas and resolve any conflicts."
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1000)
    merged_schema = response.choices[0].text.strip()

    return merged_schema

def validate_schema(schema, openai):
    prompt = f"I have a schema markup: {schema}. Please check if it follows the best practices of schema.org vocabulary and suggest any corrections if needed."
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1000)
    validation_result = response.choices[0].text.strip()

    return validation_result

