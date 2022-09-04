from tkinter import *                   # module for using tkinter GUI builder
from tkinter import filedialog          # module for browsing and loading files
import os                               # module to use gromacs in python
from tkinter import ttk                 # modle for using dropdown menu
# module for yes/no or info messages for better understanding and guiding the user
from tkinter.messagebox import askyesno 
from tkinter.messagebox import showerror, showinfo, showwarning

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

        ### _________ Title frame of Main GUI __________ ### 
        self.f1 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f1.pack(side="top", pady=20)

        self.f1_title = Label(self.f1, text="Molecular Dynamics Simulator", font="Roman 15 bold", fg="blue")
        self.f1_title.grid(row=1, column=5, sticky=W, padx=190)


        ### _________ Browsing directories of MDP files and setting Output directory __________ ### 
        self.f2 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f2.pack(side="top", pady=10)

        self.mdp_label = Label(self.f2, text="MDP Files Directories: ", font="Roman 10 bold")
        self.outDir_label = Label(self.f2, text="Ouput Files Directories: ", font="Roman 10 bold")
        self.mdp_label.grid(row=1, column=1, padx=12, pady=5)
        self.outDir_label.grid(row=2, column=1, padx=12, pady=5)

        # setting globals to use these variables in other classes' functions
        global mdp_value
        global outDir_value
        mdp_value = StringVar()
        outDir_value = StringVar()
        self.mdp_entry = Entry(self.f2, textvariable=mdp_value, width=50)
        self.outDir_entry = Entry(self.f2, textvariable=outDir_value, width=50)
        self.mdp_entry.grid(row=1, column=2, padx=10, pady=5)
        self.outDir_entry.grid(row=2, column=2, padx=10, pady=5)


        self.mdp_btn = Button(self.f2, text="Define", command=self.mdp_directory)
        self.outDir_btn = Button(self.f2, text="Define", command=self.output_directory)
        self.mdp_btn.grid(row=1, column=3, padx=12, pady=5)
        self.outDir_btn.grid(row=2, column=3, padx=12, pady=5)
        
        
        ### _________ Buttons of all 6 steps of Main Simulator __________ ### 

        self.f3 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f3.pack(side="top", pady=20)

        ### -----   Buttons for running the script, clearing and exiting the program ----- ###
        self.topology_btn = Button(self.f3, text="Generate Topology", border=5, bg="yellow", fg="black", font="Roman 11 bold", borderwidth=2, command=self.runTopology)
        self.solvate_btn = Button(self.f3, text="Define box & Solvate", border=5, bg="red", fg="black", font="Roman 11 bold", borderwidth=2, command=self.runSolvate)
        self.ions_btn = Button(self.f3, text="Add ions", border=5, bg="red", fg="black", font="Roman 11 bold", borderwidth=2, command=self.runIons)
        self.minimize_btn = Button(self.f3, text="Energy Minimization", border=5, bg="red", fg="black", font="Roman 11 bold", borderwidth=2, command=self.runMinimize)
        self.equal_btn = Button(self.f3, text="Equlibration", border=5, fg="black", bg="red", font="Roman 11 bold", borderwidth=2, command=self.runEqual)
        self.prod_btn = Button(self.f3, text="Production MD", border=5, fg="black", bg="red", font="Roman 11 bold", borderwidth=2, command=self.runProd)
        # packing of butons ---
        self.topology_btn.grid(row=1, column=1, padx=2, pady=6, ipadx=5)
        self.solvate_btn.grid(row=1, column=3, padx=2, pady=6, ipadx=5)
        self.ions_btn.grid(row=1, column=5, padx=2, pady=6, ipadx=50)
        self.minimize_btn.grid(row=3, column=5, padx=2,  pady=10, ipadx=1)
        self.equal_btn.grid(row=3, column=3, padx=2, pady=10, ipadx=40)
        self.prod_btn.grid(row=3, column=1, padx=2, pady=10, ipadx=25)
        
        # Definition and packing of arrow labels
        self.topology_arr = Button(self.f3, text=">", fg="black", font="Roman 12 bold", command=self.arrTopology)
        self.topology_arr.grid(row=1, column=2, padx=2, pady=6, ipadx=5)
        self.solvate_arr = Button(self.f3, text=">", fg="black", font="Roman 12 bold", command=self.arrSolvate)
        self.solvate_arr.grid(row=1, column=4, padx=2, pady=6, ipadx=5)
        self.ions_arr = Button(self.f3, text="v", fg="black", font="Roman 14", command=self.arrIons)
        self.ions_arr.grid(row=2, column=5, padx=2, ipadx=1, ipady=4, pady=5)
        self.minimize_arr = Button(self.f3, text="<", fg="black", font="Roman 12 bold", command=self.arrMinimize)
        self.minimize_arr.grid(row=3, column=4, padx=2, ipadx=5)
        self.equal_arr = Button(self.f3, text="<", fg="black", font="Roman 12 bold", command=self.arrEqual)
        self.equal_arr.grid(row=3, column=2, padx=2, ipadx=5)

        ### _________ Buttons of button at the bottom ((Analysis, Exit)) __________ ### 

        self.f4 = Frame(self.master, borderwidth=5, relief=GROOVE)
        # self.f7.grid(row=1, column=1, padx=20)
        self.f4.pack(side="bottom")
        
        ### -----   Buttons for running the script, clearing and exiting the program ----- ###
        self.analysis_btn = Button(self.f4, text="Analysis", fg="blue", font="Roman 11 bold", borderwidth=2, command=self.runAnalysis)
        self.exit_btn = Button(self.f4, text="Exit", fg="red", font="Roman 11 bold", borderwidth=2, command=self.exit)
        self.analysis_btn.grid(row=1, column=1, padx=5, ipadx=5)
        self.exit_btn.grid(row=1, column=2, padx=5, ipadx=15)


        ### -- Disable all buttons except Generate topology in the beginning
        self.solvate_btn["state"] = "disabled"
        self.ions_btn["state"] = "disabled"
        self.minimize_btn["state"] = "disabled"
        self.equal_btn["state"] = "disabled"
        self.prod_btn["state"] = "disabled"

        self.solvate_arr["state"] = "disabled"
        self.ions_arr["state"] = "disabled"
        self.minimize_arr["state"] = "disabled"
        self.equal_arr["state"] = "disabled"

    ##---------------------------------------------##           
    #                   Main Methods                #
    ##---------------------------------------------##

    #__________________________________________________________________#

    ### -----   for defining MDP files directories ----- ###
    def mdp_directory(self):
        self.mdpDir_selected = filedialog.askdirectory()
        mdp_value.set(self.mdpDir_selected)


    ### -----   for taking OUTPUT DIRECTORY PATH from the user ----- ###
    def output_directory(self):

        self.outDir_selected = filedialog.askdirectory()
        # try:
        #     # To ensure that the directory is empty and should be a valid path
        #     if os.path.exists(self.outDir_selected) and os.path.isdir(self.outDir_selected):
        #         if not os.listdir(self.outDir_selected):
        outDir_value.set(self.outDir_selected)
        #         else:
        #             showwarning("Directory is not empty!", "Please define an empty directory.")
        #     else:
        #         showerror("Path is not valid!", "Please define a valid path.")
            
        # except TypeError:
        #     print("No directory is selected")

    #________________________________________________________#

    ### -----   Function for running toplogy module ((Step 1))
    def runTopology(self):
        self.ToplogyWindow = Toplevel(self.master)
        self.ToplogyWindow.geometry("500x200") # width x length
        self.ToplogyWindow.resizable(False, False)
        self.ToplogyWindow.title("Generate Toplogy")
        self.app = TopologyModule(self.ToplogyWindow)
    
     ### -----   Function for defining box and solvation ((Step 2))
    def runSolvate(self):
        self.SolvateWindow = Toplevel(self.master)
        self.SolvateWindow.geometry("500x200") # width x length
        self.SolvateWindow.resizable(False, False)
        self.SolvateWindow.title("Define Box & Solvation")
        self.app = SolvateModule(self.SolvateWindow)

     ### -----   Function for addion ions ((Step 3))
    def runIons(self):
        self.IonsWindow = Toplevel(self.master)
        self.IonsWindow.geometry("500x200") # width x length
        self.IonsWindow.resizable(False, False)
        self.IonsWindow.title("Add Ions")
        self.app = IonsModule(self.IonsWindow)

     ### -----   Function for energy minimization ((Step 4))
    def runMinimize(self):
        self.MinimizeWindow = Toplevel(self.master)
        self.MinimizeWindow.geometry("500x200") # width x length
        self.MinimizeWindow.resizable(False, False)
        self.MinimizeWindow.title("Energy Minimization")
        self.app = MinimizeModule(self.MinimizeWindow)

     ### -----   Function for energy Equilibration ((Step 5))
    def runEqual(self):
        self.EqualWindow = Toplevel(self.master)
        self.EqualWindow.geometry("500x200") # width x length
        self.EqualWindow.resizable(False, False)
        self.EqualWindow.title("Equilibration")
        self.app = EqualModule(self.EqualWindow)
    
     ### -----   Function for energy Production MD ((Step 6))
    def runProd(self):
        self.ProdWindow = Toplevel(self.master)
        self.ProdWindow.geometry("500x200") # width x length
        self.ProdWindow.resizable(False, False)
        self.ProdWindow.title("Production MD")
        self.app = ProdModule(self.ProdWindow)
    #_________________________________________________________#

    ### -----   Arrow button function ((Step 1 - Generate Toplogy))
    def arrTopology(self):
        
        for item in os.listdir(outDir_value.get()):
            if "protein_processed.gro" == item:
                # print (f"file ({item}) found")
                self.topology_btn["bg"] = "green"
                self.topology_btn["state"] = "disabled"
                
                # when protein_processed.gro is found then previous buttons: disabled & next buttons: enabled
                self.topology_arr["state"] = "disabled"
                self.solvate_btn["bg"] = "yellow"
                self.solvate_btn["state"] = "normal"
                self.solvate_arr["state"] = "normal"

    ### -----   Arrow button function ((Step 2 - Define box & solvate))
    def arrSolvate(self):
        
        for item in os.listdir(outDir_value.get()):
            if "protein_solv.gro" == item:
                # print (f"file ({item}) found")
                self.solvate_btn["bg"] = "green"
                self.solvate_btn["state"] = "disabled"
                
                # when protein_processed.gro is found then previous buttons: disabled & next buttons: enabled
                self.solvate_arr["state"] = "disabled"
                self.ions_btn["bg"] = "yellow"
                self.ions_btn["state"] = "normal"
                self.ions_arr["state"] = "normal"

    ### -----   Arrow button function ((Step 3 - Add ions))
    def arrIons(self):
        
        for item in os.listdir(outDir_value.get()):
            if "protein_solv_ions.gro" == item:
                # print (f"file ({item}) found")
                self.ions_btn["bg"] = "green"
                self.ions_btn["state"] = "disabled"
                
                # when protein_processed.gro is found then previous buttons: disabled & next buttons: enabled
                self.ions_arr["state"] = "disabled"
                self.minimize_btn["bg"] = "yellow"
                self.minimize_btn["state"] = "normal"
                self.minimize_arr["state"] = "normal"
                
    ### -----   Arrow button function ((Step 4 - Energy Minimization))
    def arrMinimize(self):
        
        for item in os.listdir(outDir_value.get()):
            if "em.gro" == item:
                # print (f"file ({item}) found")
                self.minimize_btn["bg"] = "green"
                self.minimize_btn["state"] = "disabled"
                
                # when protein_processed.gro is found then previous buttons: disabled & next buttons: enabled
                self.minimize_arr["state"] = "disabled"
                self.equal_btn["bg"] = "yellow"
                self.equal_btn["state"] = "normal"
                self.equal_arr["state"] = "normal"
                
    ### -----   Arrow button function ((Step 5 - Equalibration))
    def arrEqual(self):
        
        for item in os.listdir(outDir_value.get()):
            if "npt.gro" == item:
                # print (f"file ({item}) found")
                self.equal_btn["bg"] = "green"
                self.equal_btn["state"] = "disabled"
                
                # when protein_processed.gro is found then previous buttons: disabled & next buttons: enabled
                self.equal_arr["state"] = "disabled"
                self.prod_btn["bg"] = "yellow"
                self.prod_btn["state"] = "normal"

    #_____________________________________________#

    ### -----   function for ANALYSIS button ----- ###
    def runAnalysis(self):
        # To ensure to use this module only if the user has already run virtual screening by VSpipe
        answer = askyesno(title='Confirmation!',
                    message='You can analyze the results only after successfully running MD Simulations. Have you already run simulation?')
        if (answer):
            showinfo("Well done!", "Go ahead with the analysis module")

            # Turns Production MD run btton green, and disable this button
            self.prod_btn["bg"] = "green"
            self.prod_btn["state"] = "disabled"

        else:
            showinfo("Run MD Simulations first!", "You need to run MD simulations first and then use this module.")

    ### -----   function for EXIT button ----- ###
    def exit(self):
        self.master.destroy()

    ### ----- dummy function
    def dummy(self):
        pass

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
        os.system(f'gmx pdb2gmx -f {self.protein_value.get()} -o {outDir_value.get()}/protein_processed.gro -p {outDir_value.get()}/topol.top -i {outDir_value.get()}/posre.itp -water spce')
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

        self.bsize_value = DoubleVar(value=1.0)
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
        os.system(f'gmx editconf -f {outDir_value.get()}/protein_processed.gro -o {outDir_value.get()}/protein_newbox.gro -c -d {self.bsize_value.get()} -bt {self.param_value.get()}')
        # os.system(f'gmx editconf -f protein_processed.gro -o ptor_newbox.gro -c -d 1.0 -bt cubic')

        # solvation
        os.system(f'gmx solvate -cp {outDir_value.get()}/protein_newbox.gro -cs spc216.gro -o {outDir_value.get()}/protein_solv.gro -p {outDir_value.get()}/topol.top')

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

    ### -- Function for browsing MDP protein file
    def editFile(self):   
        os.system(f'gedit {mdp_value.get()}/ions.mdp')


    ### -- Function for running gmx command for adding ions
    def runIons(self):
        os.system(f'gmx grompp -f {mdp_value.get()}/ions.mdp -c {outDir_value.get()}/protein_solv.gro -p {outDir_value.get()}/topol.top -o {outDir_value.get()}/ions.tpr -po {outDir_value.get()}/mdout.mdp')
        os.system(f'gmx genion -s {outDir_value.get()}/ions.tpr -o {outDir_value.get()}/protein_solv_ions.gro -p {outDir_value.get()}/topol.top -pname NA -nname CL -neutral')

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

    ### -- Function for browsing MDP protein file
    def editFile(self):   
        os.system(f'gedit {mdp_value.get()}/minim.mdp')


    ### -- Function for running gmx command for energy minimzation
    def runMinim(self):
        os.system(f'gmx grompp -f {mdp_value.get()}/minim.mdp -c {outDir_value.get()}/protein_solv_ions.gro -p {outDir_value.get()}/topol.top -o {outDir_value.get()}/em.tpr -po {outDir_value.get()}/mdout.mdp')
        os.system(f'gmx mdrun -v -deffnm {outDir_value.get()}/em')

    ### -----   Function for EXIT button ----- ###
    def exit(self):
        self.master.destroy()
