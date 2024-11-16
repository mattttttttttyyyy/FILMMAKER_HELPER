from tkinter import *
from create_folder import CreateFolders

create_project = False
root = Tk()
create_folders = CreateFolders()
root.geometry("300x200")
root.title("FILMMAKER CLEAN UP")

def open_popup():
    top = Tk()
    top.geometry("300x100")
    Label(top, text="Project name:").pack()
    t1 = Text(top, height=2, width=20)
    t1.pack()

    def value(t):
        x = t.get('1.0', 'end-1c')
        return x

    def submit():
        a = value(t1)
        top.quit()
        create_folders.organize_folder(a)

    Button(top, text='Submit', command=submit).pack()
    top.title("Let's name the project")


def organize_files():
    open_popup()

organize_project_folder = Button(root, text="Organize project folder", command=organize_files)
organize_project_folder.pack()

turn_off = Button(root, text="Close", command=root.quit)
turn_off.pack()

root.mainloop()
