import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def messageBoxErreurCode():
    messagebox.showerror("error","the code should be formed of 4 distincts digits")

def initialiser():
    global reponse
    global nbr_tour
    l1=[0,1,2,3,4,5,6,7,8,9]
    a1=random.choice(l1)
    l1.remove(a1)
    b1=random.choice(l1)
    l1.remove(b1)
    c1=random.choice(l1)
    l1.remove(c1)
    d1=random.choice(l1)
    l1.remove(d1)
    reponse=str(a1)+str(b1)+str(c1)+str(d1)
    nbr_tour=0
    label_message["text"] = "   "
    label_insert["text"] = "insert the code:"
    label_insert["foreground"]="red"
    label_message["foreground"]="black"
    button_insert.state(["!disabled"])

def inserer():
    global nbr_tour
    try:
        if len(entry_code.get()) != 4:
            raise ValueError("something went wrong")

        if (entry_code.get()[0]==entry_code.get()[1] or
            entry_code.get()[0]==entry_code.get()[2] or
            entry_code.get()[0]==entry_code.get()[3] or
            entry_code.get()[1]==entry_code.get()[2] or
            entry_code.get()[1]==entry_code.get()[3] or
            entry_code.get()[2]==entry_code.get()[3]):
            raise ArithmeticError("no")
        
        if entry_code.get()==reponse:
            label_message["text"]+="True,congrat("+entry_code.get()+")"
            label_message["foreground"]="green"
            button_insert.state(["disabled"])
            label_insert["text"]="congrat,you won in "+str(nbr_tour+1)+" turns"
            label_insert["foreground"]="green"
            
        else:
            counterInPlace=0
            counterNotInPlace=0
            i=0
            while i<4:
                if entry_code.get()[i] in reponse:
                    if i==reponse.index(entry_code.get()[i]):
                        counterInPlace+=1
                    else:
                        counterNotInPlace+=1
                i=i+1
            label_message["text"]+="~code("+entry_code.get()+")\n"+\
                                    str(counterInPlace)+ " true in place\n"+\
                                    str(counterNotInPlace)+ " true not in place"+"\n"
            label_insert["text"]="Re-insert a number:"
            nbr_tour = nbr_tour+1
    except ValueError as e:
        messageBoxErreurCode()

    except ArithmeticError as e:
        messageBoxErreurCode()
        


fenetre_code=Tk()
fenetre_code.title("codeBoBGame")

frame_code=ttk.Frame(fenetre_code)
frame_code.grid()

l=[0,1,2,3,4,5,6,7,8,9]
a=random.choice(l)
l.remove(a)
b=random.choice(l)
l.remove(b)
c=random.choice(l)
l.remove(c)
d=random.choice(l)
l.remove(d)
reponse=str(a)+str(b)+str(c)+str(d)
nbr_tour=0

label_rules=ttk.Label(frame_code,
                      text="we chosed a number of 4 differents digits randomly,"+\
                     "\n"+"we will tell how many digits are true in place,"+\
                     "\n"+"how many true not in place,"+\
                     "\n"+"the other digits will be false and you have to re-insert the code",
                      foreground="blue")
label_rules.grid(row=0,column=0,columnspan=3)

label_insert=ttk.Label(frame_code,text="insert the code:",foreground="red")
label_insert.grid(row=1,column=0,sticky=(W,E))

entry_code=ttk.Entry(frame_code,width=5)
entry_code.grid(row=1,column=1,columnspan=2,sticky=(W,E))

container = ttk.Frame(frame_code)
canvas = Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame,anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

label_message=ttk.Label(scrollable_frame,text="   ")
label_message.grid()

container.grid(row=2,column=1)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

button_insert=ttk.Button(frame_code,text="insert",command=inserer)
button_insert.grid(row=3,column=0,sticky=(W,E))

button_restart=ttk.Button(frame_code,text="restart",command=initialiser)
button_restart.grid(row=3,column=1,sticky=(W,E))

button_quitter=ttk.Button(frame_code,text="quit",command=fenetre_code.destroy)
button_quitter.grid(row=3,column=2,sticky=(W,E))

label_hint=ttk.Label(frame_code,text="hint:scroll up after restarting")
label_hint.grid(row=4,columnspan=3,sticky=(W,E))
fenetre_code.mainloop()