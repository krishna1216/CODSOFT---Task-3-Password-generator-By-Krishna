import tkinter as tk
import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    generated_password.set(password)
root = tk.Tk()
root.title("Password Generator")
def generate():
    try:
        password_length = int(entry.get())
        if password_length <= 0:
            generated_password.set("Password length should be greater than 0")
            return
        generate_password(password_length)

    except ValueError:
        generated_password.set("Please enter a valid integer for password length")
length_label = tk.Label(root, text="Enter password length:")
length_label.pack(pady=10)

entry = tk.Entry(root, width=20)
entry.pack(pady=10)
generate_button = tk.Button(root, text="Generate Password", command=generate)
generate_button.pack()
generated_password = tk.StringVar()
password_label = tk.Label(root, textvariable=generated_password, wraplength=300, justify='left', padx=20, pady=10)
password_label.pack()
root.mainloop()
