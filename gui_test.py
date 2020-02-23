import tkinter as tk

# create the root object, which has to be created before any other widget
root = tk.Tk()

# create a label child widget, and add the text to be displayed for the label
# pack method tells Tk to fit the size of the window to the given text
w = tk.Label(root, text="Hello world!").pack()



logo = tk.PhotoImage(file="images/giphy.gif")

w1 = tk.Label(root, image=logo).pack(side="right")
desc = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, 
sunt in culpa qui officia deserunt mollit anim id est laborum."""

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=desc).pack()

root.mainloop()