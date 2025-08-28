#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox, ttk
import uuid

class Japanese_cons_k_QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana sound Quiz")
        self.score = 0
        self.current_question = 0
        
        # Quiz questions
        self.questions = [
            ("What is 'か' in English?", "ka"),
            ("What is 'き' in English?", "ki"),
            ("What is 'く' in English?", "ku"),
            ("What is 'け' in English?", "ke"),
            ("What is 'こ' in English?", "ko")
        ]
        
        # Set window background and size
        self.root.configure(bg="#f0f4f8")
        self.root.geometry("500x400")
        
        # Create main frame with padding and background
        self.main_frame = tk.Frame(root, bg="#f0f4f8", padx=20, pady=20)
        self.main_frame.pack(expand=True, fill="both")
        
        # Title label
        self.title_label = tk.Label(
            self.main_frame,
            text="German Vocabulary Quiz",
            font=("Helvetica", 20, "bold"),
            bg="#f0f4f8",
            fg="#2c3e50"
        )
        self.title_label.pack(pady=10)
        
        # Question label
        self.label = tk.Label(
            self.main_frame,
            text="",
            font=("Arial", 14),
            bg="#f0f4f8",
            fg="#34495e",
            wraplength=400
        )
        self.label.pack(pady=20)
        
        # Answer entry with styling
        self.answer_entry = ttk.Entry(
            self.main_frame,
            font=("Arial", 12),
            width=30,
            style="Custom.TEntry"
        )
        self.answer_entry.pack(pady=10)
        
        # Submit button with styling
        self.submit_button = ttk.Button(
            self.main_frame,
            text="Submit",
            command=self.check_answer,
            style="Custom.TButton"
        )
        self.submit_button.pack(pady=10)
        
        # Score label
        self.score_label = tk.Label(
            self.main_frame,
            text=f"Score: {self.score}/5",
            font=("Arial", 12, "italic"),
            bg="#f0f4f8",
            fg="#27ae60"
        )
        self.score_label.pack(pady=10)
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure(
            "Custom.TButton",
            font=("Arial", 12, "bold"),
            padding=10,
            background="#3498db",
            foreground="#ffffff"
        )
        self.style.map(
            "Custom.TButton",
            background=[("active", "#2980b9")]
        )
        self.style.configure(
            "Custom.TEntry",
            padding=5,
            font=("Arial", 12)
        )
        
        # Start the quiz
        self.show_question()
        
    def show_question(self):
        if self.current_question < len(self.questions):
            question, _ = self.questions[self.current_question]
            self.label.config(text=f"Question {self.current_question + 1}: {question}")
            self.answer_entry.delete(0, tk.END)  # Clear the input field
        else:
            self.end_quiz()
    
    def check_answer(self):
        if self.current_question < len(self.questions):
            _, correct_answer = self.questions[self.current_question]
            user_answer = self.answer_entry.get().strip().lower()
            
            if user_answer == correct_answer:
                self.score += 1
                messagebox.showinfo("Result", f"Correct! Current score: {self.score}", parent=self.root)
            else:
                messagebox.showinfo(
                    "Result",
                    f"Incorrect. The correct answer is '{correct_answer}'. Current score: {self.score}",
                    parent=self.root
                )
            
            self.score_label.config(text=f"Score: {self.score}/5")
            self.current_question += 1
            self.show_question()
    
    def end_quiz(self):
        self.label.config(text=f"Quiz completed! Your final score is {self.score}/5")
        self.answer_entry.pack_forget()  # Hide input field
        #self.submit_button.pack_forget()  # Hide submit button
        if self.score == 5:
            messagebox.showinfo("Result", "Perfect! You got all answers correct!", parent=self.root)

# Create and run the application
root = tk.Tk()
app = Japanese_cons_k_QuizApp(root)
root.mainloop()


# In[3]:


import streamlit as st

from tkinter import messagebox, ttk
import uuid

