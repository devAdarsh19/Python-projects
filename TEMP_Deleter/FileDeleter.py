
import tkinter as tk
import tempfile
import os

def delete_files():
    for file_path in os.listdir(temp_folder):
        try:
            os.remove(os.path.join(temp_folder, file_path))
            print(f"Deleted: {file_path}")
        except OSError as e:
            print(f"Error deleting {file_path}: {e}")
            
root = tk.Tk()
root.title('TEMP Deleter')
root.configure(bg="grey")
temp_folder = tempfile.gettempdir()

folder_label = tk.Label(root, text=temp_folder)
folder_label.pack(pady=10, padx=10)
folder_label.configure(bg="grey")

delete_button = tk.Button(root, text="Delete", command=delete_files)
delete_button.pack(pady=10)

root.mainloop()