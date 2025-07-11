import tkinter as tk
from tkinter import filedialog
import subprocess
import os  # Import the os module



# Create a function to update the progress
def update_progress(progress_text):
    progress_label.config(text=progress_text)
    window.update()  # Update the window to show the changes immediately



scan_count = 1  # Initialize the scan count


def scan_image():
    format_value = format_entry.get()
    resolution_value = resolution_entry.get()
    mode_value = mode_entry.get()
    
    global scan_count  # Allow modification of the global scan_count variable
    output_path = os.path.join(
        os.path.expanduser("~/Desktop"), f"scan_{scan_count}.tiff"
    )
    scan_count += 1  # Increment the scan count for the next scan



    command = ["/opt/homebrew/bin/scanimage", "--progress", f"--format={format_value}", f"--resolution={resolution_value}", f"--mode={mode_value}"]
    with open(output_path, "wb") as output_file:
        process = subprocess.Popen(command, stdout=output_file, stderr=subprocess.PIPE, universal_newlines=True)
        for line in process.stderr:
            if "Progress" in line:
                update_progress(line.strip())  # Update progress when "Progress" is found in the output
        process.wait()

    print("Scanning complete.")
    update_progress("Scanning complete.")  # Update progress to indicate completion

    

def set_default_values():
    format_entry.delete(0, tk.END)
    format_entry.insert(tk.END, "tiff")
    resolution_entry.delete(0, tk.END)
    resolution_entry.insert(tk.END, "300")
    mode_entry.delete(0, tk.END)
    mode_entry.insert(tk.END, "color")
    output_entry.delete(0, tk.END)
    output_entry.insert(tk.END, "~/Desktop/scan.tiff")



# Create the main window
window = tk.Tk()
window.title("Scan Image")
window.configure(padx=32, pady=32, bg="#333333")
window.resizable(False, False)


# Format
format_label = tk.Label(window, text="Format:",  anchor="w")
format_label.pack(anchor="w", padx=0, pady=(0,5))  # Left-align and add padding
format_entry = tk.Entry(window, relief="flat")
format_entry.pack(anchor="w", padx=0, pady=(0, 15))  # Left-align and add padding
format_entry.insert(tk.END, "tiff")

# Resolution
resolution_label = tk.Label(window, text="Resolution:", anchor="w")
resolution_label.pack(anchor="w", padx=0, pady=(0,5))
resolution_entry = tk.Entry(window, relief="flat")
resolution_entry.pack(anchor="w", padx=0, pady=(0, 15))
resolution_entry.insert(tk.END, "300")


# Mode
mode_label = tk.Label(window, text="Mode:")
mode_label.pack(anchor="w", padx=0, pady=(0,5))
mode_entry = tk.Entry(window, relief="flat")
mode_entry.pack(anchor="w", padx=0, pady=(0, 15))
mode_entry.insert(tk.END, "color")

# Output Location
output_label = tk.Label(window, text="Output Location:")
output_label.pack(anchor="w", padx=0, pady=(0,5))
output_entry = tk.Entry(window, relief="flat")
output_entry.pack(anchor="w", padx=0, pady=(0, 15))
output_entry.insert(tk.END, "~/Desktop/scan.tiff")


# Scan Button
scan_button = tk.Button(window, text="Scan", command=scan_image)
scan_button.pack()
scan_button.pack(anchor="w", padx=0, pady=(0,5))  # Left-align and add padding

# Default Values Button
default_values_button = tk.Button(window, text="Default Values", command=set_default_values)
default_values_button.pack(anchor="w", padx=0, pady=(0,10))

# Create a label for progress
progress_label = tk.Label(window, text="", )
progress_label.pack(anchor="w", padx=0, pady=(0, 10))  # Add padding at the bottom


# Run the main event loop
window.mainloop()
