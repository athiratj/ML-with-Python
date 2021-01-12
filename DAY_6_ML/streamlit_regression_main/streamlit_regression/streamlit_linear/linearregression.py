#Loading the required libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

#Calling the model we saved above:

pickle_in = open('linearRegr.pkl', 'rb')
classifier = pickle.load(pickle_in)
#Creating the UI for the application:


st.title('Sales Prediction Using Linear Regression')
name = st.text_input("Name:")
Advertisments= st.number_input("No. of Advertisments:")
submit = st.button('Predict')
if submit:
    prediction = classifier.predict([[Advertisments]])
    st.write('Possible Sales will be ',prediction)