class Japanese_spelling_k_QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana sound Quiz")
        self.score = 0
        self.current_question = 0
        
        # Quiz questions
        self.questions = [
            ("What is 'かき' in English?", "kaki"),
            ("What is 'きこ' in English?", "kiko"),
            ("What is 'くこ' in English?", "kuko"),
            ("What is 'けか' in English?", "keka"),
            ("What is 'ここ' in English?", "koko")
        ]
        
        # Set window background and size
        self.root.configure(bg="#f0f4f8")
        self.root.geometry("500x400")
        
        # Create main frame with padding and background
        self.main_frame = tk.Frame(root, bg="#f0f4f8", padx=20, pady=20)
        self.main_frame.pack(expand=True, fill="both")
        
        # Title label
        self.title_label = tk.Label(
            self.main_frame,
            text="German Vocabulary Quiz",
            font=("Helvetica", 20, "bold"),
            bg="#f0f4f8",
            fg="#2c3e50"
        )
        self.title_label.pack(pady=10)
        
        # Question label
        self.label = tk.Label(
            self.main_frame,
            text="",
            font=("Arial", 14),
            bg="#f0f4f8",
            fg="#34495e",
            wraplength=400
        )
        self.label.pack(pady=20)
        
        # Answer entry with styling
        self.answer_entry = ttk.Entry(
            self.main_frame,
            font=("Arial", 12),
            width=30,
            style="Custom.TEntry"
        )
        self.answer_entry.pack(pady=10)
        
        # Submit button with styling
        self.submit_button = ttk.Button(
            self.main_frame,
            text="Submit",
            command=self.check_answer,
            style="Custom.TButton"
        )
        self.submit_button.pack(pady=10)
        
        # Score label
        self.score_label = tk.Label(
            self.main_frame,
            text=f"Score: {self.score}/5",
            font=("Arial", 12, "italic"),
            bg="#f0f4f8",
            fg="#27ae60"
        )
        self.score_label.pack(pady=10)
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure(
            "Custom.TButton",
            font=("Arial", 12, "bold"),
            padding=10,
            background="#3498db",
            foreground="#ffffff"
        )
        self.style.map(
            "Custom.TButton",
            background=[("active", "#2980b9")]
        )
        self.style.configure(
            "Custom.TEntry",
            padding=5,
            font=("Arial", 12)
        )
        
        # Start the quiz
        self.show_question()
        
    def show_question(self):
        if self.current_question < len(self.questions):
            question, _ = self.questions[self.current_question]
            self.label.config(text=f"Question {self.current_question + 1}: {question}")
            self.answer_entry.delete(0, tk.END)  # Clear the input field
        else:
            self.end_quiz()
    
    def check_answer(self):
        if self.current_question < len(self.questions):
            _, correct_answer = self.questions[self.current_question]
            user_answer = self.answer_entry.get().strip().lower()
            
            if user_answer == correct_answer:
                self.score += 1
                messagebox.showinfo("Result", f"Correct! Current score: {self.score}", parent=self.root)
            else:
                messagebox.showinfo(
                    "Result",
                    f"Incorrect. The correct answer is '{correct_answer}'. Current score: {self.score}",
                    parent=self.root
                )
            
            self.score_label.config(text=f"Score: {self.score}/5")
            self.current_question += 1
            self.show_question()
    
    def end_quiz(self):
        self.label.config(text=f"Quiz completed! Your final score is {self.score}/5")
        self.answer_entry.pack_forget()  # Hide input field
        #self.submit_button.pack_forget()  # Hide submit button
        if self.score == 5:
            messagebox.showinfo("Result", "Perfect! You got all answers correct!", parent=self.root)

# Create and run the application
root = tk.Tk()
app = Japanese_spelling_k_QuizApp(root)
root.mainloop()


# In[ ]:


＃さ、し、す、せ、そ
import tkinter as tk
from tkinter import messagebox, ttk
import uuid

