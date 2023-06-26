import Tkinter as Tk 

testapp = Tk.Tk()
testapp.title('mairuu')
testapp.minsize(width=400,height=400)

title_label = Tk.Label(master=testapp,text='mairuu')
title_label.pack()

text_input = Tk.Entry(master=testapp)
text_input.pack()

Button = Tk.Button(master=testapp, text='ยืนยัน')
Button.pack()
testapp.mainloop()