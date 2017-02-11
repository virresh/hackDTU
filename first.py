# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk(className ="First") #add a root window named Myfirst GUI
foo = Label(root,text='''Medanta - The Medicity, Delhi
Address
Sector - 38, Gurgaon,
Haryana 122 001, India
Phone: +91- 124 4141414, +91- 124 4411441
Fax: +91- 124 4834 111

AIIMS (All India Institute of Medical Sciences), New Delhi
Address
Ansari Nagar, New Delhi - 110029
Phone: +91-11-26588500 / 26588700
Call Centre: 18602583010
Fax: +91-11-26588663 / 26588641

Indraprastha Apollo Hospital, New Delhi
Address
Sarita Vihar, Delhi Mathura Road
New Delhi - 110076 (INDIA)
Phone No: + 91 - 11 - 2692 5858 / + 91 - 11 - 2692 5801
Fax No: +91 - 11 - 2682 5563

Asian Heart Institute, Mumbai
Address
G / N Block, Bandra Kurla Complex,
Bandra (E), Mumbai 400 051, Maharashtra, INDIA.
24x7 Assistance: 126126
Outside Mumbai Call on No.: +91-9920155000

Madras Medical Mission, Chennai
Address
4-A, Dr. J. Jayalalitha Nagar,
Mogappair, Chennai - 600 037, India.
Telephone: 91 44 26568000 / 66738000 / 26561801 / 26565961
Emergency Contact: 105911

''') # add a label to root window
foo.pack()
root.mainloop()
