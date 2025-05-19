def calculate_real_size(microscope_size, magnification):
    return microscope_size / magnification

# Sample input
microscope_size = float(input("Enter microscope size (mm): "))
magnification = float(input("Enter magnification: "))

actual_size = calculate_real_size(microscope_size, magnification)
print(f"Real-life size: {actual_size:.2f} mm")
