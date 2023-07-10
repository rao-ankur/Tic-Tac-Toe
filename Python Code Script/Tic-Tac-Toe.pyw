#importing required GUI Libraries
from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
root=Tk()
root.title("Tic Tac Toe")

# code to implement background image
photo1 =Image.open("earth.png")
r_p=photo1.resize((1600,1200),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(r_p)
label=Label(root,image=photo,width=600,height=400)
label.place(x=0,y=0,relwidth=1,relheight=1)

# function to freeze all buttons
def freeze_button():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

temp = 0
c=0
def response(b):
    global temp,c,t2,t1

    # Message box text
    if n1.get()=="":
        px="Congratulations X Won"
    else:
        px="Congratulations " + n1.get() + ", You Won"

    if n2.get()=="":
        py="Congratulations O Won"
    else:
        py="Congratulations " + n2.get() + ", You Won"

    # Replace the blank button with X or O when Clicked
    if b["text"]==" " and temp==0:
        b["text"]="X"
        c+=1
        temp=1
    elif b["text"]==" " and temp==1:
        b["text"]="O"
        c+=1
        temp=0
    else:
        messagebox.showerror("Tic Tac Toe","Sorry This Box is Already Filled \nPlease, Click On Other Box")

    # Logic of winning the game
    t=0
    if b1["text"]==b2["text"]==b3["text"]=="X" :
        b1.configure(bg="light green")
        b2.configure(bg="light green")
        b3.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",px)

    elif b4["text"]==b5["text"]==b6["text"]=="X" :
        b4.configure(bg="light green")
        b5.configure(bg="light green")
        b6.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",px)

    elif b7["text"]==b8["text"]==b9["text"]=="X" :
        b7.configure(bg="light green")
        b8.configure(bg="light green")
        b9.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",px)

    elif b1["text"]==b4["text"]==b7["text"]=="X" :
        b1.configure(bg="light green")
        b4.configure(bg="light green")
        b7.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",px)

    elif b2["text"]==b5["text"]==b8["text"]=="X" :
        b2.configure(bg="light green")
        b5.configure(bg="light green")
        b8.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",px)

    elif b3["text"]==b6["text"]==b9["text"]=="X" :
        b3.configure(bg="light green")
        b6.configure(bg="light green")
        b9.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",px)

    elif b1["text"]==b5["text"]==b9["text"]=="X" :
        b1.configure(bg="light green")
        b5.configure(bg="light green")
        b9.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",px)

    elif b3["text"]==b5["text"]==b7["text"]=="X" :
        b3.configure(bg="light green")
        b5.configure(bg="light green")
        b7.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",px)

    elif b1["text"]==b2["text"]==b3["text"]=="O" :
        b1.configure(bg="light green")
        b2.configure(bg="light green")
        b3.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",py)

    elif b4["text"]==b5["text"]==b6["text"]=="O" :
        b4.configure(bg="light green")
        b5.configure(bg="light green")
        b6.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",py)

    elif b7["text"]==b8["text"]==b9["text"]=="O" :
        b7.configure(bg="light green")
        b8.configure(bg="light green")
        b9.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",py)

    elif b1["text"]==b4["text"]==b7["text"]=="O" :
        b1.configure(bg="light green")
        b4.configure(bg="light green")
        b7.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",py)

    elif b2["text"]==b5["text"]==b8["text"]=="O" :
        b2.configure(bg="light green")
        b5.configure(bg="light green")
        b8.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",py)

    elif b3["text"]==b6["text"]==b9["text"]=="O" :
        b3.configure(bg="light green")
        b6.configure(bg="light green")
        b9.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",py)

    elif b1["text"]==b5["text"]==b9["text"]=="O" :
        b1.configure(bg="light green")
        b5.configure(bg="light green")
        b9.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",py)

    elif b3["text"]==b5["text"]==b7["text"]=="O" :
        b3.configure(bg="light green")
        b5.configure(bg="light green")
        b7.configure(bg="light green")
        freeze_button()
        t+=1
        messagebox.showinfo("Tic Tac Toe",py)

    if c==9 and t==0:
        freeze_button()
        messagebox.showinfo("Tic Tac Toe","Game Draw")

    
    if temp==0:
        t1.config(text="'X' Turn")
        t2.config(text="'X' Turn")
    elif temp==1:
        t1.config(text="'O' Turn")
        t2.config(text="'O' Turn")

# function to play again the game
def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global temp,c
    global n1,n2
    global t1,t2
    p1=StringVar
    p2=StringVar

    t1=Label(root,fg="blue",text="'X' Turn",font=("helvetica bold",20),width=8,height=1)
    t1.grid(row=2,column=1)

    t2=Label(root,fg="blue",text="'X' Turn",font=("helvetica bold",20),width=8,height=1)
    t2.grid(row=2,column=3)
    
    l1=Label(root,fg="blue",text="Player1 'X'",font=("helvetica bold",20),width=8,height=1)
    l1.grid(row=0,column=1)

    n1=Entry(root,fg="black", textvariable=p1, bd=10, width=42)
    n1.grid(row=0,column=2,columnspan=4)

    l2=Label(root,fg="blue",text="Player2 'O'",font=("helvetica bold",20),width=8,height=1)
    l2.grid(row=1,column=1,rowspan=1)

    n2=Entry(root,fg="black", textvariable=p2, bd=10, width=42)
    n2.grid(row=1,column=2,columnspan=4)

    
    temp=0;c=0

    # Creating Buttons 
    b1=Button(root, fg="black",text= " ",font=("Bold",20),width=8,height=4 , command=lambda:response(b1))
    b2=Button(root, fg="black",text= " ",font=("Bold",20),width=8,height=4 , command=lambda:response(b2))
    b3=Button(root, fg="black",text= " ",font=("Bold",20),width=8,height=4 , command=lambda:response(b3))
    b4=Button(root, fg="black",text= " ",font=("Bold",20),width=8,height=4 , command=lambda:response(b4))
    b5=Button(root, fg="black",text= " ",font=("Bold",20),width=8,height=4 , command=lambda:response(b5))
    b6=Button(root, fg="black",text= " ",font=("Bold",20),width=8,height=4 , command=lambda:response(b6))
    b7=Button(root, fg="black",text= " ",font=("Bold",20),width=8,height=4 , command=lambda:response(b7))
    b8=Button(root, fg="black",text= " ",font=("Bold",20),width=8,height=4 , command=lambda:response(b8))
    b9=Button(root, fg="black",text= " ",font=("Bold",20),width=8,height=4 , command=lambda:response(b9))

    # Creating Grid of Boxes
    b1.grid(row=3,column=1)
    b2.grid(row=3,column=2)
    b3.grid(row=3,column=3)
    b4.grid(row=4,column=1)
    b5.grid(row=4,column=2)
    b6.grid(row=4,column=3)
    b7.grid(row=5,column=1)
    b8.grid(row=5,column=2)
    b9.grid(row=5,column=3)

reset()

# Creating Play Again Button
restart_b=Button(root, fg="red",text= "Play Again",font=("Bold",20),width=8,height=1, command= reset)
restart_b.grid(row=2,column=2)
root.mainloop()