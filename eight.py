# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk(className ="Eigth") #add a root window named Myfirst GUI
foo = Label(root,text='''If your forehead is fiery with fever, you could reach for acetaminophen (Tylenol) or ibuprofen (Advil) to lower your temperature. (Don’t treat fevers with aspirin in anyone under the age of 19; doing so can trigger a potentially fatal disease called Reye’s syndrome.) But if your fever is 38.3°C (101°F) or below, don’t be afraid to let it run its course; Mother Nature has raised your temperature for a reason. If you’re uncom­fortable, though, and you want to take action, try these tips to tame the fires within.
Cool your fever
• Take a bath in lukewarm water. This temperature will feel plenty cool when you have a fever, and the bath should help bring your body temperature down. Don’t try to bring a fever down rapidly by plunging yourself into cold water; that tactic sends blood rushing to internal organs, which is how your body defends itself from cold. Your interior actually warms up instead of cooling down.
• Give yourself a sponge bath. Sponging high-heat areas like your armpits and groin with cool water can help reduce your temperature as the water evaporates.
• When you’re not bathing, place cold, damp washcloths on your forehead and the back of your neck.

A remedy that cools your whole body
• An old folk remedy for treating a fever is to soak a sheet in cold water and wrap yourself in it. Today, doctors advise against lowering your body temperature too quickly, so if you try this remedy, use slightly cool, not cold, water. Cover the wet sheet with a large beach towel or blanket, then lie down for about 15 minutes. Unwrap yourself when the wet sheet starts to get warm.
Hydrate to beat fever
• When you have a fever, it’s easy to become dehydrated. Drink 8 to 12 glasses of water a day or enough to make your urine pale. A sports drink like Gatorade can also be helpful. It not only replaces fluids lost to dehydration but lost minerals as well.
• Orange juice and other fruit juices rich in vitamin C are good choices, since the vitamin C assists your immune system in fighting off infection.
• Cold grapes provide hydration-and a soothing treat.

''') # add a label to root window
foo.pack()
root.mainloop()
