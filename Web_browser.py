#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

st.title("Japanese Quiz")

# Question 1
st.subheader("1. What does 'inu' mean?")
q1 = st.radio("Choose one:", ["Dog", "Cat", "Fish"])

# Question 2
st.subheader("2. How do you say 'Good afternoon' in Japanese?")
q2 = st.radio("Choose one:", ["Konnichiwa", "Arigatou", "Sayonara"])

# Submit button
if st.button("Submit"):
    score = 0
    if q1 == "Dog":
        score += 1
    if q2 == "Konnichiwa":
        score += 1
    st.success(f"You scored {score}/2")

