# main.py

import openai
import streamlit as st
from webpage_analysis import analyze_webpage, merge_schemas, validate_schema

def main():
    st.title('Schema Markup Analysis App')

    api_key = st.text_input("Enter your OpenAI API key", type="password")
    openai.api_key = api_key

    url = st.text_input("Enter the URL you want to analyze")

    if st.button("Analyze"):
        webpage_text, old_schema, new_schema = analyze_webpage(url, openai)

        merged_schema = merge_schemas(old_schema, new_schema, openai)

        validation_result = validate_schema(merged_schema, openai)

        st.write(f"Webpage Text: {webpage_text}")
        st.write(f"Old Schema: {old_schema}")
        st.write(f"New Schema: {new_schema}")
        st.write(f"Merged Schema: {merged_schema}")
        st.write(f"Validation Result: {validation_result}")

if __name__ == "__main__":
    main()
