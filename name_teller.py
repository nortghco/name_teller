import customtkinter as ctk
import tkinter as tk

# default appearance and theme
ctk.set_appearance_mode("light")

root = ctk.CTk()
root.title("Name Teller")
root.geometry("500x300")

# Functions
def submit():
    label.configure(root, text=f"Welcome, {entry.get()}")

def clear():
    entry.delete(0, tk.END)

# Main Label
label = ctk.CTkLabel(root, text="", font=("Arial", 15), text_color="black")
label.pack(pady=20, padx=20)

# Main Entry
entry = ctk.CTkEntry(root, placeholder_text="Enter your name", border_color="black", corner_radius=10, height=50, width=150)
entry.pack(pady=20, padx=20)

# Main Button
button = ctk.CTkButton(root, text="Submit", height=35, width=150, fg_color="white", hover_color="#e6e6e6", corner_radius=10, border_color="black", border_width=2, text_color="black", command=submit)
button.pack(pady=6)

# Main Clear Button
cbutton = ctk.CTkButton(root, text="Clear", height=35, width=150, fg_color="white", hover_color="#e6e6e6", corner_radius=10, border_color="black", border_width=2, text_color="black", command=clear)
cbutton.pack(pady=6)

# Mainloop The Window
root.mainloop()
