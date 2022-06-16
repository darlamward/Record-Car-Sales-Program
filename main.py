#Experiment File for QAP3
#
#
'''
while True:
    try:
        allowed_char = set("1234567890-")
        InvoiceDate = input("Enter an invoice date(YYYY-MM-DD): ")

    FirstName = input("Enter your first name: ").title()
    LastName = input("Enter your last name: ").title()
    PhoneNum = input("Enter your phone number(10 digits long): ")
    PlateNum = input("Enter the plate number(XXX999): ").upper()
    CarMake = input("Enter the Car Make(Kia): ")
    CarModel = input("Enter the Car Model(Forte): ")
    CarYear = input("Enter the Car's Year(YYYY): ")
    SellingPrice = float(input("Enter the Car's selling price: "))
    TradeInPrice = float(input("Enter the Car's trade in amount: "))
    SalespersonName = input("Enter the salesperson's name: ").title()
    CreditCardNum = input("Enter your Credit Card number(16 digits long): ")
    CreditCardExpDate = input("Enter your Credit Card expiration date(MM/YY): ")


    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXWYZ abcdefghijklmnopqrstuvwxyz,0123456789-.'")
        StAdd = input("Enter your street address: ").title()
        if StAdd == "":
            print("Street address cannot be blank - Please try again. ")
        elif not set(StAdd).issubset(allowed_char):
            print("Street address contains invalid characters - Please try again. ")
        else:
            break
    while True:
        try:
            allowed_char = set(("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz.-'"))
            City = input("Enter the City: ").title()
        except:
            print("City name contains invalid characters - Please re-enter ")
        if City == "":
            print("City name cannot be blank. Please re-enter.")
        elif not set(City).issubset(allowed_char):
            print("City name contains invalid characters - Please re-enter ")
        else:
            break
    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-' ")
        Prov =  input("Please enter name of province: ")
        if not set(Prov).issubset(allowed_char):
            print("Province name contains invalid characters - Please try again. ")
        elif Prov == "":
            print("Province name cannot be blank - Please enter Province name. ")
        else:
            break
    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890")
        PostalCode = input("Please enter your postal code  (A1A1A1): ").capitalize()
        if not set(PostalCode).issubset(allowed_char):
            print("Postal Code contains invalid characters - Please Re-enter.")
        elif PostalCode == "":
            print("Postal code cannot be blank - Please enter postal code. ")
        else:
            break
'''
# How to make a text file that you keep adding to.
'''
f = open("recipe.txt", "a")
f.write("\nsandwitch3")
f.close()
'''
'''
        if Choice == Choice:
            Years = Choice
            New_Price = SellPrice - TradeIn
            Payments = 12 * Choice
            FinanceFee = Years * TransferFee
            New_Price += FinanceFee
            Mon_Pay = New_Price / Payments
            Fin_FeeDsp = "${:,.2f}".format(TransferFee * Choice)
            New_PriceDsp = "${:,.2f}".format(New_Price)
            Mon_PayDsp = "${:,.2f}".format(Mon_Pay)
        if SellPrice <= 5000.00:
            LicFee = LIC_FEE75
        elif SellPrice > 5000.00:
            LicFee = LIC_FEE165
        if SellPrice <= 20000.00:
            Trans_Fee = TRANS_FEE_STD * SellPrice
        elif SellPrice > 20000.00:
            Trans_Fee = TRANS_FEE_LUX * SellPrice
        else:
            break

import datetime

date = datetime.datetime.now() + datetime.timedelta(30)
date = date.strftime("%d-%b-%y").upper()
print(date)
'''

import datetime

StDate = input("Enter the start date (yyyy-mm-dd): ")
StDate = datetime.datetime.strptime(StDate, "%Y-%m-%d")
#StDate = StDate.strftime("%d").upper()
year = StDate.strftime("%y")
month = StDate.strftime("%m")
#print(StDate)
print(year)
print(month)

