from tkinter import *
from PIL import ImageTk 
from PIL import Image as Img



root = Tk()


originalImage = ImageTk.PhotoImage(Img.open('/home/escanor/Documents/DSP/Facial-Recognition/database/1.jpeg'))

originalSection = Label(root , image=originalImage)

originalSection.pack()

root.mainloop()