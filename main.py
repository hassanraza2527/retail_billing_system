import smtplib
import tempfile
from tkinter import *
from tkinter import messagebox
import random, os

def clear():
    bathSoapEntry.delete(0,END)
    facecreamEntry.delete(0,END)
    facewashEntry.delete(0,END)
    hairsprayEntry.delete(0,END)
    hairgelEntry.delete(0,END)
    bodylotionEntry.delete(0,END)
    riceEntry.delete(0,END)
    oilEntry.delete(0,END)
    daalEntry.delete(0,END)
    wheatEntry.delete(0,END)
    sugarEntry.delete(0,END)
    teaEntry.delete(0,END)
    stringEntry.delete(0,END)
    pepsiEntry.delete(0,END)
    spriteEntry.delete(0,END)
    dewEntry.delete(0,END)
    frootiEntry.delete(0,END)
    cocacolaEntry.delete(0,END)

    bathSoapEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    facewashEntry.insert(0,0)
    hairsprayEntry.insert(0,0)
    hairgelEntry.insert(0,0)
    bodylotionEntry.insert(0,0)
    riceEntry.insert(0,0)
    oilEntry.insert(0,0)
    daalEntry.insert(0,0)
    wheatEntry.insert(0,0)
    sugarEntry.insert(0,0)
    teaEntry.insert(0,0)
    stringEntry.insert(0,0)
    pepsiEntry.insert(0,0)
    spriteEntry.insert(0,0)
    dewEntry.insert(0,0)
    frootiEntry.insert(0,0)
    cocacolaEntry.insert(0,0)

    grocerytaxEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    cosmetictaxEntry.delete(0,END)
    cosmeticpriceEntry.delete(0,END)
    drinkstaxEntry.delete(0,END)
    drinkspriceEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billNumberEntry.delete(0,END)
    textarea.delete(0,END)

