import streamlit as st
import pandas as pd
from PIL import Image
import pickle
st.write("""
# Iris Flower Classification App
""")
#st.balloons()
img = Image.open("iris_flowers.jpeg")
st.image(img,width=600,caption='Iris Species')
#Load the Pickle file
irisclassifier = open('decision_tree.pkl', 'rb')
classifier = pickle.load(irisclassifier)

# Text Input
Sepal_Length = st.text_input("Enter the Sepal length",)
Sepal_Width = st.text_input("Enter the Sepal Width",)
Petal_Length = st.text_input("Enter the Petal length",)
Petal_Width = st.text_input("Enter the Petal Width",)
submit = st.button('Classify')

if submit:
    with st.spinner("Classifying.."):
        result = classifier.predict([[Sepal_Length,Sepal_Width,Petal_Length,Petal_Width]])
        st.write(result)
 
