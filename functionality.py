import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        
        self.label = tk.Label(self.root, text="Your Message", font=("Arial", 24))
        self.label.pack(pady=20, padx=20) 
        
        self.textbox = tk.Text(self.root, height=5, font=("Arial", 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)
        
        #checkbox
        #IntVar() is used to track the state of the checkbox (checked or unchecked)
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Messagebox!",font=("Arial", 16), variable=self.check_state)
        self.check.pack(pady=10, padx=10)
        
        self.button = tk.Button(self.root, text="Show Message!", font=("Arial", 18), command=self.show_message)
        self.button.pack(pady=10, padx=10)
        
        #protocol method is used to handle the window close event. When the user tries to close the window, the on_closing method will be called, which will ask the user for confirmation before closing the window.
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
        
    #function to show the message in the console or in a messagebox depending on the state of the checkbox
    def show_message(self):
        #get() method retrieves the current value of the checkbox (0 for unchecked, 1 for checked)
        #if the checkbox is unchecked, it will print the message in the console. If the checkbox is checked, it will display the message in a messagebox.
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))
            
    #shortcut for showing the messagebox when the user presses Control + Enter        
    def shortcut(self, event):
        #event.state checks if the Control key is pressed (state 12 corresponds to the Control key)
        #event.keysym checks if the "Enter" key is pressed
        if event.state == 12 and event.keysym == "Return":
            self.show_message()
    
    #function to handle the window close event, asking the user for confirmation before closing the window        
    def on_closing(self):
        #askokcancel() method displays a confirmation dialog with "OK" and "Cancel" options. If the user clicks "OK", the method returns True, and the window will be destroyed. If the user clicks "Cancel", the method returns False, and the window will remain open.
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy() 
                        
MyGUI()