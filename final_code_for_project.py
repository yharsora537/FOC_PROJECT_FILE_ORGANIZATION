import os
import shutil
from tkinter import Tk, Button, Label, Entry, StringVar, OptionMenu

def organize_files():
    folder_path = folder_path_var.get()
    organize_by = organize_by_var.get()

    if not os.path.exists(folder_path):
        info_label.config(text="Invalid folder path.")
        return

    alphabet_folders = {}
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        alphabet_folders[char] = os.path.join(folder_path, char)
        if not os.path.exists(alphabet_folders[char]):
            os.makedirs(alphabet_folders[char])

    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            if organize_by == "Alphabetical":
                first_char = file_name[0].upper()
                if first_char in alphabet_folders:
                    shutil.move(os.path.join(folder_path, file_name), alphabet_folders[first_char])
            elif organize_by == "Date":
                modified_time = os.path.getmtime(os.path.join(folder_path, file_name))
                modified_date = time.strftime('%Y-%m-%d', time.localtime(modified_time))
                year = modified_date.split('-')[0]
                month = modified_date.split('-')[1]
                destination_folder = os.path.join(alphabet_folders[year], month)
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                shutil.move(os.path.join(folder_path, file_name), destination_folder)

    info_label.config(text="Files organized successfully.")

# GUI
root = Tk()
root.title("File Organizer")

folder_path_var = StringVar()
organize_by_var = StringVar()

Label(root, text="Folder Path:").grid(row=0, column=0)
Entry(root, textvariable=folder_path_var, width=50).grid(row=0, column=1)

Label(root, text="Organize By:").grid(row=1, column=0)
OptionMenu(root, organize_by_var, "Alphabetical", "Date").grid(row=1, column=1)

organize_button = Button(root, text="Organize Files", command=organize_files)
organize_button.grid(row=2, columnspan=2)

info_label = Label(root, text="")
info_label.grid(row=3, columnspan=2)

root.mainloop()
