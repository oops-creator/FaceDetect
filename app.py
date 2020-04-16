from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk 
from PIL import Image as Img
import time
import os
import threading
import Recognize






root = Tk()

imgpath =  askopenfilename(initialdir = "./",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))


#Show the original image on left hand side  
originalImage = ImageTk.PhotoImage(
                Img.open(imgpath))
originalSection = Label(root , image=originalImage ,  width=600 , height=600 , borderwidth=2 , relief="groove")
originalSection.grid(row=0,column=0)


#Get all the images from 'database'
relDatabasePath = 'database'

currentDir = os.getcwd()
images = os.listdir(os.path.join(currentDir,relDatabasePath))
dbImages = [os.path.join(currentDir ,relDatabasePath, image) for image in images]

#Show the comparable image on right hand side
comparingSection = Label(root, width=600 , height=600 , borderwidth=2 , relief="groove")
comparingSection.grid(row=0,column=1)

similarImages = [imgpath]
relativeImage = None

#Loop through the images in the database folder
def changeImage():
    recognizer = Recognize.Recognize()
    similarExists = None
    for i in dbImages:
        
        similarExists = recognizer.verifyFace(imgpath, i)
        if(len(similarImages) == 1):
            global relativeImage
            relativeImage = ImageTk.PhotoImage(Img.open(i))
            time.sleep(0.1)
            comparingSection.configure(image=relativeImage)
    
        if similarExists:
            similarImages.append(similarExists) 
        
    
   

thread = threading.Thread(target=changeImage)
thread.start()



def on_closing():
    root.destroy()
    thread._stop()
    

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()