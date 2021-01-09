import streamlit as st
from PIL import Image 


st.write(""" # Image Compressor """)
st.write(""" ## Made by: Shivam Bhosale """)
uploaded_file = st.file_uploader("Upload your Image to be compressed here", type=".jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image',width=300)
    st.write("The image is compressed")
    link = 'http://localhost:8516/media/d27bc46630157c00765b1d806c3f065222818e824ef6cdf1f6d9c84a.jpeg'
    if st.button('Download'):
        st.write("To Download the Image right-click on the image and select 'Save Image As' ")