class Japanese_cons_k_QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana sound Quiz")
        self.score = 0
        self.current_question = 0
        
        # Quiz questions
        self.questions = [
            ("What is 'さ' in English?", "sa"),
            ("What is 'し' in English?", "shi"),
            ("What is 'す' in English?", "su"),
            ("What is 'せ' in English?", "se"),
            ("What is 'そ' in English?", "so")
        ]
        
        # Set window background and size
        self.root.configure(bg="#f0f4f8")
        self.root.geometry("500x400")
        
        # Create main frame with padding and background
        self.main_frame = tk.Frame(root, bg="#f0f4f8", padx=20, pady=20)
        self.main_frame.pack(expand=True, fill="both")
        
        # Title label
        self.title_label = tk.Label(
            self.main_frame,
            text="German Vocabulary Quiz",
            font=("Helvetica", 20, "bold"),
            bg="#f0f4f8",
            fg="#2c3e50"
        )
        self.title_label.pack(pady=10)
        
        # Question label
        self.label = tk.Label(
            self.main_frame,
            text="",
            font=("Arial", 14),
            bg="#f0f4f8",
            fg="#34495e",
            wraplength=400
        )
        self.label.pack(pady=20)
        
        # Answer entry with styling
        self.answer_entry = ttk.Entry(
            self.main_frame,
            font=("Arial", 12),
            width=30,
            style="Custom.TEntry"
        )
        self.answer_entry.pack(pady=10)
        
        # Submit button with styling
        self.submit_button = ttk.Button(
            self.main_frame,
            text="Submit",
            command=self.check_answer,
            style="Custom.TButton"
        )
        self.submit_button.pack(pady=10)
        
        # Score label
        self.score_label = tk.Label(
            self.main_frame,
            text=f"Score: {self.score}/5",
            font=("Arial", 12, "italic"),
            bg="#f0f4f8",
            fg="#27ae60"
        )
        self.score_label.pack(pady=10)
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure(
            "Custom.TButton",
            font=("Arial", 12, "bold"),
            padding=10,
            background="#3498db",
            foreground="#ffffff"
        )
        self.style.map(
            "Custom.TButton",
            background=[("active", "#2980b9")]
        )
        self.style.configure(
            "Custom.TEntry",
            padding=5,
            font=("Arial", 12)
        )
        
        # Start the quiz
        self.show_question()
        
    def show_question(self):
        if self.current_question < len(self.questions):
            question, _ = self.questions[self.current_question]
            self.label.config(text=f"Question {self.current_question + 1}: {question}")
            self.answer_entry.delete(0, tk.END)  # Clear the input field
        else:
            self.end_quiz()
    
    def check_answer(self):
        if self.current_question < len(self.questions):
            _, correct_answer = self.questions[self.current_question]
            user_answer = self.answer_entry.get().strip().lower()
            
            if user_answer == correct_answer:
                self.score += 1
                messagebox.showinfo("Result", f"Correct! Current score: {self.score}", parent=self.root)
            else:
                messagebox.showinfo(
                    "Result",
                    f"Incorrect. The correct answer is '{correct_answer}'. Current score: {self.score}",
                    parent=self.root
                )
            
            self.score_label.config(text=f"Score: {self.score}/5")
            self.current_question += 1
            self.show_question()
    
    def end_quiz(self):
        self.label.config(text=f"Quiz completed! Your final score is {self.score}/5")
        self.answer_entry.pack_forget()  # Hide input field
        #self.submit_button.pack_forget()  # Hide submit button
        if self.score == 5:
            messagebox.showinfo("Result", "Perfect! You got all answers correct!", parent=self.root)

# Create and run the application
root = tk.Tk()
app = Japanese_cons_k_QuizApp(root)
root.mainloop()


# In[ ]:


＃さ、し、す、セ、そ
import tkinter as tk
from tkinter import messagebox, ttk
import uuid

class Japanese_cons_k_QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana sound Quiz")
        self.score = 0
        self.current_question = 0
        
        # Quiz questions
        self.questions = [
            ("What is 'さ' in English?", "ka"),
            ("What is 'し' in English?", "ki"),
            ("What is 'す' in English?", "ku"),
            ("What is 'せ' in English?", "ke"),
            ("What is 'そ' in English?", "ko")
        ]


# In[ ]:


＃た、ち、つ、て、と
import tkinter as tk
from tkinter import messagebox, ttk
import uuid

