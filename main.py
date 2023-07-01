"""
# main.py

import openai
import streamlit as st
from webpage_analysis import analyze_webpage, merge_schemas, validate_schema

def main():
    try:
        st.title('Schema Markup Analysis App')

        # Error handling for API key
        api_key = st.text_input("Enter your OpenAI API key", type="password")
        if not api_key:
            st.warning("Please enter your OpenAI API key")
            return
        openai.api_key = api_key

        # Error handling for URL
        url = st.text_input("Enter the URL you want to analyze")
        if not url:
            st.warning("Please enter a URL")
            return

        if st.button("Analyze"):
            try:
                # Error handling for analysis
                webpage_text, old_schema, new_schema = analyze_webpage(url, openai)
                if not webpage_text:
                    st.error("Unable to fetch the webpage text")
                    return
                if not old_schema:
                    st.error("Unable to fetch the old schema")
                    return
                if not new_schema:
                    st.error("Unable to fetch the new schema")
                    return

                merged_schema = merge_schemas(old_schema, new_schema, openai)
                validation_result = validate_schema(merged_schema, openai)

                st.write(f"Webpage Text: {webpage_text}")
                st.write(f"Old Schema: {old_schema}")
                st.write(f"New Schema: {new_schema}")
                st.write(f"Merged Schema: {merged_schema}")
                st.write(f"Validation Result: {validation_result}")

            except Exception as e:
                st.error("An error occurred during analysis")
                st.error(str(e))
    except Exception as e:
        st.error("An error occurred")
        st.error(str(e))

if __name__ == "__main__":
    main()
"""

# Changes Made:
# - Added try-except block to catch any error that occurs during the program execution.
# - Displayed appropriate error messages for various error scenarios.
# - Imported the necessary functions from the module `webpage_analysis`.
# - Added a check for API key and URL input fields to ensure they are not empty.
# - Wrapped the main functionality inside a button click event to trigger the analysis.
# - Displayed the fetched webpage text, old schema, new schema, merged schema, and validation result using `st.write()`.
# - Added appropriate error handling for the analysis process and displayed error messages to the user
