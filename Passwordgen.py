import tkinter as tk
import random
import string

# Function to generate password
def generate_password():
    name = name_entry.get()

    if not name:
        result_label.config(text="Please enter your name!", fg="red")
        return

    # Character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    # Combine all
    all_chars = letters + digits + symbols

    # Ensure password contains at least one of each
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Add characters based on user's name
    name_part = ''.join(random.sample(name, min(len(name), 3)))
    password.extend(name_part)

    # Fill remaining length
    length = 12
    while len(password) < length:
        password.append(random.choice(all_chars))

    # Shuffle password
    random.shuffle(password)

    final_password = ''.join(password)

    result_label.config(text=f"Generated Password:\n{final_password}", fg="green")


# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#2c3e50")

# Title
title_label = tk.Label(root, text="Strong Password Generator",
                       font=("Arial", 16, "bold"),
                       bg="#2c3e50", fg="white")
title_label.pack(pady=10)

# Name input
name_label = tk.Label(root, text="Enter your name:",
                      bg="#2c3e50", fg="white")
name_label.pack()

name_entry = tk.Entry(root, width=25)
name_entry.pack(pady=5)

# Generate button
generate_btn = tk.Button(root, text="Generate Password",
                         command=generate_password,
                         bg="#27ae60", fg="white",
                         font=("Arial", 10, "bold"))
generate_btn.pack(pady=15)

# Result display
result_label = tk.Label(root, text="",
                        bg="#2c3e50", fg="white",
                        font=("Arial", 12))
result_label.pack(pady=10)

# Run app
root.mainloop()