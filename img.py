# -*- coding: utf-8 -*-
"""
Created on Thu jun  8 22:06:05 2024

@author: siddhardhan
"""

import openai
import urllib.request
import cv2
import streamlit as st

openai.api_key = "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"

def generate_image(image_description):

    img_response = openai.Image.create(
        prompt=image_description,
        n=1,
        size="512x512"
    )

    img_url = img_response['data'][0]['url']

    urllib.request.urlretrieve(img_url, 'img.png')

    # Load image using OpenCV
    img = cv2.imread("img.png")

    # Convert BGR (OpenCV default) to RGB for display in Streamlit
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  
    return img_rgb

# page title
st.title('DALL.E - Image Generation - OpenAI')

# text input box for image description
img_description = st.text_input('Image Description')

if st.button('Generate Image'):
    generated_img = generate_image(img_description)
    st.image(generated_img)