def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            ob.sendmail(senderEntry.get(),recieverEntry.get(),email_textarea.get(1.0,END))
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully send',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','404 Error',parrent=root1)

    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error', 'Bill is Empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('Send Gmail')
        root1.config(bg='gray20')
        root1.resizable(0,0)

        senderFrame=LabelFrame(root1,text='Sender',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)
        senderLabel=Label(senderFrame,text='Sender email',font=('arial',14,'bold'),bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)
        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLabel = Label(senderFrame, text='Password', font=('arial', 14, 'bold'), bg='gray20', fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)
        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(root1, text='Recipient', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)
        recieverLabel = Label(recipientFrame, text='Email Address', font=('arial', 14, 'bold'), bg='gray20', fg='white')
        recieverLabel.grid(row=0, column=0, padx=10, pady=8)
        recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text='Message', font=('arial', 14, 'bold'), bg='gray20', fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)
        email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendButton=Button(root1,text='SEND',font=('arial',14,'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)

        root1.mainloop()
def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')



def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billNumberEntry.get():
            f=open(f'bills/{i}',"r")
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break

    else:
        messagebox.showerror('Error','Invalid bill number')


if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global billnumber
    result = messagebox.askyesno('Confrim', 'Do you Want to save this Bill?')
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f'bills/ {billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success', f'Bill Number {billnumber} is saved successfully')
        billnumber = random.randint(500, 1000)


billnumber = random.randint(500, 1000)


def invoice():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Error', 'Customer Details Are Required')
    elif cosmeticpriceEntry.get() == '' and grocerypriceEntry.get() == '' and drinkspriceEntry.get() == '':
        messagebox.showerror('Error', 'Products Are Not Selected')
    elif cosmeticpriceEntry.get() == '0 RS' and grocerypriceEntry.get() == '0 RS' and drinkspriceEntry.get() == '0 RS':
        messagebox.showerror('Error', 'Products Are Not Selected')
    else:
        textarea.delete(1.0, END)
        textarea.insert(END, '\t\t**Welcome Customer**\n')
        textarea.insert(END, f'\nBill Number: {billnumber}\n')
        textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END, f'\nCustomer Phone Number: {phoneEntry.get()}\n')
        textarea.insert(END, '\n=======================================================\n')
        textarea.insert(END, 'Product\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n=======================================================\n')
        if bathSoapEntry.get() != '0':
            textarea.insert(END, f'Bath Soap\t\t\t{bathSoapEntry.get()}\t\t\t{soapprice}\n')
        if facecreamEntry.get() != '0':
            textarea.insert(END, f'Face Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice}\n')
        if facewashEntry.get() != '0':
            textarea.insert(END, f'Face Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice}\n')
        if hairgelEntry.get() != '0':
            textarea.insert(END, f'Hair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice}\n')
        if hairsprayEntry.get() != '0':
            textarea.insert(END, f'Hair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice}\n')
        if bodylotionEntry.get() != '0':
            textarea.insert(END, f'Body Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice}\n')
        if riceEntry.get() != '0':
            textarea.insert(END, f'Rice\t\t\t{riceEntry.get()}\t\t\t{riceprice}\n')
        if oilEntry.get() != '0':
            textarea.insert(END, f'Oil\t\t\t{oilEntry.get()}\t\t\t{oilprice}\n')
        if daalEntry.get() != '0':
            textarea.insert(END, f'Daal\t\t\t{daalEntry.get()}\t\t\t{daalprice}\n')
        if wheatEntry.get() != '0':
            textarea.insert(END, f'Wheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice}\n')
        if sugarEntry.get() != '0':
            textarea.insert(END, f'Sugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice}\n')
        if teaEntry.get() != '0':
            textarea.insert(END, f'Tea Pack\t\t\t{teaEntry.get()}\t\t\t{teaprice}\n')
        if stringEntry.get() != '0':
            textarea.insert(END, f'String\t\t\t{stringEntry.get()}\t\t\t{stringprice}\n')
        if pepsiEntry.get() != '0':
            textarea.insert(END, f'Pepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice}\n')
        if dewEntry.get() != '0':
            textarea.insert(END, f'Dew\t\t\t{dewEntry.get()}\t\t\t{dewprice}\n')
        if cocacolaEntry.get() != '0':
            textarea.insert(END, f'CocaCola\t\t\t{cocacolaEntry.get()}\t\t\t{cocacolaprice}\n')
        if spriteEntry.get() != '0':
            textarea.insert(END, f'Sprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice}\n')
        if frootiEntry.get() != '0':
            textarea.insert(END, f'Frooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice}\n')
        textarea.insert(END, '\n-------------------------------------------------------\n')
        if cosmetictaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\nCosmetic Tax\t\t\t\t{cosmetictaxEntry.get()}')
        if drinkstaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\nDrinks Tax \t\t\t\t {drinkstaxEntry.get()}')
        if grocerytaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\nGrocery Tax \t\t\t\t {grocerytaxEntry.get()}')
        textarea.insert(END, '\n-------------------------------------------------------\n')
        textarea.insert(END, f'\nTotal Bill \t\t\t\t {totalbill}')
        save_bill()


