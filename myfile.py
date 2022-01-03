import streamlit as st
from PIL import Image

st.title("Merry Christmas and Happy New Year!")

image = Image.open('img/santa.jpg')
st.image(image, width=700)

st.write('“Gifts come and go, what really matters are the people who light up our lives all year long. Thank you!”')

def factorial(n):
    if n in (0, 1): return 1
    else: return n * factorial(n-1)

n = st.slider('Select the number.')
st.write('The factorial of {0} is {1}.'.format(n, factorial(n)))

st.text_input("Enter your name")