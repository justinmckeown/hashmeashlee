from tkinter import *
from tkinter.filedialog import askdirectory
import diectorydive


def gui_window():
    root = Tk()
    myLabel = Label(root, text="Hello world")
    file_path = Entry(root)
    myButton = Button(root, text="find Folder", command=get_filepath)
    myLabel.grid(row=0, column=0)
    file_path.grid(row=0, column=1)
    myButton.grid(row=0, column=2)
    root.mainloop()


def get_filepath():
    pth = askdirectory()
    print(f'PATH: {pth}')
    



if __name__ == '__main__':
    gui_window()