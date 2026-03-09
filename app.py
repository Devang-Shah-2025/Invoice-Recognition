## Invoice Extractor
from dotenv import load_dotenv

load_dotenv() ##load all env variables from .env file

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

## configuring api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini model and get response
def get_gemini_response(input, image, prompt):
    ## Swapped to the Flash model for free-tier compatibility
    model = genai.GenerativeModel("gemini-2.5-flash") 
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

## Initializing streamlit app
st.set_page_config(page_title="Invoice Extractor", page_icon=":money_with_wings:", layout="centered")

st.header("Gemini Invoice Extractor") # Updated header
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True) 

submit = st.button("Tell me the invoice details")

input_prompt = """
You are an expert in understanding Invoices. You will
receive input images as invoices and you will have to
answer questions based on the input image.
"""

## If submit button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)

    st.subheader("Response from Gemini")
    st.write(response)