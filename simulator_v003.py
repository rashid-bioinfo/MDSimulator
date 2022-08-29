from tkinter import *
from tkinter import filedialog # module for browsing and loading files
import os
from tkinter import ttk # modle for using dropdown menu

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
        self.solvate_btn = Button(self.f2, text="Define box & Solvate", fg="green", font="Roman 11 bold", borderwidth=2, command=self.runSolvate)
        self.ions_btn = Button(self.f2, text="Add ions", fg="green", font="Roman 11 bold", borderwidth=2, command=self.runIons)
        self.minimize_btn = Button(self.f2, text="Energy Minimization", fg="green", font="Roman 11 bold", borderwidth=2, command=self.runMinimize)
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
   
    ### -----   Function for running toplogy module ((Step 1))
    def runTopology(self):
        self.ToplogyWindow = Toplevel(self.master)
        self.ToplogyWindow.geometry("500x150") # width x length
        self.ToplogyWindow.resizable(False, False)
        self.ToplogyWindow.title("Generate Toplogy")
        self.app = TopologyModule(self.ToplogyWindow)
    
     ### -----   Function for defining box and solvation ((Step 2))
    def runSolvate(self):
        self.SolvateWindow = Toplevel(self.master)
        self.SolvateWindow.geometry("500x150") # width x length
        self.SolvateWindow.resizable(False, False)
        self.SolvateWindow.title("Define Box & Solvation")
        self.app = SolvateModule(self.SolvateWindow)

     ### -----   Function for addion ions ((Step 3))
    def runIons(self):
        self.IonsWindow = Toplevel(self.master)
        self.IonsWindow.geometry("500x150") # width x length
        self.IonsWindow.resizable(False, False)
        self.IonsWindow.title("Add Ions")
        self.app = IonsModule(self.IonsWindow)

     ### -----   Function for energy minimization ((Step 4))
    def runMinimize(self):
        self.MinimizeWindow = Toplevel(self.master)
        self.MinimizeWindow.geometry("500x150") # width x length
        self.MinimizeWindow.resizable(False, False)
        self.MinimizeWindow.title("Energy Minimization")
        self.app = MinimizeModule(self.MinimizeWindow)

    ### ----- dummy function
    def dummy(self):
        pass

    ### -----   function for EXIT button ----- ###
    def exit(self):
        self.master.destroy()

##______________________________________________________________________##
#                                                                        #      
#                      Step 1: Generate Topology                         #
##______________________________________________________________________##

class TopologyModule():
    def __init__(self, master):

        self.master = master 

        ##---------------------------------------------##           
        #               Topology Module GUI             #
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
    #               Topology Module Methods         #
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
##______________________________________________________________________##
#                                                                        #      
#                    Step 2: Define box & Solvation                      #
##______________________________________________________________________##

class SolvateModule():
    def __init__(self, master):

        self.master = master 

        ##---------------------------------------------##           
        #               Solvate Module GUI              #
        ##---------------------------------------------##

        ### -- Browse button for loading protien file 

        self.f1 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f1.pack(side="top", pady=25, ipadx=20)

        self.bsize_label = Label(self.f1, text="Box Size: ", font="Roman 10 bold")
        self.bsize_label.grid(row=1, column=1, sticky=W,  pady=5, ipadx=5, ipady=3)
        self.bsize_label = Label(self.f1, text="Box Type: ", font="Roman 10 bold")
        self.bsize_label.grid(row=1, column=3, sticky=W,  pady=5, padx=1, ipady=3)

        self.bsize_value = DoubleVar()
        self.bsize_entry = Entry(self.f1, textvariable=self.bsize_value, width=10)
        self.bsize_entry.grid(row=1, column=2, padx=5, pady=5)
                  
        # Combobox dropdown menu
        self.param_value = StringVar(value=' cubic')
        self.param_combo = ttk.Combobox(self.f1, width = 13, textvariable = self.param_value)

        self.param_combo['values'] = (' cubic', 
                          ' dodecahedron',
                          ' octahedron',
                          ' triclinic')

        self.param_combo.grid(row=1, column=4, padx=12, sticky=W, pady=10)


        ### -- Buttons of button at the bottom ((Run, Exit)) 

        self.f2 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f2.pack(side="bottom")
        
        ### -----   Buttons for running the script, clearing and exiting the program ----- ###
        self.run_btn = Button(self.f2, text="Run", fg="blue", font="Roman 11 bold", borderwidth=2, command=self.runSolvate)
        self.exit_btn = Button(self.f2, text="Main", fg="green", font="Roman 11 bold", borderwidth=2, command=self.exit)

        self.run_btn.grid(row=3, column=1, padx=1, ipadx=5)
        self.exit_btn.grid(row=3, column=2, padx=1, ipadx=1)

    ##---------------------------------------------##           
    #               Solvate Module Methods          #
    ##---------------------------------------------##
    
    def dummy(self):
        pass

    ### -- Function for running gmx command for defining box and solvate  
    def runSolvate(self):
        # define the box    
        os.system(f'gmx editconf -f protein_processed.gro -o protein_newbox.gro -c -d {self.bsize_value.get()} -bt {self.param_value.get()}')
        # os.system(f'gmx editconf -f protein_processed.gro -o ptor_newbox.gro -c -d 1.0 -bt cubic')

        # solvation
        os.system(f'gmx solvate -cp protein_newbox.gro -cs spc216.gro -o protein_solv.gro -p topol.top')

    ### -----   Function for EXIT button ----- ###
    def exit(self):
        self.master.destroy()

