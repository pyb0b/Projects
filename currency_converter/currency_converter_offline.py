from tkinter import*
from tkinter import ttk
from tkinter import messagebox


liste_devise=['EUR', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL']
dictionnaire_equivalent_euro_devise={'AED': 3.974156, 'AFN': 82.995247, 'ALL': 123.35067, 'AMD': 527.907137, 'ANG': 1.94172, 'AOA': 603.65355, 'ARS': 73.184019, 'AUD': 1.686782, 'AWG': 1.947636, 'AZN': 1.843729, 'BAM': 1.957042, 'BBD': 2.184072, 'BDT': 91.882081, 'BGN': 1.956946, 'BHD': 0.408464, 'BIF': 2066.658054, 'BMD': 1.08202, 'BND': 1.541047, 'BOB': 7.458487, 'BRL': 6.337035, 'BSD': 1.08168, 'BTC': 0.000116, 'BTN': 81.961462, 'BWP': 13.19189, 'BYN': 2.647394, 'BYR': 21207.5905, 'BZD': 2.18047, 'CAD': 1.526736, 'CDF': 1960.620493, 'CHF': 1.051464, 'CLF': 0.032457, 'CLP': 895.592124, 'CNY': 7.684726, 'COP': 4244.439554, 'CRC': 615.436735, 'CUC': 1.08202, 'CUP': 28.673528, 'CVE': 110.528762, 'CZK': 27.714646, 'DJF': 192.297007, 'DKK': 7.454581, 'DOP': 59.839907, 'DZD': 139.534913, 'EGP': 17.021801, 'ERN': 16.230686, 'ETB': 36.529417, 'EUR': 1, 'FJD': 2.43698, 'FKP': 0.893957, 'GBP': 0.893958, 'GEL': 3.467917, 'GGP': 0.893957, 'GHS': 6.259529, 'GIP': 0.893957, 'GMD': 55.728196, 'GNF': 10230.498761, 'GTQ': 8.327632, 'GYD': 226.202141, 'HKD': 8.38678, 'HNL': 27.050882, 'HRK': 7.56228, 'HTG': 114.833163, 'HUF': 354.832247, 'IDR': 16098.725229, 'ILS': 3.828407, 'IMP': 0.893957, 'INR': 82.100469, 'IQD': 1287.603709, 'IRR': 45558.449258, 'ISK': 157.304474, 'JEP': 0.893957, 'JMD': 157.481963, 'JOD': 0.767048, 'JPY': 115.872977, 'KES': 115.858193, 'KGS': 82.866608, 'KHR': 4432.498727, 'KMF': 491.782163, 'KPW': 973.841837, 'KRW': 1334.336564, 'KWD': 0.334565, 'KYD': 0.901466, 'KZT': 455.529934, 'LAK': 9743.589788, 'LBP': 1636.383638, 'LKR': 203.256999, 'LRD': 214.727267, 'LSL': 20.02145, 'LTL': 3.194924, 'LVL': 0.654503, 'LYD': 1.53688, 'MAD': 10.690769, 'MDL': 19.252641, 'MGA': 4127.906383, 'MKD': 61.541056, 'MMK': 1519.816334, 'MNT': 3029.466566, 'MOP': 8.635606, 'MRO': 386.281128, 'MUR': 43.106769, 'MVR': 16.775357, 'MWK': 797.993739, 'MXN': 25.920657, 'MYR': 4.70863, 'MZN': 74.015615, 'NAD': 20.021404, 'NGN': 418.752938, 'NIO': 36.734984, 'NOK': 11.072963, 'NPR': 131.138619, 'NZD': 1.822918, 'OMR': 0.416556, 'PAB': 1.08178, 'PEN': 3.722555, 'PGK': 3.728682, 'PHP': 54.896322, 'PKR': 173.123558, 'PLN': 4.568725, 'PYG': 7102.563158, 'QAR': 3.939676, 'RON': 4.841178, 'RSD': 117.61956, 'RUB': 79.642622, 'RWF': 1014.393678, 'SAR': 4.064993, 'SBD': 9.06027, 'SCR': 17.860804, 'SDG': 59.839682, 'SEK': 10.669694, 'SGD': 1.546288, 'SHP': 0.893957, 'SLL': 10657.896612, 'SOS': 628.653942, 'SRD': 8.069746, 'STD': 23859.289225, 'SVC': 9.465949, 'SYP': 556.564945, 'SZL': 20.021324, 'THB': 34.69501, 'TJS': 11.083838, 'TMT': 3.78707, 'TND': 3.152736, 'TOP': 2.508235, 'TRY': 7.46724, 'TTD': 7.317598, 'TWD': 32.427096, 'TZS': 2503.148824, 'UAH': 28.810075, 'UGX': 4095.335589, 'USD': 1.08202, 'UYU': 47.519861, 'UZS': 10939.221788, 'VEF': 10.806678, 'VND': 25249.475924, 'VUV': 130.258929, 'WST': 3.031637, 'XAF': 656.360352, 'XAG': 0.065002, 'XAU': 0.00062, 'XCD': 2.924213, 'XDR': 0.796189, 'XOF': 656.786453, 'XPF': 119.628517, 'YER': 270.856678, 'ZAR': 20.106517, 'ZMK': 9739.481623, 'ZMW': 19.984573, 'ZWL': 348.410416}

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
