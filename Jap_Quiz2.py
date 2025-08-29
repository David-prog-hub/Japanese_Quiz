#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# In[1]:


get_ipython().system('python -m nbconvert --to script Jap_Quiz.ipynb')


# In[1]:


python -m tkinter


# In[2]:


self.score = 0,


# In[3]:


class Japanese_cons_k_QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana sound Quiz")
        self.score = 0   # ✅ FIXED (no comma, integer not tuple)
        self.current_question = 0


# In[4]:


root = tk.Tk()
app = Japanese_cons_k_QuizApp(root)
root.mainloop()


# In[5]:


import tkinter as tk
from tkinter import messagebox, ttk


# In[ ]:


root = tk.Tk()
app = Japanese_cons_k_QuizApp(root)
root.mainloop()

