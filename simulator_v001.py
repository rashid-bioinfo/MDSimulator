from tkinter import *

print ("\n|-------------------------------------------------------------------|")
print ("\n|                          Enzyme Simulator                         |")
print ("\n|-------------------------------------------------------------------|")
print ("\n|                          Linux version                            |")
print ("\n|-------------------------------------------------------------------|")

#------------------------------------------------------ ----##           
#                   Main GUI                     #
##----------------------------------------------------------##

class MDSimulator:
    def __init__(self, master):

        self.master = master 

        ##----------------------------------------------------------------------##           
        #                             Title Frame (Top)                          #
        ##----------------------------------------------------------------------##

        self.f1 = Frame(self.master, borderwidth=5, relief=SUNKEN)
        self.f1.pack(side="top", pady=10)

        self.f1_title = Label(self.f1, text="Molecular Dynamics Simulator", font="Roman 15 bold", fg="#660099")
        self.f1_title.grid(row=1, column=5, sticky=W, padx=80)





# ==========================================

### --- Creating object of the class 

if __name__ == '__main__':
    
    root = Tk()
    root.geometry("575x640") # width x length
    root.resizable(False, False)
    root.title("MD_Simulator")
    app = MDSimulator(root)
    root.mainloop()
