import tkinter as tk

def show_out():
    num = int(text_input.get())
    output = ''
    
    for i in range (1, 13):
        output += str(num)+' x '+str(i)
        output += ' = '+str(num*i)+'\n'
    output_label.configure(text=output)

real = tk.Tk()
real.title('Multiplication table')
real.minsize(width=400,height=400)

title_label = tk.Label(master=real,text='กรอกเลขแม่สูตรคูณ')
title_label.pack()

text_input = tk.Entry(master=real)
text_input.pack()

title_button = tk.Button(master=real,text='ยืนยัน',command=show_out)
title_button.pack()

output_label = tk.Label(master=real)
output_label.pack()


real.mainloop()