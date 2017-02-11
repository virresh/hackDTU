# from Tkinter import *
import Tkinter as tk
import tkFont
q = 0
s = -1
count = 0
correct = 0
incorrect = 0
question = ["Answer is 1","Answer is 2","Answer is 3","Answer is 4"]
answer = [1,2,3,4]
root = tk.Tk()
fnt=tkFont.Font(family="Helvetica",size=12)
name = tk.Label(root,text = "GUI Quiz",font=fnt)
name.grid(row=0,column=1)
label = tk.Label(root,text = question[0],font=fnt)
label.grid(row=1,column=1)

def out(par):
    global q,correct,incorrect,s,count
    count = count + 1
    q=q+1
    if answer[q-1] == par :
        correct = correct + 1
    else:
        incorrect = incorrect + 1
    if count>=4:
        label.config(text = "Correct: "+str(correct) + " Incorrect:   "+str(incorrect) ,font=fnt)
        return
    label.config(text = question[q],font=fnt)
def stop():
    global q,correct,incorrect
    q = 0
    correct = 0
    incorrect = 0
    label.config(text = question[0])
corr  = tk.IntVar()
rad = tk.Radiobutton(root, text='First Option', variable=corr, value=1,font=fnt)
rad2 = tk.Radiobutton(root, text='Second', variable=corr, value=2,font=fnt)
rad3=tk.Radiobutton(root, text='Third', variable=corr, value=3,font=fnt)
rad4=tk.Radiobutton(root, text='Fourth', variable=corr, value=4,font=fnt)
rad.grid(row=2,column=0)
rad2.grid(row=2,column=1)
rad3.grid(row=2,column=2)
rad4.grid(row=2,column=3)
button = tk.Button(root,text = "Next",command = lambda:out((corr.get())%4),font=fnt)
button.grid(row=3,column=2)
button_two = tk.Button(root,text = "Restart",command = stop,font=fnt)
button_two.grid(row=3,column=1)
# root.geometry("400x400")
root.mainloop()