from tkinter import*
form = Tk()
form.geometry("700x500")
v = IntVar()

rdm = Radiobutton(form , text = "male",value =1,variable =v)
rdm.pack()
drf = Radiobutton(form ,text = "female",value =0,variable =v)
drf.pack()
def f ():
    print(v.get())
Button(form ,text ="OK",command = f).pack()

form.mainloop()
