from Tkinter import *
import Tkinter as tk
import tkFont
q = 0
s = -1
count = 0
correct = 0
incorrect = 0
question = ["Answer is 1","Answer is 2","Answer is 3","Answer is 4"]
answer = [1,2,3,4]
root = Tk()
fnt=tkFont.Font(family="Helvetica",size=12)
name = tk.Label(root,text = "GUI Quiz",font=fnt)
name.pack()
label = tk.Label(root,text = question[0],font=fnt)
label.pack()
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
rad.pack()
rad2.pack()
rad3.pack()
rad4.pack()
button = tk.Button(root,text = "Next",command = lambda:out(corr.get()),font=fnt)
button.pack()
button_two = tk.Button(root,text = "Restart",command = stop,font=fnt)
button_two.pack()
root.geometry("400x400")
root.mainloop()