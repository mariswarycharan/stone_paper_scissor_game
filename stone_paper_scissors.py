from itertools import count
from logging import root
from secrets import choice
from tkinter import *
import random
from tkinter.font import BOLD, ITALIC
from unittest import result




root = Tk()

# to give title for this window

root.title("Stone Paper Scissors")
root.configure(background="#33ccff")



l1 = Label(root,padx=20,pady=10,background="#33ccff")
l1.grid(row=1,column=1)

l2= Label(root,padx=20,pady=10,background="#33ccff")
l2.grid(row=1,column=2)


title = Label(root,text="Stone Paper Scissors",font = ("ALGERIAN",40,BOLD), foreground="red",background="black",padx=80,pady=5)
title.grid(row=1,column=3)

b1 = Label(root,padx=50,pady=5,text="computer",font = ("ALGERIAN",20), foreground="red",background="black")
b1.grid(row=2,column=1)

l3 = Label(root,padx=20,pady=5,background="#33ccff")
l3.grid(row=2,column=2)

l4 = Label(root,padx=20,pady=5,background="#33ccff")
l4.grid(row=2,column=3)

l5 = Label(root,padx=20,pady=5,background="#33ccff")
l5.grid(row=2,column=4)



b2 = Label(root,padx=40,pady=5,text="player_1",font = ("ALGERIAN",20), foreground="red",background="black")
b2.grid(row=2,column=5)

photo1 = PhotoImage(file="E:\\Pravin - Photos\\stone1.png")

label1 = Label(root,background="#33ccff")
label1.grid(row=3,column=1)

photo2 = PhotoImage(file="E:\\Pravin - Photos\\paper1.png")

photo3 = PhotoImage(file="E:\\Pravin - Photos\\sciccors1.png")

photo4 = PhotoImage(file="E:\\Pravin - Photos\\stone1.png")

label = Label(root,background="#33ccff")
label.grid(row=3,column=5)

photo5 = PhotoImage(file="E:\\Pravin - Photos\\paper1.png")
photo6 = PhotoImage(file="E:\\Pravin - Photos\\sciccors1.png")

statement_computer = 0
statement_player = 0

def stone():
    
    r = 1
    p = 2
    s = 3
    
    
    a = random.randint(1,3)
    if a == 1:
        label1.config(image = photo1)
        
    if a == 2:
        label1.config(image = photo2)
    
    if a == 3:
           label1.config(image = photo3)
           
    if r == a:
        result.config(text="draw")
        
        
    if p == a:
        result.config(text="you loss")
        global statement_computer
        statement_computer += 1
        count_computer.config(text=statement_computer,font = ("ALGERIAN",20,BOLD,ITALIC), foreground="red")
        
    if s == a:
        
        result.config(text="you win")
        global statement_player
        statement_player += 1
        count_player.config(text=statement_player,font = ("ALGERIAN",20,BOLD,ITALIC), foreground="red")     
    
            
                
    
    label.config(image = photo4)
    
def paper():
    r = 1
    p = 2
    s = 3
    
    a = random.randint(1,3)
    if a == 1:
        label1.config(image = photo1)
        
    if a == 2:
        label1.config(image = photo2)
    
    if a == 3:
        label1.config(image = photo3)
    
    
    label.config(image = photo5)
    
    # for draw if a is paper , p is paper
    if p == a:
        result.config(text="draw")
        
    # win if a is stone, r is paper
    
    if r == a:
        result.config(text="you win")
        global statement_player
        statement_player += 1
        count_player.config(text=statement_player,font = ("ALGERIAN",20,BOLD,ITALIC), foreground="red")
           
    # loss if a is scissors ,s is paper
      
    if s == a:
        result.config(text=" you loss")
        global statement_computer
        statement_computer += 1
        
        count_computer.config(text=statement_computer,font = ("ALGERIAN",20,BOLD,ITALIC), foreground="red")
    
    
    
def scissors():
    r = 1
    p = 2
    s = 3
     
    a = random.randint(1,3)
    if a == 1:
        label1.config(image = photo1)
        
    if a == 2:
        label1.config(image = photo2)
    
    if a == 3:
           label1.config(image = photo3)
           
            
    label.config(image = photo6)
    
    if s == a:
        result.config(text="draw")
        
    if r == a:
        result.config(text="you loss")
        global statement_computer
        statement_computer += 1
        count_computer.config(text=statement_computer,font = ("ALGERIAN",20,BOLD,ITALIC), foreground="red")
             
    if p == a:
        result.config(text="you win")
        global statement_player
        statement_player += 1
        count_player.config(text=statement_player,font = ("ALGERIAN",20,BOLD,ITALIC), foreground="red")       
    
    

  
button1=Button(root,text="stone" ,font = ("ALGERIAN",20,BOLD,ITALIC), foreground="red",background="#33ff33",padx=100,pady=5,command=stone)
button1.grid(row=5,column=3)

button2=Button(root,text="paper" ,font = ("ALGERIAN",20,BOLD,ITALIC), foreground="red",background="#33ff33",padx=100,pady=5,command=paper)
button2.grid(row=6,column=3)

button3=Button(root,text="scissors" ,font = ("ALGERIAN",20,BOLD,ITALIC), foreground="red",background="#33ff33", padx=85,pady=5,command=scissors)
button3.grid(row=7,column=3)
    
vs_image = PhotoImage(file="E:\\Pravin - Photos\\vs.png")

label_vs = Label(root,image=vs_image)
label_vs.grid(row=3,column=3)

count_computer = Label(root,text="computer no of win ",font = ("ALGERIAN",20,ITALIC), foreground="red",background="yellow")
count_computer.grid(row=4,column=1)

count_player = Label(root,text="player no of win",font = ("ALGERIAN",20,ITALIC), foreground="red",background="yellow")
count_player.grid(row=4,column=5)

count_computer = Label(root,background="#33ccff")
count_computer.grid(row=5,column=1)

count_player = Label(root,background="#33ccff")
count_player.grid(row=5,column=5)

# result = Label(root,background="#33ccff")
# result.grid(row=8,column=3)

result = Label(root,padx=100,pady=10,font = ("ALGERIAN",30,ITALIC), foreground="red",background="#33ccff")
result.grid(row=9,column=3)

l6 = Label(root,padx=50,font =  ("ALGERIAN",30,ITALIC), text="Result:",foreground="yellow",background="#33ccff")
l6.grid(row=9,column=1)




root.mainloop()
