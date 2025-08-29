#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st

st.title("Japanese Quiz")

# Question 1
st.subheader("1. What is the English for'あ'?")
q1 = st.radio("Choose one:", ["ka", "a", "u"])

# Question 2
st.subheader("2. What is the English for'い'?")
q2 = st.radio("Choose one:", ["u", "e", "i"])

# Question 3
st.subheader("2. What is the English for'う'?")
q2 = st.radio("Choose one:", ["u", "a", "i"])

# Question 4
st.subheader("2. What is the English for'え'?")
q2 = st.radio("Choose one:", ["e", "u", "i"])

# Question 5
st.subheader("2. What is the English for'お'?")
q2 = st.radio("Choose one:", ["u", "e", "o"])


# Submit button
if st.button("Submit"):
    score = 0
    if q1 == "a":
        score += 1
    if q1 !="a":
        print("Wrong answer")
    if q2 == "i":
        score += 1
    if q2 != "i":
        print("Wrong anser")
    if q3 == "u":
        score += 1
    if q3 != "u":
        print("Wrong anser")
    if q4 == "e":
        score += 1
    if q4 != "e":
        print("Wrong anser")
    if q5 == "o":
        score += 1
    if q5 != "o":
        print("Wrong anser")
    st.success(f"You scored {score}/5")






