from tkinter import  Tk, Label, Button, Entry, W, N, E, S, X,Y, Frame, LEFT, RIGHT, CENTER, Text, messagebox
from tkinter.filedialog import askdirectory
import diectorydive


class HasherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hash Me Ashlee")
        self.master.minsize(750,60)
        
        self.width = master.winfo_screenwidth()
        self.height = master.winfo_screenheight()

        search_frame = Frame(master)
        button_frame = Frame(master)

        self.myLabel = Label(search_frame, text="Path to Folder: ")
        self.myButton = Button(search_frame, text="Find Folder", command=self.get_filepath)
        self.the_file_path = Entry(search_frame)

        self.hashButton = Button(button_frame, text="Hash Files", command=self.go_hash)

        #grid layout....
        self.myLabel.grid(row=0, column=0, padx=5, pady=10)
        self.the_file_path.grid(row=0, column=1, columnspan=3, padx=5, pady=10, sticky=(W,E))
        self.myButton.grid(row=0, column=4, padx=5, pady=5, sticky=(E))
        self.hashButton.grid(row=1, column=4, padx=5, pady=2, sticky=(E))
        
        #Add frames to 
        search_frame.grid(row=0, column=0, columnspan=2, sticky=(N,W,E))
        button_frame.grid(row=1, column=1, sticky=(N,E))

        #configure searchframes expanding
        search_frame.columnconfigure(0, weight=0)
        search_frame.columnconfigure(1, weight=3)
        search_frame.columnconfigure(2, weight=3)
        search_frame.columnconfigure(3, weight=3)

        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=3)
        


        #TODO: See: https://tkdocs.com/tutorial/grid.html 
        #self.master.columnconfigure()
        #self.master.rowconfigure()


        
        #pack layout...
        #self.myLabel.pack(side=LEFT)
        #self.the_file_path.pack(side=LEFT, expand=True,fill=Y)
        #self.myButton.pack(side=RIGHT)
        #self.hashButton.pack(side=RIGHT)
        #search_frame.pack(side='top', expand=True)
        #button_frame.pack(side='bottom', expand=True)
        
        

    
        #self.the_file_path.bind("<1>", self.get_filepath)

        
    def get_filepath(self):
        pth = askdirectory()
        print(f'PATH: {pth}')
        self.the_file_path.insert(0,pth)
    
    def go_hash(self):
        try:
            print(f'go_hash called')
        except Exception as e:
            print(f'Error in go_hash: {e}')
            messagebox.showerror("ERROR", f"something has gone wrong while attempting to produce hashes o fyour files. Message is as follows:\n {e}")
        else:
            messagebox.showinfo("SUCCESS!", "Hashing files has completed without error")

    



if __name__ == '__main__':
        root = Tk()
        my_app = HasherApp(root)
        root.mainloop()