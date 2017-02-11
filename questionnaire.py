import Tkinter as tk
import tkFont

responses = []
q = 0
s = -1
count = 0
correct = 0
incorrect = 0
question = ["Are heart diseases congenital in your family?","Do you have past records of being anaemic?","Are you a regular consumer of alcohol?","Are you a frequent Smoker?","Are you a heavy caffeine consumer? (Colas, Coffee, etc)"
,"Are you under a lot of stress currently?","Are you feeling dizzy or abnormally tired these days?","Are you suffering from very high fever right now?"]
#answer = ["Yes","No","Yes","No","Yes","No","Yes","No","Yes"]
root = tk.Tk()
xVal = 0
fnt=tkFont.Font(family="Helvetica",size=12)
name = tk.Label(root,text = "Health Questionnaire",font=fnt)
name.grid(row=0,column=1)
corr  = tk.IntVar()

rad1 = tk.Radiobutton(root, text="Yes", variable=corr, value=1,font=fnt)
rad2 = tk.Radiobutton(root, text="No", variable=corr, value=0,font=fnt)
button = tk.Button(root,text = "Next",command = lambda:out((corr.get())),font=fnt)
# name.pack()
label = tk.Label(root,text = question[0],font=fnt)
label.grid(row=1,column=1)



def out(par): 
    global responses,xVal
    responses.append(par)
    f(xVal+1)
    xVal+=1
    # print responses
    

def f(xVal):
    if xVal==8 :
        for i in responses:
            print i 
        root.destroy()
        return
    label.config(text = question[xVal])

q = 0
correct = 0
incorrect = 0
rad1.grid(row=2,column=0)
rad2.grid(row=2,column=2)
button.grid(row=3,column=2)

#   global q,correct,incorrect,s,count
#     count = count + 1
#     q=q+1
#     if answer[q-1] == par :
#         correct = correct + 1
#     else:
#         incorrect = incorrect + 1
#     if count>=4:
#         label.config(text = "Correct: "+str(correct) + " Incorrect:   "+str(incorrect) ,font=fnt)
#         return
#     label.config(text = question[q],font=fnt)

# def stop():
    
# button.pack()
# root.geometry("400x400")
root.mainloop()