##______________________________________________________________________##
#                                                                        #      
#                       Step 5: Equilibration                            #
##______________________________________________________________________##

class EqualModule():
    def __init__(self, master):

        self.master = master 

        ##---------------------------------------------##           
        #               Equal. Module GUI             #
        ##---------------------------------------------##

        ### -- Browse button for loading protien file 

        self.f1 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f1.pack(side="top", pady=25)

        # NVT ensemble (constant Number of particles, Volume, and Temperature)
        self.protein_label = Label(self.f1, text="NVT MDP File: ", font="Roman 10 bold")
        self.protein_label.grid(row=1, column=1, sticky=W,  pady=5, ipadx=5, ipady=3)
        self.protein_label = Label(self.f1, text="Use default settings or customize: ", font="Roman 10")
        self.protein_label.grid(row=1, column=2, sticky=W,  pady=5, ipadx=5, ipady=3)

        self.protein_browse = Button(self.f1, text="Edit file", command=self.editNvtFile)
        self.protein_browse.grid(row=1, column=3, padx=5, pady=5)
        
        # NPT ensemble (constant Number of particles, Pressure, and Temperature)
        self.protein_label = Label(self.f1, text="NPT MDP File: ", font="Roman 10 bold")
        self.protein_label.grid(row=2, column=1, sticky=W,  pady=5, ipadx=5, ipady=3)
        self.protein_label = Label(self.f1, text="Use default settings or customize: ", font="Roman 10")
        self.protein_label.grid(row=2, column=2, sticky=W,  pady=5, ipadx=5, ipady=3)

        self.protein_browse = Button(self.f1, text="Edit file", command=self.editNptFile)
        self.protein_browse.grid(row=2, column=3, padx=5, pady=5)

        ### -- Buttons of button at the bottom ((Run, Exit)) 

        self.f2 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f2.pack(side="bottom")
        
        ### -----   Buttons for running the script, clearing and exiting the program ----- ###
        self.run_btn = Button(self.f2, text="Run", fg="blue", font="Roman 11 bold", borderwidth=2, command=self.runEqual)
        self.exit_btn = Button(self.f2, text="Main", fg="green", font="Roman 11 bold", borderwidth=2, command=self.exit)

        self.run_btn.grid(row=3, column=1, padx=1, ipadx=5)
        self.exit_btn.grid(row=3, column=2, padx=1, ipadx=1)

    ##---------------------------------------------##           
    #               Equal. Module Methods         #
    ##---------------------------------------------##

    ### -- Function for browsing NVT file
    def editNvtFile(self):   
        # NVT ensemble (constant Number of particles, Volume, and Temperature)
        os.system(f'gedit {mdp_value.get()}/nvt.mdp') 

    ### -- Function for browsing NPT file
    def editNptFile(self):  
        # NPT ensemble (constant Number of particles, Pressure, and Temperature)
        os.system(f'gedit {mdp_value.get()}/npt.mdp') 

    ### -- Function for running gmx command for equilibration
    def runEqual(self):
        # NVT ensemble (constant Number of particles, Volume, and Temperature)
        os.system(f'gmx grompp -f {mdp_value.get()}/nvt.mdp -c {outDir_value.get()}/em.gro -r {outDir_value.get()}/em.gro -p {outDir_value.get()}/topol.top -o {outDir_value.get()}/nvt.tpr -po {outDir_value.get()}/mdout.mdp')
        os.system(f'gmx mdrun -v -deffnm {outDir_value.get()}/nvt')

        # NPT ensemble (constant Number of particles, Pressure, and Temperature)
        os.system(f'gmx grompp -f {mdp_value.get()}/npt.mdp -c {outDir_value.get()}/nvt.gro -r {outDir_value.get()}/nvt.gro -t {outDir_value.get()}/nvt.cpt -p {outDir_value.get()}/topol.top -o {outDir_value.get()}/npt.tpr -po {outDir_value.get()}/mdout.mdp')
        os.system(f'gmx mdrun -v -deffnm {outDir_value.get()}/npt')


    ### -----   Function for EXIT button ----- ###
    def exit(self):
        self.master.destroy()