def total():
    global soapprice, facecreamprice, facewashprice, hairgelprice, hairsprayprice, bodylotionprice
    global riceprice
    global daalprice
    global oilprice
    global wheatprice
    global sugarprice
    global teaprice
    global stringprice
    global pepsiprice
    global dewprice
    global cocacolaprice
    global spriteprice
    global frootiprice
    global totalbill
    try:
        soap_qty = int(bathSoapEntry.get())
        facewash_qty = int(facewashEntry.get())
        facecream_qty = int(facecreamEntry.get())
        hairgel_qty = int(hairgelEntry.get())
        hairspray_qty = int(hairsprayEntry.get())
        bodylotion_qty = int(bodylotionEntry.get())

        soapprice = soap_qty * 110
        facewashprice = facewash_qty * 250
        facecreamprice = facecream_qty * 320
        hairgelprice = hairgel_qty * 130
        hairsprayprice = hairspray_qty * 220
        bodylotionprice = bodylotion_qty * 320
        totalcosmeticprice = (soapprice + facecreamprice + facewashprice +
                              hairsprayprice + hairgelprice + bodylotionprice)
        cosmeticpriceEntry.delete(0, END)
        cosmeticpriceEntry.insert(0, f'{totalcosmeticprice} Rs')
        cosmetictax = round(totalcosmeticprice * 0.12, 3)
        cosmetictaxEntry.delete(0, END)
        cosmetictaxEntry.insert(0, f'{cosmetictax} Rs')
        # print(totalcosmeticprice)

        riceprice = int(riceEntry.get()) * 200
        daalprice = int(daalEntry.get()) * 100
        oilprice = int(oilEntry.get()) * 250
        wheatprice = int(wheatEntry.get()) * 150
        sugarprice = int(sugarEntry.get()) * 185
        teaprice = int(teaEntry.get()) * 240
        # print(riceprice)
        # print(daalprice)
        # print(oilprice)
        # print(wheatprice)
        # print(sugarprice)
        # print(teaprice)
        totalgroceryprice = riceprice + daalprice + oilprice + wheatprice + sugarprice + teaprice
        grocerypriceEntry.delete(0, END)
        grocerypriceEntry.insert(0, f'{totalgroceryprice} Rs')
        grocerytax = round(totalgroceryprice * 0.05, 3)
        grocerytaxEntry.delete(0, END)
        grocerytaxEntry.insert(0, f'{grocerytax} Rs')

        stringprice = int(stringEntry.get()) * 250
        pepsiprice = int(pepsiEntry.get()) * 180
        dewprice = int(dewEntry.get()) * 180
        cocacolaprice = int(cocacolaEntry.get()) * 180
        spriteprice = int(spriteEntry.get()) * 180
        frootiprice = int(frootiEntry.get()) * 150
        totaldrinksprice = stringprice + pepsiprice + dewprice + cocacolaprice + spriteprice + frootiprice
        drinkspriceEntry.delete(0, END)
        drinkspriceEntry.insert(0, f'{totaldrinksprice} Rs')
        drinkstax = round(totaldrinksprice * 0.08, 3)
        drinkstaxEntry.delete(0, END)
        drinkstaxEntry.insert(0, f'{drinkstax} Rs')
        totalbill = totaldrinksprice + totalgroceryprice + totalcosmeticprice + drinkstax + cosmetictax + grocerytax
    except ValueError:
        print("Please enter valid numeric values for quantity.")


root = Tk()
root.title("Retail Billing System")
root.geometry('1270x685')
root.iconbitmap('icons.ico')
headingLabel = Label(root, text='Retail Billing System', font=('times new roman', 30, 'bold'), bg='gray20', fg='gold',
                     bd=12, relief=GROOVE)
headingLabel.pack(fill=X)

customerDetailframe = LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold'), fg='gold', bd=8,
                                 relief=GROOVE, bg='gray20')
customerDetailframe.pack(fill=X)

