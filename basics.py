import tkinter as tk

#----WINDOW BASICS----
#create window
root = tk.Tk()
#window size
root.geometry("500x500")
#window title
root.title("My First GUI")
#label
label = tk.Label(root, text="Hello World!", font=("Arial", 24))
#layout
label.pack(pady=20, padx=20)

#textbox for multiline input, for descriptions, etc.
textbox = tk.Text(root, height=5, font=("Arial", 16))
textbox.pack()

#textbox for single line input, for usernames, passwords, etc.
myentry = tk.Entry(root, font=("Arial", 16))
myentry.pack(pady=10)

#---BUTTONS---
button = tk.Button(root, text="Click Me!", font=("Arial", 16))
button.pack(pady=10, padx=10)

#Tkinter container
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)  

button1 = tk.Button(buttonframe, text="Button 1", font=("Arial", 16)) 
button1.grid(row=0, column=0, padx=5, pady=5, sticky="ew") 
button2 = tk.Button(buttonframe, text="Button 2", font=("Arial", 16))
button2.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
button3 = tk.Button(buttonframe, text="Button 3", font=("Arial", 16))
button3.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

buttonframe.pack(pady=10, padx=10, fill="x")
#keep window open(ALWAYS LAST LINE)
root.mainloop() 