##______________________________________________________________________##
#                                                                        #      
#                       Step 6: Production MD                            #
##______________________________________________________________________##

class ProdModule():
    def __init__(self, master):

        self.master = master 

        ##---------------------------------------------##           
        #               Prod. Module GUI             #
        ##---------------------------------------------##

        ### -- Browse button for loading protien file 

        self.f1 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f1.pack(side="top", pady=25)

        # NVT ensemble (constant Number of particles, Volume, and Temperature)
        self.protein_label = Label(self.f1, text="Load MDP File: ", font="Roman 10 bold")
        self.protein_label.grid(row=1, column=1, sticky=W,  pady=5, ipadx=5, ipady=3)
        self.protein_label = Label(self.f1, text="Use default settings or customize: ", font="Roman 10")
        self.protein_label.grid(row=1, column=2, sticky=W,  pady=5, ipadx=5, ipady=3)

        self.protein_browse = Button(self.f1, text="Edit file", command=self.editFile)
        self.protein_browse.grid(row=1, column=3, padx=5, pady=5)
        
        # Number of CPUs/Threads, want to allocate for running MD simulations
        self.protein_label = Label(self.f1, text="Number of CPUs: ", font="Roman 10 bold")
        self.protein_label.grid(row=2, column=1, sticky=W,  pady=5, ipadx=5, ipady=3)
        self.cpu_value = IntVar()
        self.cpu_entry = Entry(self.f1, textvariable=self.cpu_value, width=10)
        self.cpu_entry.grid(row=2, column=2, padx=1, pady=5)

        ### -- Buttons of button at the bottom ((Run, Exit)) 

        self.f2 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f2.pack(side="bottom")
        
        ### -----   Buttons for running the script, clearing and exiting the program ----- ###
        self.run_btn = Button(self.f2, text="Run", fg="blue", font="Roman 11 bold", borderwidth=2, command=self.runEqual)
        self.exit_btn = Button(self.f2, text="Main", fg="green", font="Roman 11 bold", borderwidth=2, command=self.exit)

        self.run_btn.grid(row=3, column=1, padx=1, ipadx=5)
        self.exit_btn.grid(row=3, column=2, padx=1, ipadx=1)

    ##---------------------------------------------##           
    #               Prod. Module Methods         #
    ##---------------------------------------------##

    ### -- Function for browsing MDP file
    def editFile(self):   
        os.system(f'gedit {mdp_value.get()}/md.mdp') 

    ### -- Function for running gmx command for equilibration
    def runEqual(self):
        os.system(f'gmx grompp -f {mdp_value.get()}/npt.mdp -c {outDir_value.get()}/nvt.gro -r {outDir_value.get()}/nvt.gro -t {outDir_value.get()}/nvt.cpt -p {outDir_value.get()}/topol.top -o {outDir_value.get()}/npt.tpr -po {outDir_value.get()}/mdout.mdp')
        os.system(f'gmx mdrun -v -deffnm {outDir_value.get()}/npt')

        os.system(f'gmx grompp -f {mdp_value.get()}/md.mdp -c {outDir_value.get()}/npt.gro -t {outDir_value.get()}/npt.cpt -p {outDir_value.get()}/topol.top -o {outDir_value.get()}/md_0_1.tpr -po {outDir_value.get()}/mdout.mdp')
        os.system(f'gmx mdrun -v -deffnm {outDir_value.get()}/md_0_1 -nt {self.cpu_value.get()}')

    ### -----   Function for EXIT button ----- ###
    def exit(self):
        self.master.destroy()

# ==========================================

### --- Creating object of the class 

if __name__ == '__main__':
    
    root = Tk()
    root.geometry("800x450") # width x length
    root.resizable(False, False)
    root.title("MD_Simulator")
    app = MDSimulator(root)
    root.mainloop()
