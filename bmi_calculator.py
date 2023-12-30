import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BMIApp:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")

        self.user_data = []
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry Widgets
        tk.Label(self.master, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.master, text="Height (cm):").grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.weight_entry = tk.Entry(self.master)
        self.height_entry = tk.Entry(self.master)

        self.weight_entry.grid(row=0, column=1, padx=10, pady=10)
        self.height_entry.grid(row=1, column=1, padx=10, pady=10)

        # Calculate BMI Button
        tk.Button(self.master, text="Calculate BMI", command=self.calculate_bmi).grid(row=2, column=0, columnspan=2, pady=10)

        # BMI Result Label
        self.result_label = tk.Label(self.master, text="BMI: ")
        self.result_label.grid(row=3, column=0, columnspan=2)

        # Save Data Button
        tk.Button(self.master, text="Save Data", command=self.save_data).grid(row=4, column=0, columnspan=2, pady=10)

        # Historical Data Combobox
        tk.Label(self.master, text="Select User:").grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.user_combobox = ttk.Combobox(self.master, values=["Select User"])
        self.user_combobox.grid(row=5, column=1, padx=10, pady=10)

        # View History Button
        tk.Button(self.master, text="View History", command=self.view_history).grid(row=6, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get()) / 100.0  # Convert height to meters
            bmi = weight / (height ** 2)

            self.result_label.config(text=f"BMI: {bmi:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

    def save_data(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get()) / 100.0  # Convert height to meters
            bmi = weight / (height ** 2)

            self.user_data.append({"Weight": weight, "Height": height, "BMI": bmi})
            self.user_combobox["values"] = [f"User {i+1}" for i in range(len(self.user_data))]
            self.user_combobox.current(len(self.user_data) - 1)

            messagebox.showinfo("Success", "Data saved successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

    def view_history(self):
        selected_user_index = self.user_combobox.current()
        if selected_user_index != -1:
            selected_user_data = self.user_data[selected_user_index]
            self.show_history_graph(selected_user_data)
        else:
            messagebox.showwarning("Warning", "Please select a user.")

    def show_history_graph(self, user_data):
        fig, ax = plt.subplots()
        ax.plot([f"Entry {i+1}" for i in range(len(user_data))], [entry["BMI"] for entry in user_data], marker='o')
        ax.set_xlabel("Entry")
        ax.set_ylabel("BMI")
        ax.set_title("BMI Trend Analysis")

        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=7, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()
