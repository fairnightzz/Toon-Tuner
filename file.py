from tkinter import filedialog
from tkinter import*

root = Tk()
root.withdraw()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "TEST",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

#root.deiconify()
print (root.filename)

