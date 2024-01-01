import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string
import pyperclip  # Clipboard integration

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_var = tk.IntVar(value=12)
        self.complexity_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)

        self.create_widgets()

    def create_widgets(self):
        # Length Label and Entry
        length_label = ttk.Label(self.root, text="Password Length:")
        length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        length_entry = ttk.Entry(self.root, textvariable=self.length_var)
        length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Complexity Checkbox
        complexity_checkbox = ttk.Checkbutton(
            self.root, text="Include Uppercase Letters", variable=self.complexity_var
        )
        complexity_checkbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Symbols Checkbox
        symbols_checkbox = ttk.Checkbutton(
            self.root, text="Include Symbols", variable=self.symbols_var
        )
        symbols_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Digits Checkbox
        digits_checkbox = ttk.Checkbutton(
            self.root, text="Include Digits", variable=self.digits_var
        )
        digits_checkbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Generate Button
        generate_button = ttk.Button(
            self.root, text="Generate Password", command=self.generate_password
        )
        generate_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Copy to Clipboard Button
        copy_button = ttk.Button(
            self.root, text="Copy to Clipboard", command=self.copy_to_clipboard
        )
        copy_button.grid(row=5, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = self.length_var.get()
        complexity = self.complexity_var.get()
        symbols = self.symbols_var.get()
        digits = self.digits_var.get()

        chars = string.ascii_letters if complexity else string.ascii_lowercase
        if symbols:
            chars += string.punctuation
        if digits:
            chars += string.digits

        if not chars:
            messagebox.showerror("Error", "Please select at least one character set.")
            return

        password = "".join(random.choice(chars) for _ in range(length))
        self.show_generated_password(password)

    def show_generated_password(self, password):
        messagebox.showinfo("Generated Password", f"Your password is:\n{password}")

    def copy_to_clipboard(self):
        password = self.generate_password()
        pyperclip.copy(password)
        messagebox.showinfo("Copied to Clipboard", "Password copied to clipboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
