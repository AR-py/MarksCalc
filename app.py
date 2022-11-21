from tkinter import *
from dark_title_bar import *

w = Tk()
w.geometry('450x600')
w.title('Marks')
w.iconbitmap('icon.ico')
w.resizable(False,False)
w.configure(bg= '#222427')
dark_title_bar(w)

l = Label(w, text='Name:', background= '#222427', foreground= 'white')
l.pack(pady=3)
e = Entry(w, background= '#222427', foreground= 'white')
e.pack(pady=7)

l1 = Label(w, text='Subject 1:', background= '#222427', foreground= 'white')
l1.pack(pady=3)
e1 = Entry(w, background= '#222427', foreground= 'white')
e1.pack(pady=7)

l2 = Label(w, text='Subject 2:', background= '#222427', foreground= 'white')
l2.pack(pady=3)
e2 = Entry(w, background= '#222427', foreground= 'white')
e2.pack(pady=7)

l3 = Label(w, text='Subject 3:', background= '#222427', foreground= 'white')
l3.pack(pady=3)
e3 = Entry(w, background= '#222427', foreground= 'white')
e3.pack(pady=7)

l4 = Label(w, text='Subject 4:', background= '#222427', foreground= 'white')
l4.pack(pady=3)
e4 = Entry(w, background= '#222427', foreground= 'white')
e4.pack(pady=7)

l5 = Label(w, text='Subject 5:', background= '#222427', foreground= 'white')
l5.pack(pady=3)
e5 = Entry(w, background= '#222427', foreground= 'white')
e5.pack(pady=7)

l0 = Label(w, text='Total marks', background= '#222427', foreground= 'white')
l0.pack(pady=3)
e0 = Entry(w, background= '#222427', foreground= 'white')
e0.pack(pady=7)

def sub():
    l6.config(text=e.get())
    l7.config(text='Percentage: ' + f'{int(str(e1.get()))+int(str(e2.get()))+int(str(e3.get()))+int(str(e4.get()))+int(str(e5.get()))/int(str(e0.get()))*100}'+'%')

l6 = Label(w, text='', background= '#222427', foreground= 'white')
l6.pack(pady=2)
l7 = Label(w, text='', background= '#222427', foreground= 'white')
l7.pack(pady=2)

btn = Button(w, text='Submit', background= '#222427', foreground= 'white')
btn.pack(pady=3)

w.mainloop()