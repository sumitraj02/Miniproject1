       #   TEXT EDITOR BY SUMIT KUMAR MINI PROJECT OF PYTHON
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import webbrowser  
import os  # Added import for os module

HELP_LINK = "https://github.com/Engsumit"

def open_file(window, text_edit, filename_label):
    filepath = askopenfilename(filetypes=[("Text Files", ".txt")])
    
    if not filepath:
        return 
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    
    filename = os.path.basename(filepath)  # Extract only the filename
    window.title(f"Open File: {filename}")
    filename_label.config(text=f"File: {filename}")

def save_file(window, text_edit, filename_label):
    filepath = asksaveasfilename(filetypes=[("Text Files", ".txt")])

    if not filepath:
        return
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    
    filename = os.path.basename(filepath)  # Extract only the filename
    window.title(f"Open File: {filename}")
    filename_label.config(text=f"File: {filename}")

def open_help():
    webbrowser.open(HELP_LINK)

def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(
        frame, text="Save", command=lambda: save_file(window, text_edit, filename_label))
    open_button = tk.Button(
        frame, text="Open", command=lambda: open_file(window, text_edit, filename_label))
    help_button = tk.Button(
        frame, text="Help", command=open_help) 

    filename_label = tk.Label(frame, text="File: None")
    filename_label.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, sticky="ew")
    help_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")  
    
    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", lambda x: save_file(window, text_edit, filename_label))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit, filename_label))
    window.mainloop()

main()
