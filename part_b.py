import sqlite3

def calculate_real_size(microscope_size, magnification):
    return microscope_size / magnification

def save_to_db(username, microscope_size, magnification, actual_size):
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

# Inputs
username = input("Enter username: ")
microscope_size = float(input("Enter microscope size (mm): "))
magnification = float(input("Enter magnification: "))

actual_size = calculate_real_size(microscope_size, magnification)
print(f"Real-life size: {actual_size:.2f} mm")

save_to_db(username, microscope_size, magnification, actual_size)
