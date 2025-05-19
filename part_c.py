import tkinter as tk
import sqlite3

def calculate_and_save():
    username = username_entry.get()
    microscope_size = float(size_entry.get())
    magnification = float(mag_entry.get())
    actual_size = microscope_size / magnification

    result_label.config(text=f"Actual Size: {actual_size:.2f} mm")

    conn = sqlite3.connect("specimens.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS specimens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            microscope_size REAL,
            magnification REAL,
            actual_size REAL
        )
    ''')
    cursor.execute("INSERT INTO specimens (username, microscope_size, magnification, actual_size) VALUES (?, ?, ?, ?)",
                   (username, microscope_size, magnification, actual_size))
    conn.commit()
    conn.close()

# GUI setup
root = tk.Tk()
root.title("Microscope Calculator")

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Microscope Size (mm):").pack()
size_entry = tk.Entry(root)
size_entry.pack()

tk.Label(root, text="Magnification:").pack()
mag_entry = tk.Entry(root)
mag_entry.pack()

tk.Button(root, text="Calculate", command=calculate_and_save).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
