from tkinter import * #GUI
import sys            #importing system lib
from subprocess import Popen   #calling file
class Window(Frame):


    def __init__(self, master=None):     
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("Smart Emotion & Gesture detection")
        self.pack(fill=BOTH, expand=1)

        StartButton = Button(self, text="Detect Emotions",bg="black",fg="white",font=("Times",16),command=s)
        StartButton.place(x=225, y=150)

        DetectWeapon= Button(self, text="Detect Weapon ",bg="black",fg="white",font=("Times",16),command=detectweapons)
        DetectWeapon.place(x=230, y=200)

        quitButton = Button(self, text="Quit",bg="red",fg="white",font=("Times",16),command=closewindow)
        quitButton.place(x=270, y=300)




        #creating label  
        title = Label(self, font=("Times",30),text = "Smart Emotion & Gesture detection").place(x =10,y = 50)  

root = Tk()

#size of the window
root.geometry("600x400")
def s():
    Popen('python Emotions_Gesture_detector.py') 

def Detectboths():
    root.destroy()
    
def detectweapons():
    Popen('python Weapon_detection_code.py')
    
def closewindow():
    root.destroy()
app = Window(root)

root.mainloop()  

