import streamlit as st

st.title("Japanese Quiz")

# Question 1
st.subheader("1. What does '猫' mean?")
q1 = st.radio("Choose one:", ["Dog", "Cat", "Fish"])

# Question 2
st.subheader("2. How do you say 'ありがとう' in Japanese?")
q2 = st.radio("Choose one:", ["Konnichiwa", "Arigatou", "Sayonara"])

# Submit button
if st.button("Submit"):
    score = 0
    if q1 == "猫":
        score += 1
    if q2 == "ありがとう":
        score += 1
    st.success(f"You scored {score}/2")

