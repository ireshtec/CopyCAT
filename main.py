import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import shutil
import os

# -----------------------
# Functions
# -----------------------

def timestamp():
    now = datetime.now()
    return now.strftime("%Y%m%d%H%M")

def get_mounted_drives():
    drives = []
    media_path = "/media/iresh"
    if os.path.exists(media_path):
        for item in os.listdir(media_path):
            full_path = os.path.join(media_path, item)
            if os.path.ismount(full_path):
                drives.append(full_path)
    return drives

def copy_with_progress(src, dest):
    file_list = []
    for root_dir, _, files in os.walk(src):
        for file in files:
            file_list.append(os.path.join(root_dir, file))

    total_files = len(file_list)
    if total_files == 0:
        messagebox.showinfo("Info", "No files to copy!")
        return

    time_str = timestamp()
    global last_copy_folder
    last_copy_folder = os.path.join(
        dest, f"CopyCAT_{os.path.basename(src)}_{time_str}"
    )

    os.makedirs(last_copy_folder, exist_ok=True)

    for idx, file_path in enumerate(file_list, start=1):
        rel_path = os.path.relpath(file_path, src)
        dest_path = os.path.join(last_copy_folder, rel_path)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

        try:
            shutil.copy2(file_path, dest_path)
        except PermissionError:
            continue

        progress_var.set(int(idx / total_files * 100))
        currentFile_path.set(f"Copying: {rel_path}")
        window.update_idletasks()

    progress_var.set(100)
    currentFile_path.set("Copy completed ✔")
    messagebox.showinfo("Success", f"Copied {total_files} files")

def start_copy():
    src = source_var.get()
    dst = dest_var.get()
    if not src or not dst:
        messagebox.showwarning("Error", "Select both source and destination drives!")
        return
    copy_with_progress(src, dst)

# -----------------------
# VERIFY FUNCTION
# -----------------------

def verify_copy():
    get_mounted_drives()
    if not source_var.get() or not last_copy_folder:
        messagebox.showwarning("Error", "Nothing to verify yet!")
        return

    src = source_var.get()

    for root, _, files in os.walk(src):
        for f in files:
            src_path = os.path.join(root, f)
            rel = os.path.relpath(src_path, src)
            dst_path = os.path.join(last_copy_folder, rel)

            if not os.path.exists(dst_path):
                messagebox.showerror("Verify Failed", f"Missing file:\n{rel}")
                return

            if os.path.getsize(src_path) != os.path.getsize(dst_path):
                messagebox.showerror("Verify Failed", f"Size mismatch:\n{rel}")
                return

    messagebox.showinfo("Verify", "All files verified successfully ✅")

# -----------------------
# GUI
# -----------------------

window = tk.Tk()
window.title("USB Drive Copier")
window.geometry("480x360")
window.attributes("-topmost", True)

last_copy_folder = None

drives = get_mounted_drives()

tk.Label(window, text="Select Source Drive:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
source_var = tk.StringVar()
ttk.Combobox(window, values=drives, textvariable=source_var, state="readonly") \
    .grid(row=0, column=1, padx=10, pady=10, sticky="w")

tk.Label(window, text="Select Destination Drive:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
dest_var = tk.StringVar()
ttk.Combobox(window, values=drives, textvariable=dest_var, state="readonly") \
    .grid(row=1, column=1, padx=10, pady=10, sticky="w")

# -----------------------
# BUTTON ROW (INLINE)
# -----------------------

copy_btn = tk.Button(window, text="Copy", command=start_copy, bg="green", fg="white", width=10)
copy_btn.grid(row=2, column=0, pady=15)

verify_btn = tk.Button(window, text="Verify", command=verify_copy, bg="#007acc", fg="white", width=10)
verify_btn.grid(row=2, column=1, pady=15)

close_btn = tk.Button(window, text="Close", command=window.destroy, bg="red", fg="white", width=10)
close_btn.grid(row=2, column=2, pady=15)

# -----------------------
# PROGRESS BAR
# -----------------------

progress_var = tk.IntVar()
ttk.Progressbar(window, orient="horizontal", length=420,
                mode="determinate", variable=progress_var) \
    .grid(row=3, column=0, columnspan=3, padx=20, pady=10)

# -----------------------
# STATUS LABEL
# -----------------------

currentFile_path = tk.StringVar()
tk.Label(window, textvariable=currentFile_path, width=60, anchor="w") \
    .grid(row=4, column=0, columnspan=3, pady=10)

# -----------------------
# FOOTER
# -----------------------

tk.Label(window, text="@Iresh", fg="gray") \
    .grid(row=5, column=2, sticky="e", padx=10, pady=5)

window.mainloop()
