import os
import tkinter as tk
from tkinter import filedialog, messagebox


def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)


def rename_files(preview=True):
    folder = folder_path.get()

    if not os.path.isdir(folder):
        messagebox.showerror("Error", "Invalid folder path!")
        return

    prefix = prefix_entry.get()
    suffix = suffix_entry.get()

    files = sorted(os.listdir(folder))
    count = 1
    output_text.delete(1.0, tk.END)

    for file in files:
        old_path = os.path.join(folder, file)

        if not os.path.isfile(old_path):
            continue

        if file.startswith('.'):
            continue

        name, ext = os.path.splitext(file)
        new_name = f"{prefix}{name}{suffix}_{count:03}{ext}"
        new_path = os.path.join(folder, new_name)

        if os.path.exists(new_path):
            output_text.insert(tk.END, f"⚠ Skipped: {new_name} (exists)\n")
            continue

        if preview:
            output_text.insert(tk.END, f"[PREVIEW] {file} → {new_name}\n")
        else:
            os.rename(old_path, new_path)
            output_text.insert(tk.END, f"Renamed: {file} → {new_name}\n")
            count += 1

    messagebox.showinfo("Done", "Operation completed!")


# GUI Setup
root = tk.Tk()
root.title("Bulk File Renamer Tool")
root.geometry("600x400")

folder_path = tk.StringVar()

# Folder selection
tk.Label(root, text="Select Folder:").pack()
tk.Entry(root, textvariable=folder_path, width=50).pack()
tk.Button(root, text="Browse", command=select_folder).pack(pady=5)

# Prefix & Suffix
tk.Label(root, text="Prefix:").pack()
prefix_entry = tk.Entry(root)
prefix_entry.pack()

tk.Label(root, text="Suffix:").pack()
suffix_entry = tk.Entry(root)
suffix_entry.pack()

# Buttons
tk.Button(root, text="Preview", command=lambda: rename_files(True)).pack(pady=5)
tk.Button(root, text="Rename Files", command=lambda: rename_files(False)).pack(pady=5)

# Output box
output_text = tk.Text(root, height=10)
output_text.pack(fill="both", expand=True)

root.mainloop()