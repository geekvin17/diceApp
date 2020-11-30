import random
import tkinter
from PIL import Image , ImageTk
import os 
import sys 

root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll a Dice ')


#adding heading labe
HeadingLabel = tkinter.Label(root, text="Party Dice",fg='red',bg='green',font='Helvetica 16 bold italic ')
HeadingLabel.pack() 

#adding  images
dice = ['die1.png', 'die2.png', 'die3.png', 
    'die4.png', 'die5.png', 'die6.png']

#to access application directory path 
dir = os.path.dirname(sys.argv[0])
d = random.choice(dice)
path = dir+"/"+ d
DiceImage = ImageTk.PhotoImage(Image.open(path))

#  label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)

#ImageLabel.image = DiceImage
ImageLabel.pack( expand=True)

#function to roll a dice 
def roll_Dice():
    dir = os.path.dirname(sys.argv[0])
    d = random.choice(dice)
    path = dir+"/"+ d
    DiceImage = ImageTk.PhotoImage(Image.open(path))
    ImageLabel.configure(image=DiceImage)
    ImageLabel.image = DiceImage


# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll', fg='blue', command=roll_Dice)
# pack a widget in the parent widget
button.pack( expand=True)

root.mainloop()
