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
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}], max_tokens=1000)
    new_schema = response.choices[0].message['content'].strip()

    return webpage_text, current_schema, new_schema

def merge_schemas(old_schema, new_schema, openai):
    prompt = f"Merge the following two schemas:\n\nOld Schema: {old_schema}\nNew Schema: {new_schema}"
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}], max_tokens=1000)
    merged_schema = response.choices[0].message['content'].strip()

    return merged_schema

def validate_schema(schema, openai):
    prompt = f"Validate the following schema: {schema}"
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}], max_tokens=1000)
    validation_result = response.choices[0].message['content'].strip()

    return validation_result
