'''calling the required modules'''
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
from PIL import ImageTk, Image
import shutil
import os
import easygui


def open_window():
    '''open a file box window when we want to select a file'''
    read = easygui.fileopenbox()
    return read


def open_file():
    '''open a file'''
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File not found!")


def copy_file():
    '''copy a file'''
    source1 = open_window()
    destination1 = filedialog.askdirectory()
    shutil.copy(source1, destination1)
    mb.showinfo('confirmation', "File Copied!")


def delete_file():
    '''deleting a file'''
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)
    else:
        mb.showinfo('confirmation', "File Not Found!")


def rename_file():
    '''rename a file'''
    chosen_file = open_window()
    path1 = os.path.dirname(chosen_file)
    extension = os.path.splitext(chosen_file)[1]
    new_name = input("Enter the new name for the chosen file: ")
    path = os.path.join(path1, new_name + extension)
    print(path)
    os.rename(chosen_file, path)
    mb.showinfo('confirmation', "File Renamed!")


def move_file():
    '''moving a file'''
    source = open_window()
    destination = filedialog.askdirectory()
    if source == destination:
        mb.showinfo('confirmation', "Same source and destination!")
    else:
        shutil.move(source, destination)
        mb.showinfo('confirmation', "File Moved!")


def make_folder():
    '''function to remove a folder'''
    new_folder_path = filedialog.askdirectory()
    new_folder = input("Enter the name of the new folder: ")
    path = os.path.join(new_folder_path, new_folder)
    os.mkdir(path)
    mb.showinfo('confirmation', "Folder Created!")


def remove_folder():
    '''function to remove a folder'''
    del_folder = filedialog.askdirectory()
    os.rmdir(del_folder)
    mb.showinfo('confirmation', "Folder Deleted!")

def list_files():
    '''listing all the files in a folder'''
    folder_list = filedialog.askdirectory()
    sortlist = sorted(os.listdir(folder_list))
    i = 0
    print("Files in ", folder_list, "folder are: ")
    while i < len(sortlist):
        print(sortlist[i] + '\n')
        i += 1

''' building the file manager UI using Tkinter'''

root = Tk()
# creating a canvas to insert image
canv = Canvas(root, width=500, height=420, bg='white')
canv.grid(row=0, column=2)

# img = ImageTk.PhotoImage(Image.open("D:\programming\python\programs\python projects\17_file_manager\file_logo.png"))  
# canv.create_image(20, 20, anchor=NW, image=img)

# creating label and buttons to perform operations
Label(root, text="TechVidvan File Manager", font=("Helvetica", 16), fg="blue").grid(row = 5, column = 2)

Button(root, text = "Open a File", command = open_file).grid(row=15, column =2)

Button(root, text = "Copy a File", command = copy_file).grid(row = 25, column = 2)

Button(root, text = "Delete a File", command = delete_file).grid(row = 35, column = 2)

Button(root, text = "Rename a File", command = rename_file).grid(row = 45, column = 2)

Button(root, text = "Move a File", command = move_file).grid(row = 55, column =2)

Button(root, text = "Make a Folder", command = make_folder).grid(row = 75, column = 2)

Button(root, text = "Remove a Folder", command = remove_folder).grid(row = 65, column =2)

Button(root, text = "List all Files in Directory", command = list_files).grid(row = 85,column = 2)

root.mainloop()

