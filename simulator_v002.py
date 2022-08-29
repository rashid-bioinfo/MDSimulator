from tkinter import *
from tkinter import filedialog
import os

print ("\n|-------------------------------------------------------------------|")
print ("\n|                          Enzyme Simulator                         |")
print ("\n|-------------------------------------------------------------------|")
print ("\n|                          Linux version                            |")
print ("\n|-------------------------------------------------------------------|")

##______________________________________________________________________##
#                                                                        #      
#                              Main class                                #
##______________________________________________________________________##

class MDSimulator:
    def __init__(self, master):

        self.master = master 

        ##---------------------------------------------##           
        #                       Main GUI                #
        ##---------------------------------------------##

        ### -- Title frame of Main GUI 

        self.f1 = Frame(self.master, borderwidth=5, relief=SUNKEN)
        self.f1.pack(side="top", pady=10)

        self.f1_title = Label(self.f1, text="Molecular Dynamics Simulator", font="Roman 15 bold", fg="#660099")
        self.f1_title.grid(row=1, column=5, sticky=W, padx=80)

        ### -- Buttons of all 6 steps of Main Simulator 

        self.f2 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f2.pack(side="top", pady=25)

        ### -----   Buttons for running the script, clearing and exiting the program ----- ###
        self.topology_btn = Button(self.f2, text="Generate Topology", fg="green", font="Roman 11 bold", borderwidth=2, command=self.runTopology)
        self.solvate_btn = Button(self.f2, text="Define box & Solvate", fg="green", font="Roman 11 bold", borderwidth=2, command=self.dummy)
        self.ions_btn = Button(self.f2, text="Add ions", fg="green", font="Roman 11 bold", borderwidth=2, command=self.dummy)
        self.minimize_btn = Button(self.f2, text="Energy Minimization", fg="green", font="Roman 11 bold", borderwidth=2, command=self.dummy)
        self.equal_btn = Button(self.f2, text="Equlibration", fg="green", font="Roman 11 bold", borderwidth=2, command=self.dummy)
        self.prod_btn = Button(self.f2, text="Production MD", fg="green", font="Roman 11 bold", borderwidth=2, command=self.dummy)

        
        # packing of butons ---
        self.topology_btn.grid(row=1, column=1, padx=2, ipadx=5)
        self.solvate_btn.grid(row=1, column=3, padx=2, ipadx=5)
        self.ions_btn.grid(row=1, column=5, padx=2, ipadx=50)
        self.minimize_btn.grid(row=3, column=5, padx=2, pady=10, ipadx=1)
        self.equal_btn.grid(row=3, column=3, padx=2, pady=10, ipadx=40)
        self.prod_btn.grid(row=3, column=1, padx=2, pady=10, ipadx=25)

        # Definition and packing of arrow labels
        self.topology_arr = Label(self.f2, text=">", fg="black", font="Roman 12 bold")
        self.topology_arr.grid(row=1, column=2, padx=2, ipadx=5)
        self.solvate_arr = Label(self.f2, text=">", fg="black", font="Roman 12 bold")
        self.solvate_arr.grid(row=1, column=4, padx=2, ipadx=5)
        self.ions_arr = Label(self.f2, text="v", fg="black", font="Roman 14")
        self.ions_arr.grid(row=2, column=5, padx=2, ipadx=5, pady=5)
        self.ions_arr = Label(self.f2, text="<", fg="black", font="Roman 12 bold")
        self.ions_arr.grid(row=3, column=4, padx=2, ipadx=5)
        self.ions_arr = Label(self.f2, text="<", fg="black", font="Roman 12 bold")
        self.ions_arr.grid(row=3, column=2, padx=2, ipadx=5)

        ### -- Buttons of button at the bottom ((Analysis, Exit)) 

        self.f3 = Frame(self.master, borderwidth=5, relief=GROOVE)
        # self.f7.grid(row=1, column=1, padx=20)
        self.f3.pack(side="bottom")
        
        ### -----   Buttons for running the script, clearing and exiting the program ----- ###
        self.analyze_btn = Button(self.f3, text="Analysis", fg="blue", font="Roman 11 bold", borderwidth=2, command=self.dummy)
        self.exit_btn = Button(self.f3, text="Exit", fg="red", font="Roman 11 bold", borderwidth=2, command=self.exit)

        self.analyze_btn.grid(row=1, column=1, padx=5, ipadx=5)
        self.exit_btn.grid(row=1, column=2, padx=5, ipadx=15)

    ##---------------------------------------------##           
    #                   Main Methods                #
    ##---------------------------------------------##
   
    ### -----   Function for running toplogy module
    def runTopology(self):
        self.ToplogyWindow = Toplevel(self.master)
        self.ToplogyWindow.geometry("500x150") # width x length
        self.ToplogyWindow.resizable(False, False)
        self.ToplogyWindow.title("Generate Toplogy")
        self.app = TopologyModule(self.ToplogyWindow)
    
    def dummy(self):
        pass

    ### -----   function for EXIT button ----- ###
    def exit(self):
        self.master.destroy()

