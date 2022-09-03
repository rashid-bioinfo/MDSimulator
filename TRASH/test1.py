from tkinter import * 
from tkinter.ttk import *
  
# create tkinter window
gui = Tk() 
  
# Adding widgets to the window
Label(gui, text='Setting', font=('Verdana', 15)).pack(side=TOP, pady=10) 
  
# Create a photoimage object to use the image
photo = PhotoImage(file = r"/home/rashid/8_Dr_Yasir/Holoenzyme_simulator_git/image.png") 

# Add image to button
Button(gui, image=photo).pack(side=TOP) 
  
gui.mainloop()