##______________________________________________________________________##
#                                                                        #      
#                           Step 3: Add Ions                             #
##______________________________________________________________________##

class IonsModule():
    def __init__(self, master):

        self.master = master 

        ##---------------------------------------------##           
        #               Ions Module GUI             #
        ##---------------------------------------------##

        ### -- Browse button for loading protien file 

        self.f1 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f1.pack(side="top", pady=25)

        self.protein_label = Label(self.f1, text="Load MDP File: ", font="Roman 10 bold")
        self.protein_label.grid(row=1, column=1, sticky=W,  pady=5, ipadx=5, ipady=3)
        self.protein_label = Label(self.f1, text="Use default settings or customize: ", font="Roman 10")
        self.protein_label.grid(row=1, column=2, sticky=W,  pady=5, ipadx=5, ipady=3)

        self.protein_browse = Button(self.f1, text="Edit file", command=self.editFile)
        self.protein_browse.grid(row=1, column=3, padx=5, pady=5)

        ### -- Buttons of button at the bottom ((Run, Exit)) 

        self.f2 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f2.pack(side="bottom")
        
        ### -----   Buttons for running the script, clearing and exiting the program ----- ###
        self.run_btn = Button(self.f2, text="Run", fg="blue", font="Roman 11 bold", borderwidth=2, command=self.runIons)
        self.exit_btn = Button(self.f2, text="Main", fg="green", font="Roman 11 bold", borderwidth=2, command=self.exit)

        self.run_btn.grid(row=3, column=1, padx=1, ipadx=5)
        self.exit_btn.grid(row=3, column=2, padx=1, ipadx=1)

    ##---------------------------------------------##           
    #               Ions Module Methods         #
    ##---------------------------------------------##

    ### -- Function for browse button to load protein file
    def editFile(self):   
        os.system('gedit ions.mdp')


    ### -- Function for running gmx command for adding ions
    def runIons(self):
        os.system(f'gmx grompp -f ions.mdp -c protein_solv.gro -p topol.top -o ions.tpr')
        os.system(f'gmx genion -s ions.tpr -o protein_solv_ions.gro -p topol.top -pname NA -nname CL -neutral')

    ### -----   Function for EXIT button ----- ###
    def exit(self):
        self.master.destroy()
##______________________________________________________________________##
#                                                                        #      
#                       Step 4: Energy Minimization                      #
##______________________________________________________________________##

class MinimizeModule():
    def __init__(self, master):

        self.master = master 

        ##---------------------------------------------##           
        #               Minimize Module GUI             #
        ##---------------------------------------------##

        ### -- Browse button for loading protien file 

        self.f1 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f1.pack(side="top", pady=25)

        self.protein_label = Label(self.f1, text="Load MDP File: ", font="Roman 10 bold")
        self.protein_label.grid(row=1, column=1, sticky=W,  pady=5, ipadx=5, ipady=3)
        self.protein_label = Label(self.f1, text="Use default settings or customize: ", font="Roman 10")
        self.protein_label.grid(row=1, column=2, sticky=W,  pady=5, ipadx=5, ipady=3)

        self.protein_browse = Button(self.f1, text="Edit file", command=self.editFile)
        self.protein_browse.grid(row=1, column=3, padx=5, pady=5)

        ### -- Buttons of button at the bottom ((Run, Exit)) 

        self.f2 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f2.pack(side="bottom")
        
        ### -----   Buttons for running the script, clearing and exiting the program ----- ###
        self.run_btn = Button(self.f2, text="Run", fg="blue", font="Roman 11 bold", borderwidth=2, command=self.runMinim)
        self.exit_btn = Button(self.f2, text="Main", fg="green", font="Roman 11 bold", borderwidth=2, command=self.exit)

        self.run_btn.grid(row=3, column=1, padx=1, ipadx=5)
        self.exit_btn.grid(row=3, column=2, padx=1, ipadx=1)

    ##---------------------------------------------##           
    #               Minimize Module Methods         #
    ##---------------------------------------------##

    ### -- Function for browse button to load protein file
    def editFile(self):   
        os.system('gedit minim.mdp')


    ### -- Function for running gmx command for energy minimzation
    def runMinim(self):
        os.system(f'gmx grompp -f minim.mdp -c protein_solv_ions.gro -p topol.top -o em.tpr')
        os.system(f'gmx mdrun -v -deffnm em ')

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
