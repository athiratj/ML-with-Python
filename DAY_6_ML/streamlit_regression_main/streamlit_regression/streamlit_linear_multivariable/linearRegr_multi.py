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

pickle_in = open('linearRegr_multi.pkl', 'rb')
classifier = pickle.load(pickle_in)
#Creating the UI for the application:

st.sidebar.header('Price Prediction of Bosten House Using multivarient linera Regression')
select = st.sidebar.selectbox('Select Form', ['Form 1'], key='1')
if not st.sidebar.checkbox("Hide", True, key='1'):
    st.title('Price Prediction')
    name = st.text_input("Name:")
    CRIM= st.number_input("per capita crime rate by town :")
    ZN = st.number_input("proportion of residential land zoned for lots over 25,000 sq.ft. :")
    INDUS =  st.number_input("proportion of non-retail business acres per town:")
    CHAS= st.number_input("Charles River dummy variable (= 1 if tract bounds      river; 0 otherwise) :")
    NOX = st.number_input("nitric oxides concentration (parts per 10 million):")
    RM =  st.number_input("average number of rooms per dwelling")
    AGE= st.number_input("proportion of owner-occupied units built prior to 1940")
    DIS = st.number_input("weighted distances to five Boston employment centres")
    RAD =  st.number_input("index of accessibility to radial highways")
    TAX= st.number_input("full-value property-tax rate per $10,000 :")
    PTRATIO = st.number_input("pupil-teacher ratio by town:")
    B =  st.number_input("1000(Bk - 0.63)^2 where Bk is the proportion of blacks  by town")
    LSTAT = st.number_input("% lower status of the population")
    MEDV =  st.number_input(" Median value of owner-occupied homes in $1000's :")
    submit = st.button('Predict')
    if submit:
        prediction = classifier.predict([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX,PTRATIO, B, LSTAT]])
        st.write('Congratulation',prediction,'You are not diabetic')
