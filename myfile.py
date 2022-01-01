import streamlit as st
from PIL import Image

st.title("Merry Christmas and Happy New Year!")

image = Image.open('img/santa.jpg')
st.image(image, width=700)