# main.py

import streamlit as st
import openai
from webpage_analysis import analyze_webpage, merge_schemas, validate_schema

st.set_page_config(page_title="Schema Markup Analysis")

# Get API key from secrets
api_key = st.secrets["openai_api_key"]

# Initialize OpenAI with the API key
openai.api_key = api_key

st.title("Schema Markup Analysis App")

url = st.text_input("Enter URL", "")

if url:
    st.markdown("### Analyzing webpage and generating schema markup...")
    webpage_text, current_schema, new_schema = analyze_webpage(url, openai)

    st.markdown("### Merging current and new schema markup...")
    merged_schema = merge_schemas(current_schema, new_schema)

    st.json(merged_schema)

    st.markdown("### Validating schema markup...")
    is_valid, validation_errors = validate_schema(merged_schema)

    if is_valid:
        st.success("Schema markup is valid!")
    else:
        st.error("Schema markup validation failed. Errors:")
        st.write(validation_errors)