class Japanese_cons_k_QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana sound Quiz")
        self.score = 0
        self.current_question = 0
        
        # Quiz questions
        self.questions = [
            ("What is 'た' in English?", "ta"),
            ("What is 'ち' in English?", "chi"),
            ("What is 'つ' in English?", "tsu"),
            ("What is 'て' in English?", "te"),
            ("What is 'と' in English?", "to")
import tkinter as tk
from tkinter import messagebox, ttk
import uuid

class Japanese_cons_k_QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana sound Quiz")
        self.score = 0
        self.current_question = 0
        
        # Quiz questions
        self.questions = [
            ("What is 'さ' in English?", "ka"),
            ("What is 'し' in English?", "ki"),
            ("What is 'つ' in English?", "ku"),
            ("What is 'せ' in English?", "ke"),
            ("What is 'そ' in English?", "ko")
import tkinter as tk
from tkinter import messagebox, ttk
import uuid

class Japanese_cons_k_QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana sound Quiz")
        self.score = 0
        self.current_question = 0
        
        # Quiz questions
        self.questions = [
            ("What is 'さ' in English?", "ka"),
            ("What is 'し' in English?", "ki"),
            ("What is 'つ' in English?", "ku"),
            ("What is 'せ' in English?", "ke"),
            ("What is 'そ' in English?", "ko")


# In[ ]:


＃な、に、ぬ、ね、の
import tkinter as tk
from tkinter import messagebox, ttk
import uuid

class Japanese_cons_k_QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana sound Quiz")
        self.score = 0
        self.current_question = 0
        
        # Quiz questions
        self.questions = [
            ("What is 'な' in English?", "na"),
            ("What is 'に' in English?", "ni"),
            ("What is 'ぬ' in English?", "nu"),
            ("What is 'ね' in English?", "ne"),
            ("What is 'の' in English?", "no")


# In[ ]:


＃は、ひ、ふ、へ、ほ
import tkinter as tk
from tkinter import messagebox, ttk
import uuid

class Japanese_cons_k_QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana sound Quiz")
        self.score = 0
        self.current_question = 0
        
        # Quiz questions
        self.questions = [
            ("What is 'は' in English?", "ha"),
            ("What is 'ひ' in English?", "hi"),
            ("What is 'ふ' in English?", "fu"),
            ("What is 'へ' in English?", "he"),
            ("What is 'ほ' in English?", "ho")


# In[ ]:


＃ま、み、む、め、も
import tkinter as tk
from tkinter import messagebox, ttk
import uuid

class Japanese_cons_k_QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana sound Quiz")
        self.score = 0
        self.current_question = 0
        
        # Quiz questions
        self.questions = [
            ("What is 'ま' in English?", "ma"),
            ("What is 'み' in English?", "mi"),
            ("What is 'む' in English?", "mu"),
            ("What is 'め' in English?", "me"),
            ("What is 'も' in English?", "mo")


# In[ ]:


＃や、い、ゆ、え、よ
import tkinter as tk
from tkinter import messagebox, ttk
import uuid

class Japanese_cons_k_QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana sound Quiz")
        self.score = 0
        self.current_question = 0
        
        # Quiz questions
        self.questions = [
            ("What is 'は' in English?", "ya"),
            ("What is 'ひ' in English?", "i"),
            ("What is 'ふ' in English?", "yu"),
            ("What is 'へ' in English?", "e"),
            ("What is 'ほ' in English?", "yo")


# In[ ]:


＃ら、り、る、れ、ろ
import tkinter as tk
from tkinter import messagebox, ttk
import uuid

class Japanese_cons_k_QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana sound Quiz")
        self.score = 0
        self.current_question = 0
        
        # Quiz questions
        self.questions = [
            ("What is 'ら' in English?", "ra"),
            ("What is 'り' in English?", "ri"),
            ("What is 'る' in English?", "ru"),
            ("What is 'れ' in English?", "re"),
            ("What is 'ろ' in English?", "ro")


# In[ ]:


＃わ、を
import tkinter as tk
from tkinter import messagebox, ttk
import uuid

class Japanese_cons_k_QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana sound Quiz")
        self.score = 0
        self.current_question = 0
        
        # Quiz questions
        self.questions = [
            ("What is 'わ' in English?", "wa"),
            ("What is 'ひ' in English?", "ki"),
            ("What is 'ふ' in English?", "ku"),
            ("What is 'へ' in English?", "ke"),
            ("What is 'を' in English?", "o")


# In[ ]:


get_ipython().system('python -m nbconvert --to script Kana_cons_Quiz.ipynb')