##______________________________________________________________________##
#                                                                        #      
#                         Generate Topology                              #
##______________________________________________________________________##

class TopologyModule():
    def __init__(self, master):

        self.master = master 

        ##---------------------------------------------##           
        #               TopologyClass GUI               #
        ##---------------------------------------------##

        ### -- Browse button for loading protien file 

        self.f1 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f1.pack(side="top", pady=25)

        self.protein_label = Label(self.f1, text="Load Protein File: ", font="Roman 10 bold")
        self.protein_label.grid(row=1, sticky=W,  pady=5, ipadx=5, ipady=3)

        self.protein_value = StringVar()
        self.protein_entry = Entry(self.f1, textvariable=self.protein_value, width=25)
        self.protein_entry.grid(row=1, column=2, padx=10, pady=5)

        self.protein_browse = Button(self.f1, text="Browse", command=self.fileBrowse)
        self.protein_browse.grid(row=1, column=3, padx=5, pady=5)

        ### -- Buttons of button at the bottom ((Run, Exit)) 

        self.f2 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f2.pack(side="bottom")
        
        ### -----   Buttons for running the script, clearing and exiting the program ----- ###
        self.run_btn = Button(self.f2, text="Run", fg="blue", font="Roman 11 bold", borderwidth=2, command=self.runTopology)
        self.exit_btn = Button(self.f2, text="Main", fg="green", font="Roman 11 bold", borderwidth=2, command=self.exit)

        self.run_btn.grid(row=3, column=1, padx=1, ipadx=5)
        self.exit_btn.grid(row=3, column=2, padx=1, ipadx=1)

    ##---------------------------------------------##           
    #               TopologyClass Methods           #
    ##---------------------------------------------##
    
    def dummy(self):
        pass

    ### -- Function for browse button to load protein file
    def fileBrowse(self):   
        self.receptor_selected = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a Receptor File",
                                            filetypes = (("Text files",
                                                            "*.pdb*"),
                                                        ("all files",
                                                            "*.*")))
        self.protein_value.set(self.receptor_selected)


    ### -- Function for running gmx command for gnerating topology file    
    def runTopology(self):
        os.system(f'gmx pdb2gmx -f {self.protein_value.get()} -o protein_processed.gro -water spce')
        # os.system(f'gmx pdb2gmx -f 1aki_clean.pdb -o protein_processed.gro -water spce')

    ### -----   Function for EXIT button ----- ###
    def exit(self):
        self.master.destroy()



# ==========================================

### --- Creating object of the class 

if __name__ == '__main__':
    
    root = Tk()
    root.geometry("730x300") # width x length
    root.resizable(False, False)
    root.title("MD_Simulator")
    app = MDSimulator(root)
    root.mainloop()
