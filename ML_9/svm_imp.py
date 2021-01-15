import streamlit as st
import pandas as pd
import pickle
st.write("""
# SVM implementation app
 """)
svm_classifier = open('svm_model.pkl','rb')
classifier = pickle.load(svm_classifier)
#Text Input
age = st.text_input("Enter the Age",)
salary = st.text_input("Enter the Salary: (Salary in Rupees)")
gender =  st.text_input("Enter the Gender: (1-Male,0-Female)")
submit = st.button("Classify")

if submit:
	result = classifier.predict([[age,salary,gender]])
	if result ==0:
		st.write("yes")
	else:
		st.write("No")		
		#st.write(result)
