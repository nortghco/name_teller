import customtkinter as ctk

# default appearance and theme
ctk.set_appearance_mode("light")

root = ctk.CTk()
root.title("Name Teller")
root.geometry("500x300")

# Submit Function
def submit():
    label.configure(root, text=f"Welcome, {entry.get()}")

# Main Label
label = ctk.CTkLabel(root, text="", font=("Arial", 15), text_color="black")
label.pack(pady=20, padx=20)

# Main Entry
entry = ctk.CTkEntry(root, placeholder_text="Enter your name", border_color="black", corner_radius=10, height=50, width=150)
entry.pack(pady=20, padx=20)

# Main Button
button = ctk.CTkButton(root, text="Submit", height=50, width=150, fg_color="white", hover_color="#e6e6e6", corner_radius=10, border_color="black", border_width=2, command=submit)
button.pack(pady=20, padx=20)

# Mainloop The Window
root.mainloop()
