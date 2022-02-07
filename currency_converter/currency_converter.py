from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import requests
import json
from PIL import ImageTk,Image

splash_screen=Tk()
splash_screen.title("Welcome")

img = ImageTk.PhotoImage(Image.open("currency.png"))
panel = ttk.Label(splash_screen, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

splash_screen.update()


url = "http://data.fixer.io/api/latest?access_key=d47eed0b9aab3874c3218fa094ddbcf0"
response = requests.request("GET", url)
infoCurrency=json.loads(response.text)

liste_devise=[]
liste_devise.append(infoCurrency["base"])
for rate in infoCurrency["rates"]:
    liste_devise.append(rate)
dictionnaire_equivalent_euro_devise=infoCurrency["rates"]

splash_screen.destroy()

def errorMessageBox():
    messagebox.showerror("error","the two devise cannot be the same")

def choisirDevisePaid(arg):
    try:
        if combobox_devise_recieved_in.get() == combobox_devise_paid_in.get():
            raise ValueError("the two devise cannot be the same")
        paid.set("1 "+combobox_devise_paid_in.get()+" is equal to")
        if combobox_devise_recieved_in.get() != "":
            a=dictionnaire_equivalent_euro_devise[combobox_devise_paid_in.get()]
            b=dictionnaire_equivalent_euro_devise[combobox_devise_recieved_in.get()]
            n=b/a
            resultat.set(str("{0:.6f}".format(n)))
    except:
        errorMessageBox()

def choisirDeviseReceived(arg):
    try:
        if combobox_devise_recieved_in.get() == combobox_devise_paid_in.get():
            raise ValueError("the two devise cannot be the same")
        recieved.set(combobox_devise_recieved_in.get())
        if combobox_devise_paid_in.get() != "":
            a=dictionnaire_equivalent_euro_devise[combobox_devise_paid_in.get()]
            b=dictionnaire_equivalent_euro_devise[combobox_devise_recieved_in.get()]
            n=b/a
            resultat.set(str("{0:.6f}".format(n)))
    except:
        errorMessageBox()

def switch():
    save_paid=paid.get()
    paid.set("1 "+recieved.get()+" is equal to")
    recieved.set(save_paid.split()[1])
    resultat.set(str("{0:.6f}".format(1/float(resultat.get()))))
    

fenetre_convertir=Tk()
fenetre_convertir.title("Convertir")

frame_convertir=ttk.Frame(fenetre_convertir)
frame_convertir.grid()
    
devise_recieved=StringVar()
devise_paid=StringVar()
resultat=StringVar()
paid=StringVar()
recieved=StringVar()

label_text_paid=ttk.Label(frame_convertir,text="Money paid in:")
label_text_paid.grid(row=0,column=0)

combobox_devise_paid_in=ttk.Combobox(frame_convertir,textvariable=devise_paid,
                             values=liste_devise, 
                             stat="readonly")
combobox_devise_paid_in.bind("<<ComboboxSelected>>",choisirDevisePaid) 
combobox_devise_paid_in.grid(row=0,column=1,sticky=(W),padx=5)

label_text_recieved=ttk.Label(frame_convertir,text="Money recieved in:")
label_text_recieved.grid(row=0,column=2,padx=5)

combobox_devise_recieved_in=ttk.Combobox(frame_convertir,textvariable=devise_recieved,
                             values=liste_devise, 
                             stat="readonly")
combobox_devise_recieved_in.bind("<<ComboboxSelected>>",choisirDeviseReceived) 
combobox_devise_recieved_in.grid(row=0,column=3,columnspan=2,sticky=(W))

label_balance=ttk.Label(frame_convertir,text="Balance:")
label_balance.grid(row=1,column=0)

label_paid=ttk.Label(frame_convertir,textvariable=paid)
label_paid.grid(row=1,column=1)

label_equivalent=ttk.Label(frame_convertir,textvariable=resultat)
label_equivalent.grid(row=1,column=3,sticky=(W))

label_received=ttk.Label(frame_convertir,textvariable=recieved)
label_received.grid(row=1,column=4,sticky=(W))

button_switch=ttk.Button(frame_convertir,text="switch",command=switch)
button_switch.grid(row=1,column=5)

fenetre_convertir.mainloop()


