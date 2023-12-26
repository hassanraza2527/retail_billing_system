from tkinter import *

root=Tk()
root.title("Retail Billing System")
root.geometry('1270x685')
root.iconbitmap('icons.ico')
headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customerDetailframe=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
customerDetailframe.pack(fill=X)

nameFrame=Label(customerDetailframe,text='Name',font=('times new roman',15,'bold'),fg='white',bg='gray20')
nameFrame.grid(row=0,column=0,padx=20)
nameEntry=Entry(customerDetailframe,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneFrame=Label(customerDetailframe,text='Phone Number',font=('times new roman',15,'bold'),fg='white',bg='gray20')
phoneFrame.grid(row=0,column=2,padx=20)
phoneEntry=Entry(customerDetailframe,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billNumberFrame=Label(customerDetailframe,text='Bill Number',font=('times new roman',15,'bold'),fg='white',bg='gray20')
billNumberFrame.grid(row=0,column=4,padx=20)
billNumberEntry=Entry(customerDetailframe,font=('arial',15),bd=7,width=18)
billNumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customerDetailframe,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productFrame=Frame(root)
productFrame.pack()

cosmeticsFrame=LabelFrame(productFrame,text='Cosmetics',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
cosmeticsFrame.grid(row=0,column=0)

bathSoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',15,'bold'),fg='white',bg='gray20')
bathSoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
bathSoapEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathSoapEntry.grid(row=0,column=1,pady=9,padx=10)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),fg='white',bg='gray20')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)

facewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roman',15,'bold'),fg='white',bg='gray20')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)

hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),fg='white',bg='gray20')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),fg='white',bg='gray20')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)

bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),fg='white',bg='gray20')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)

groceryFrame=LabelFrame(productFrame,text='Grocery',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),fg='white',bg='gray20')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)

oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),fg='white',bg='gray20')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)

daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),fg='white',bg='gray20')
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10)

wheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),fg='white',bg='gray20')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
wheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10)

sugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),fg='white',bg='gray20')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10)

teaLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),fg='white',bg='gray20')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10)

drinksFrame=LabelFrame(productFrame,text='Cold Drinks',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
drinksFrame.grid(row=0,column=2)

maazaLabel=Label(drinksFrame,text='Maaza',font=('times new roman',15,'bold'),fg='white',bg='gray20')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
maazaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)

pepsiLabel=Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold'),fg='white',bg='gray20')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
pepsiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)

spriteLabel=Label(drinksFrame,text='Sprite',font=('times new roman',15,'bold'),fg='white',bg='gray20')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
spriteEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)

dewLabel=Label(drinksFrame,text='Dew',font=('times new roman',15,'bold'),fg='white',bg='gray20')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
dewEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
dewEntry.grid(row=3,column=1,pady=9,padx=10)

frootiLabel=Label(drinksFrame,text='Frooti',font=('times new roman',15,'bold'),fg='white',bg='gray20')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
frootiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10)

cocacolaLabel=Label(drinksFrame,text='Coca Cola',font=('times new roman',15,'bold'),fg='white',bg='gray20')
cocacolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
cocacolaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cocacolaEntry.grid(row=5,column=1,pady=9,padx=10)

billFrame=LabelFrame(productFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=10)

billareaLabel=Label(billFrame,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)
scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billFrame,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',14,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
billmenuFrame.pack()

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman',14,'bold'),fg='white',bg='gray20')
grocerypriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')
grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=0,column=1,pady=6,padx=10)

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',14,'bold'),fg='white',bg='gray20')
cosmeticpriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')
cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=1,column=1,pady=6,padx=10)

drinkspriceLabel=Label(billmenuFrame,text='Cold Drinks Price',font=('times new roman',14,'bold'),fg='white',bg='gray20')
drinkspriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')
drinkspriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=6,padx=10)

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',14,'bold'),fg='white',bg='gray20')
grocerytaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')
grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=0,column=3,pady=6,padx=10)

cosmetictaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',14,'bold'),fg='white',bg='gray20')
cosmetictaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')
cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=1,column=3,pady=6,padx=10)

drinkstaxLabel=Label(billmenuFrame,text='Cold Drinks Tax',font=('times new roman',14,'bold'),fg='white',bg='gray20')
drinkstaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')
drinkstaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,pady=6,padx=10)


buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)
totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8)
clearButton.grid(row=0,column=4,pady=20,padx=5)


root.mainloop()