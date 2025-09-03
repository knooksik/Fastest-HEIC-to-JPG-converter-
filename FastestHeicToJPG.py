import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pillow_heif
from PIL import Image
import os

root = tk.Tk()
root.title("FastestHeicToJpg")
root.configure(bg="#232946")

frm = ttk.Frame(root, padding=20)
frm.grid()
frm.configure(style="Custom.TFrame")

selected_files = []
selected_folder = ""

def select_files_or_folder():
    global selected_files, selected_folder
    file_paths = filedialog.askopenfilenames(title="Select Files", filetypes=[("HEIC files", "*.heic")])
    if file_paths:
        selected_files = list(file_paths)
        selected_folder = ""
        log_text.insert(tk.END, f"Selected files:\n{selected_files}\n")
        print(f"Selected files: {selected_files}")
    else:
        folder_path = filedialog.askdirectory(title="Select Folder")
        if folder_path:
            selected_folder = folder_path
            selected_files = []
            log_text.insert(tk.END, f"Selected folder:\n{selected_folder}\n")
            print(f"Selected folder: {selected_folder}")
        else:
            log_text.insert(tk.END, "No selection made.\n")
            print("No selection made.")

def convert_heic_to_jpg():
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        log_text.insert(tk.END, "No output folder selected.\n")
        print("No output folder selected.")
        return

    print(f"Converting... Files: {selected_files}, Folder: {selected_folder}, Output: {output_folder}")
    if selected_files:
        for file_path in selected_files:
            try:
                heif_file = pillow_heif.read_heif(file_path)
                image = Image.frombytes(
                    heif_file.mode, heif_file.size, heif_file.data, "raw"
                )
                base_name = os.path.splitext(os.path.basename(file_path))[0]
                jpg_path = os.path.join(output_folder, base_name + ".jpg")
                image.save(jpg_path, "JPEG")
                log_text.insert(tk.END, f"Converted: {jpg_path}\n")
                print(f"Converted: {jpg_path}")
            except Exception as e:
                log_text.insert(tk.END, f"Error converting {file_path}: {e}\n")
                print(f"Error converting {file_path}: {e}")
    elif selected_folder:
        for filename in os.listdir(selected_folder):
            if filename.lower().endswith(".heic"):
                file_path = os.path.join(selected_folder, filename)
                try:
                    heif_file = pillow_heif.read_heif(file_path)
                    image = Image.frombytes(
                        heif_file.mode, heif_file.size, heif_file.data, "raw"
                    )
                    base_name = os.path.splitext(filename)[0]
                    jpg_path = os.path.join(output_folder, base_name + ".jpg")
                    image.save(jpg_path, "JPEG")
                    log_text.insert(tk.END, f"Converted: {jpg_path}\n")
                    print(f"Converted: {jpg_path}")
                except Exception as e:
                    log_text.insert(tk.END, f"Error converting {file_path}: {e}\n")
                    print(f"Error converting {file_path}: {e}")
    else:
        log_text.insert(tk.END, "No files or folder selected.\n")
        print("No files or folder selected.")

# Custom style for buttons and frame
style = ttk.Style()
style.theme_use("clam")
style.configure("Custom.TFrame", background="#232946")
style.configure("Custom.TButton", font=("Helvetica", 12, "bold"), foreground="#232946", background="#eebbc3", borderwidth=2, focusthickness=3, focuscolor='none')
style.map("Custom.TButton",
          foreground=[('pressed', '#232946'), ('active', '#232946')],
          background=[('pressed', '#eebbc3'), ('active', '#f6caca')])

ttk.Label(frm, text="FASTESTHEICTOJPG", font=("Arial Rounded MT Bold", 20, "bold"), background="#232946", foreground="#eebbc3").grid(column=2, row=0, pady=10)
ttk.Button(frm, text="Quit", command=root.destroy, style="Custom.TButton").grid(column=1, row=1, padx=10)
ttk.Button(frm, text="Convert", command=convert_heic_to_jpg, style="Custom.TButton").grid(column=3, row=1, padx=10)
ttk.Button(frm, text="Select Files or Folders", command=select_files_or_folder, style="Custom.TButton").grid(column=2, row=1, padx=10)

log_text = tk.Text(frm, width=50, height=10, font=("Consolas", 12), bg="#121629", fg="#eebbc3", insertbackground="#eebbc3", borderwidth=3, relief="ridge")
log_text.grid(column=1, row=3, columnspan=3, pady=20)

root.mainloop()