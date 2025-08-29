#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
# Display the coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)


# In[ ]:




