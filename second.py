# -*- coding: utf-8 -*-
from Tkinter import *
root = Tk(className ="Second") #add a root window named Myfirst GUI
foo = Label(root,text='''Taking iron supplement pills and getting enough iron in your food will correct most cases of iron deficiency anemia. You usually take iron pills 1 to 3 times a day. To get the most benefit from the pills, take them with vitamin C (ascorbic acid) pills or orange juice. Vitamin C helps your body absorb more iron.
Most people start to feel better within a few days of beginning treatment. Even though you feel better, you will need to keep taking the pills for several months to build up your iron stores. Sometimes it takes up to 6 months of treatment with iron supplements before iron levels return to normal.
''') # add a label to root window
foo.pack()
root.mainloop()