nameFrame = Label(customerDetailframe, text='Name', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
nameFrame.grid(row=0, column=0, padx=20)
nameEntry = Entry(customerDetailframe, font=('arial', 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)

phoneFrame = Label(customerDetailframe, text='Phone Number', font=('times new roman', 15, 'bold'), fg='white',
                   bg='gray20')
phoneFrame.grid(row=0, column=2, padx=20)
phoneEntry = Entry(customerDetailframe, font=('arial', 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

billNumberFrame = Label(customerDetailframe, text='Bill Number', font=('times new roman', 15, 'bold'), fg='white',
                        bg='gray20')
billNumberFrame.grid(row=0, column=4, padx=20)
billNumberEntry = Entry(customerDetailframe, font=('arial', 15), bd=7, width=18)
billNumberEntry.grid(row=0, column=5, padx=8)

searchButton = Button(customerDetailframe, text='SEARCH', font=('arial', 12, 'bold'), bd=7, width=10,command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)

productFrame = Frame(root)
productFrame.pack()

cosmeticsFrame = LabelFrame(productFrame, text='Cosmetics', font=('times new roman', 15, 'bold'), bg='gray20',
                            fg='gold', bd=8, relief=GROOVE)
cosmeticsFrame.grid(row=0, column=0)

bathSoapLabel = Label(cosmeticsFrame, text='Bath Soap', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
bathSoapLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
bathSoapEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
bathSoapEntry.grid(row=0, column=1, pady=9, padx=10)
bathSoapEntry.insert(0, 0)

facecreamLabel = Label(cosmeticsFrame, text='Face Cream', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
facecreamLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
facecreamEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
facecreamEntry.grid(row=1, column=1, pady=9, padx=10)
facecreamEntry.insert(0, 0)

facewashLabel = Label(cosmeticsFrame, text='Face Wash', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
facewashLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
facewashEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
facewashEntry.grid(row=2, column=1, pady=9, padx=10)
facewashEntry.insert(0, 0)

hairsprayLabel = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
hairsprayLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')
hairsprayEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
hairsprayEntry.grid(row=3, column=1, pady=9, padx=10)
hairsprayEntry.insert(0, 0)

hairgelLabel = Label(cosmeticsFrame, text='Hair Gel', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
hairgelLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')
hairgelEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
hairgelEntry.grid(row=4, column=1, pady=9, padx=10)
hairgelEntry.insert(0, 0)

bodylotionLabel = Label(cosmeticsFrame, text='Body Lotion', font=('times new roman', 15, 'bold'), fg='white',
                        bg='gray20')
bodylotionLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')
bodylotionEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
bodylotionEntry.grid(row=5, column=1, pady=9, padx=10)
bodylotionEntry.insert(0, 0)

groceryFrame = LabelFrame(productFrame, text='Grocery', font=('times new roman', 15, 'bold'), bg='gray20', fg='gold',
                          bd=8, relief=GROOVE)
groceryFrame.grid(row=0, column=1)

riceLabel = Label(groceryFrame, text='Rice', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
riceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
riceEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
riceEntry.grid(row=0, column=1, pady=9, padx=10)
riceEntry.insert(0, 0)

oilLabel = Label(groceryFrame, text='Oil', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
oilLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
oilEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
oilEntry.grid(row=1, column=1, pady=9, padx=10)
oilEntry.insert(0, 0)

daalLabel = Label(groceryFrame, text='Daal', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
daalLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
daalEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
daalEntry.grid(row=2, column=1, pady=9, padx=10)
daalEntry.insert(0, 0)

wheatLabel = Label(groceryFrame, text='Wheat', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
wheatLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')
wheatEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
wheatEntry.grid(row=3, column=1, pady=9, padx=10)
wheatEntry.insert(0, 0)

sugarLabel = Label(groceryFrame, text='Sugar', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
sugarLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')
sugarEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
sugarEntry.grid(row=4, column=1, pady=9, padx=10)
sugarEntry.insert(0, 0)

teaLabel = Label(groceryFrame, text='Tea Pack', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
teaLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')
teaEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
teaEntry.grid(row=5, column=1, pady=9, padx=10)
teaEntry.insert(0, 0)

drinksFrame = LabelFrame(productFrame, text='Cold Drinks', font=('times new roman', 15, 'bold'), bg='gray20', fg='gold',
                         bd=8, relief=GROOVE)
drinksFrame.grid(row=0, column=2)

stringLabel = Label(drinksFrame, text='String', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
stringLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
stringEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
stringEntry.grid(row=0, column=1, pady=9, padx=10)
stringEntry.insert(0, 0)

pepsiLabel = Label(drinksFrame, text='Pepsi', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
pepsiLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
pepsiEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
pepsiEntry.grid(row=1, column=1, pady=9, padx=10)
pepsiEntry.insert(0, 0)

spriteLabel = Label(drinksFrame, text='Sprite', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
spriteLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
spriteEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
spriteEntry.grid(row=2, column=1, pady=9, padx=10)
spriteEntry.insert(0, 0)

dewLabel = Label(drinksFrame, text='Dew', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
dewLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')
dewEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
dewEntry.grid(row=3, column=1, pady=9, padx=10)
dewEntry.insert(0, 0)

frootiLabel = Label(drinksFrame, text='Frooti', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
frootiLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')
frootiEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
frootiEntry.grid(row=4, column=1, pady=9, padx=10)
frootiEntry.insert(0, 0)

cocacolaLabel = Label(drinksFrame, text='Coca Cola', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
cocacolaLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')
cocacolaEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
cocacolaEntry.grid(row=5, column=1, pady=9, padx=10)
cocacolaEntry.insert(0, 0)

billFrame = LabelFrame(productFrame, bd=8, relief=GROOVE)
billFrame.grid(row=0, column=3, padx=10)

billareaLabel = Label(billFrame, text='Bill Area', font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)
billareaLabel.pack(fill=X)
scrollbar = Scrollbar(billFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea = Text(billFrame, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 14, 'bold'), bg='gray20', fg='gold', bd=8,
                           relief=GROOVE)
billmenuFrame.pack()

grocerypriceLabel = Label(billmenuFrame, text='Grocery Price', font=('times new roman', 14, 'bold'), fg='white',
                          bg='gray20')
grocerypriceLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')
grocerypriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
grocerypriceEntry.grid(row=0, column=1, pady=6, padx=10)

cosmeticpriceLabel = Label(billmenuFrame, text='Cosmetic Price', font=('times new roman', 14, 'bold'), fg='white',
                           bg='gray20')
cosmeticpriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')
cosmeticpriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
cosmeticpriceEntry.grid(row=1, column=1, pady=6, padx=10)

drinkspriceLabel = Label(billmenuFrame, text='Cold Drinks Price', font=('times new roman', 14, 'bold'), fg='white',
                         bg='gray20')
drinkspriceLabel.grid(row=2, column=0, pady=6, padx=10, sticky='w')
drinkspriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
drinkspriceEntry.grid(row=2, column=1, pady=6, padx=10)

grocerytaxLabel = Label(billmenuFrame, text='Grocery Tax', font=('times new roman', 14, 'bold'), fg='white',
                        bg='gray20')
grocerytaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky='w')
grocerytaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
grocerytaxEntry.grid(row=0, column=3, pady=6, padx=10)

cosmetictaxLabel = Label(billmenuFrame, text='Cosmetic Tax', font=('times new roman', 14, 'bold'), fg='white',
                         bg='gray20')
cosmetictaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky='w')
cosmetictaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
cosmetictaxEntry.grid(row=1, column=3, pady=6, padx=10)

drinkstaxLabel = Label(billmenuFrame, text='Cold Drinks Tax', font=('times new roman', 14, 'bold'), fg='white',
                       bg='gray20')
drinkstaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky='w')
drinkstaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
drinkstaxEntry.grid(row=2, column=3, pady=6, padx=10)

buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)
totalButton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                     command=total)
totalButton.grid(row=0, column=0, pady=20, padx=5)

billButton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                    command=invoice)
billButton.grid(row=0, column=1, pady=20, padx=5)

emailButton = Button(buttonFrame, text='Email', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,command=send_email)
emailButton.grid(row=0, column=2, pady=20, padx=5)

printButton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,command=print_bill)
printButton.grid(row=0, column=3, pady=20, padx=5)

clearButton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,command=clear)
clearButton.grid(row=0, column=4, pady=20, padx=5)

root.mainloop()
