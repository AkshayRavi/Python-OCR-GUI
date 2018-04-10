from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import Image
import pytesseract

root = Tk(  )

def readFimage():
    path = T1.get('1.0','end-1c')
    if path:
        im = Image.open(path)
        text = pytesseract.image_to_string(im, lang = 'eng')
        T2.delete('1.0',END)
        T2.insert(END,text)
    else:
        T2.delete('1.0',END)
        T2.insert(END,"FILE CANNOT BE READ")
    

def OpenFile():
    name = askopenfilename(initialdir="/media/akshay/CC8A9DC68A9DAE08/Linux Share/Python/Image GUI Project",
                           filetypes =(("PNG File", "*.png"),("BMP File", "*.bmp"),("JPEG File", "*.jpeg")),
                           title = "Choose a file."
                           ) 
    T1.delete("1.0",END)
    T1.insert(END,name)
Title = root.title( "Image Reader!")
path = StringVar()

L01 = Label(root,text="Image ")
L01.grid(row = 1,column = 1,sticky=(E))
L02 = Label(root,text=" Reader")
L02.grid(row = 1,column = 2,sticky=(W))

L2 = Label(root,text = "INPUT IMAGE:")
L2.grid(row=2,column = 1)

B1 = Button(root,text="Browse",command = OpenFile)
B1.grid(row=2,column=2)

L3 = Label(root,text = "Path:")
L3.grid(row = 3,column=1,sticky=(W))

T1 = Text(root,height = 2)
T1.grid(row = 4,column = 1,columnspan=2)

B2 = Button(root,text="READ FROM IMAGE",command = readFimage)
B2.grid(row = 5,column = 2)

L4 = Label(root,text = "DATA IN IMAGE:")
L4.grid(row = 6,column=1,sticky=(W))

T2 = Text(root,height = 6)
T2.grid(row = 7,column = 1,columnspan=2)



root.mainloop()
