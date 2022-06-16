# A program to keep track of Honest Harry's used car sales. Shows payment options and a receipt.
# Completed by: Darla Ward
# Date Completed: 06-15-2022
"""
Note: I made the program to work without the invoice date having to be the current date. For example, you can have the
invoice date be 1990-06-18 and the calculations will be done around that date. The first payment date will be 1990-JUL-18
and the expiry date for the credit card will need to be valid within 4 years of 1990. Therefore, this program can record
all used cars sales; previous(year 1900+), present and future. It does not need to be a current date in order for this
program to work.
"""

import datetime

LIC_FEE75 = 75.00
LIC_FEE165 = 165.00
HST_RATE = .15
TRANSFER_FEE_RATE = 0.01
LUXURY_TAX = 0.016
YEARLY_FINANCE_FEE = 39.99

FIN_FEE = 39.99
FIN_FEE2 = FIN_FEE * 2
FIN_FEE3 = FIN_FEE * 3
FIN_FEE4 = FIN_FEE * 4

FIN_OPT1 = "1"
FIN_OPT2 = "2"
FIN_OPT3 = "3"
FIN_OPT4 = "4"

FIN_MON12 = 12
FIN_MON24 = 24
FIN_MON36 = 36
FIN_MON48 = 48

PAYMENT1 = 12
PAYMENT2 = 24
PAYMENT3 = 36
PAYMENT4 = 48

YEAR1 = 1
YEAR2 = 2
YEAR3 = 3
YEAR4 = 4

while True:
    while True:
        try:
            allowed_char = set("1234567890-")
            InvoiceDate = input("Please enter the date(YYYY-MM-DD): ")
            InvoiceDate = datetime.datetime.strptime(InvoiceDate, "%Y-%m-%d")
        except:
            print("Date format is not a valid format. Please re-enter. ")
        else:
            break
    while True:
        try:
            allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz-'")
            FirstName = input("Please enter your first name: ").title()
        except FirstName == "":
            print("Name cannot be blank. Please enter your name. ")
        if not set(FirstName).issubset(allowed_char):
            print("Customers name cannot contain invalid characters. Please re-enter. ")
        else:
            break
    while True:
        try:
            allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
            LastName = input("Please enter your last name: ").title()
        except LastName == "":
            print("Name cannot be blank. Please enter your name. ")
        if not set(LastName).issubset(allowed_char):
            print("Customers name cannot contain invalid characters. Please re-enter. ")
        else:
            break
    while True:
        PhoneNum = input("Please enter your phone number(10 digits including area code): ")
        if not PhoneNum.isdigit():
            print("Phone numbers cannot contain invalid characters. Please re-enter.")
        if len(PhoneNum) != 10:
            print("Phone number must include area code and should be 10 digits. Please re-enter.")
        else:
            break
    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")
        LicPlate = input("Enter the licence plate number(LLL000): ").capitalize()
        if not set(LicPlate).issubset(allowed_char):
            print("Licence plate number contains invalid characters. Please re-enter: ")
        elif LicPlate == "":
            print("Licence plate number cannot be blank. Please re-enter.")
        elif len(LicPlate) != 6:
            print("Licence plate must be 6 characters. Please re-enter.")
        elif not LicPlate[0:3].isalpha():
            print("Licence plate number must start with 3 letters. Please re-enter.")
        elif not LicPlate[3:6].isdigit():
            print("Licence plate number must end with 3 numbers. Please re-enter.")
        else:
            break
    while True:
        try:
            allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz.,-")
            VehicleMake = input("Enter the make of the vehicle(Kia, Dodge, Ford, etc.): ").title()
        except:
            print("Vehicle make contains invalid characters. Please re-enter.")
        if not set(VehicleMake).issubset(allowed_char):
            print("Vehicle make contains invalid characters. Please re-enter.")
        if VehicleMake == "":
            print("Vehicle make cannot be blank. Please enter the vehicle make.")
        else:
            break
    while True:
        try:
            allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz,'.-")
            VehicleModel = input("Enter the vehicle model(Escape, Rio, Camry, etc.): ").title()
        except:
            print("Vehicle model contains invalid characters. Please re-enter. ")
        if VehicleModel == "":
            print("Vehicle model cannot be blank. Please re-enter.")
        elif not set(VehicleMake).issubset(allowed_char):
            print("Vehicle model contains invalid characters. Please re-enter.")
        else:
            break
    while True:
        allowed_char = set("1234567890")
        VehicleYear = int(input("Enter the year of the vehicle(YYYY): "))
        year = InvoiceDate.strftime("%Y")
        if int(VehicleYear) == "":
            print("Vehicle year cannot be blank. Please enter the vehicle year. ")
        elif int(VehicleYear) < 1900 or VehicleYear > (int(year) + 1):
            print("Please enter a valid year. ")
        elif not set(str(VehicleYear)).issubset(allowed_char):
            print("Vehicle year contains invalid characters. Please re-enter.")
        else:
            break
    while True:
        allowed_char = set("1234567890.")
        SellPrice = input("Enter the sell price of the vehicle(less than $50000.00): ")
        if SellPrice == "":
            print("Sell price cannot be blank. Please re-enter the sell price: ")
        elif not set(SellPrice).issubset(allowed_char):
            print("Sell price contains invalid characters. Please re-enter. ")
        elif float(SellPrice) > 50000:
            print("Sell price cannot be greater than $50,000.00. Please re-enter.")
        elif float(SellPrice) < 0:
            print("Sell price cannot be less than $0.00. Please re-enter.")
        else:
            break
    while True:
        allowed_char = set("1234567890.")
        TradeIn = input("Enter the trade-in value of the vehicle(Trade-in value must be less than the sell price): ")
        if TradeIn == "":
            print("Trade-in value cannot be blank. Please re-enter the trade-in value. ")
        elif float(TradeIn) > float(SellPrice):
            print("Trade-in value must be less than the sell price. Please re-enter.")
        else:
            break
    while True:
        try:
            allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz,-.'")
            SalesPerson = input("Enter the salespersons name: ").title()
        except:
            print("Salesperson's name cannot contain invalid characters. Please re-enter.")
        if SalesPerson == "":
            print("Salesperson's name cannot be blank. Please enter salesperson's name. ")
        elif not set(SalesPerson).issubset(allowed_char):
            print("Salesperson's name cannot contain invalid characters. Please re-enter. ")
        else:
            break
    while True:
        allowed_char = set("1234567890")
        CreditNum = input("Please enter the credit card number(16 digits without dashes or spaces): ")
        if len(CreditNum) > 16 or len(CreditNum) < 16:
            print("Credit card number must be 16 digits long. Please re-enter:")
        elif not set(CreditNum).issubset(allowed_char):
            print("Credit card number cannot contain invalid characters. Please re-enter:")
        else:
            break
    while True:
        Expiry = input("Enter Credit Card Expiry Date (MM/YY):")
        year = InvoiceDate.strftime("%y")
        month = InvoiceDate.strftime("%m")
        if len(Expiry) > 5:
            print("Date is too long. Please re-enter.")
        elif Expiry[2] != "/":
            print("Date needs to be format MM/YY. Please re-enter.")
        elif int(Expiry[0:2]) < 1 or int(Expiry[0:2]) > 12:
            print("Not a valid month. Month needs to be between 01 and 12. Please re-enter.")
        elif int(Expiry[3:5]) < int(year) or int(Expiry[3:5]) > (int(year) + 4):
            print("Not a valid year. Year must be within 4 years of the invoice date year. Please re-enter.")
        elif int(Expiry[0:2]) < int(month) and int(Expiry[3:5]) == int(year):
            print("Not a valid credit card. Please re-enter.")
        else:
            break

    PriceAfterTrade = float(SellPrice) - float(TradeIn)
    Taxes = float(SellPrice) * HST_RATE
    if float(SellPrice) > 5000:
        LicenseFee = 165.00
    else:
        LicenseFee = 75.00
    if float(SellPrice) < 20000:
        TransferFee = float(SellPrice) * TRANSFER_FEE_RATE
    else:
        TransferFee = (float(SellPrice) * TRANSFER_FEE_RATE) + (float(SellPrice) * LUXURY_TAX)
    TotalSalesPrice = PriceAfterTrade + Taxes + LicenseFee + TransferFee

    TotalSalesPrice1 = TotalSalesPrice + FIN_FEE
    TotalSalesPrice2 = TotalSalesPrice + FIN_FEE2
    TotalSalesPrice3 = TotalSalesPrice + FIN_FEE3
    TotalSalesPrice4 = TotalSalesPrice + FIN_FEE4
    MonthlyPay1 = TotalSalesPrice1 / FIN_MON12
    MonthlyPay2 = TotalSalesPrice2 / FIN_MON24
    MonthlyPay3 = TotalSalesPrice3 / FIN_MON36
    MonthlyPay4 = TotalSalesPrice4 / FIN_MON48

    print()
    print("# Years         # Payments          Financing Fee               Total Price             Monthly Payment")
    print("-------------------------------------------------------------------------------------------------------")
    print("{:>4} {:>18}                ${:>7,.2f}                 ${:>10,.2f}                  ${:>9,.2f}".format(YEAR1,
                                                                                                                  PAYMENT1,
                                                                                                                  FIN_FEE,
                                                                                                                  TotalSalesPrice1,
                                                                                                                  MonthlyPay1))
    print("{:>4} {:>18}                ${:>7,.2f}                 ${:>10,.2f}                  ${:>9,.2f}".format(YEAR2,
                                                                                                                  PAYMENT2,
                                                                                                                  FIN_FEE2,
                                                                                                                  TotalSalesPrice2,
                                                                                                                  MonthlyPay2))
    print("{:>4} {:>18}                ${:>7,.2f}                 ${:>10,.2f}                  ${:>9,.2f}".format(YEAR3,
                                                                                                                  PAYMENT3,
                                                                                                                  FIN_FEE3,
                                                                                                                  TotalSalesPrice3,
                                                                                                                  MonthlyPay3))
    print("{:>4} {:>18}                ${:>7,.2f}                 ${:>10,.2f}                  ${:>9,.2f}".format(YEAR4,
                                                                                                                  PAYMENT4,
                                                                                                                  FIN_FEE4,
                                                                                                                  TotalSalesPrice4,
                                                                                                                  MonthlyPay4))

    print()

    while True:
        print()
        Choice = int(input("Enter the payment schedule you want to follow(1-4): "))
        print()
        if Choice == 1:
            MonthlyPay = MonthlyPay1
            TotalSalesPrice = TotalSalesPrice1
            Payments = PAYMENT1
            break
        elif Choice == 2:
            MonthlyPay = MonthlyPay2
            TotalSalesPrice = TotalSalesPrice2
            Payments = PAYMENT2
            break
        elif Choice == 3:
            MonthlyPay = MonthlyPay3
            TotalSalesPrice = TotalSalesPrice3
            Payments = PAYMENT3
            break
        elif Choice == 4:
            MonthlyPay = MonthlyPay4
            TotalSalesPrice = TotalSalesPrice4
            Payments = PAYMENT4
            break
        else:
            print("Not a valid payment schedule. Please re-enter.")
    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXWYZ abcdefghijklmnopqrstuvwxyz,0123456789-.'")
        StAdd = input("Enter your street address: ").title()
        if StAdd == "":
            print("Street address cannot be blank. Please re-enter. ")
        elif not set(StAdd).issubset(allowed_char):
            print("Street address contains invalid characters. Please re-enter. ")
        else:
            break
    while True:
        try:
            allowed_char = set(("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz.-'"))
            City = input("Enter the City: ").title()
        except:
            print("City name contains invalid characters. Please re-enter. ")
        if City == "":
            print("City name cannot be blank. Please re-enter.")
        else:
            break
    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-' ")
        Prov = input("Please enter name of province: ")
        if not set(Prov).issubset(allowed_char):
            print("Province name contains invalid characters. Please re-enter. ")
        elif len(Prov) <= 2:
            print("Province must be spelled out. Please re-enter.")
        elif Prov == "":
            print("Province name cannot be blank. Please re-enter. ")
        else:
            break
    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890")
        PostalCode = input("Please enter your postal code(A1A1A1): ").capitalize()
        if not set(PostalCode).issubset(allowed_char):
            print("Postal Code contains invalid characters. Please Re-enter.")
        elif PostalCode == "":
            print("Postal code cannot be blank. Please enter postal code. ")
        else:
            break

    ReceiptDsp = f"{FirstName.upper()[0]}{LastName.upper()[0]}-{LicPlate.upper()[3:6]}-{PhoneNum[6:10]}"
    SalesPriceDsp = "${:,.2f}".format(float(SellPrice))
    TradeInDsp = "${:,.2f}".format(float(TradeIn))
    PriceAfterTradeDsp = "${:,.2f}".format(PriceAfterTrade)
    TaxesDsp = "${:,.2f}".format(Taxes)
    LicenseFeeDsp = "${:,.2f}".format(LicenseFee)
    Trans_FeeDsp = "${:,.2f}".format(TransferFee)
    TotalSalesCostDsp = "${:,.2f}".format(TotalSalesPrice)
    MonthlyPayDsp = "${:,.2f}".format(MonthlyPay)
    PaymentDate = InvoiceDate + datetime.timedelta(30)
    PaymentDate = PaymentDate.strftime("%d-%b-%y").upper()

    print()
    print("        Honest Harry Car Sales  ")
    print("       Used Car Sale and Receipt ")
    print()
    print("Invoice Date: ", InvoiceDate.strftime("%B %d, %Y "))
    print("Receipt No:", ReceiptDsp.upper())
    print()
    print("Sold to: ")
    print("    "f"{FirstName.upper()[0]}.", LastName.title())
    print("   ", StAdd.title())
    print("   ", City.title(), "," "", Prov.title(), "," "", PostalCode.upper())
    print()
    print("Car Details: ")
    print("          ", VehicleYear, VehicleMake.upper(), VehicleModel.upper())
    print("-----------------------------------------")
    print("Sale Price: ", "{:>28}".format(SalesPriceDsp))
    print("Trade Allowance: ", "{:>23}".format(TradeInDsp))
    print("Price after Trade: ", "{:>21}".format(PriceAfterTradeDsp))
    print("                              -----------")
    print("HST:", "{:>36}".format(TaxesDsp))
    print("Licence Fee: {:>28}".format(LicenseFeeDsp))
    print("Transfer Fee: {:>27}".format(Trans_FeeDsp))
    print("                              -----------")
    print("Total Sales Cost: {:>23}".format(TotalSalesCostDsp))
    print("-----------------------------------------")
    print("Terms: {:>2}              Total Payments:{:>3}".format(Choice, Payments))
    print("Monthly Payment: {:>24}".format(MonthlyPayDsp))
    print("First Payment Date:   {:>19} ".format(PaymentDate))
    print()
    print("{:^41}".format("Honest Harry Car Sales"))
    print("{:^41}".format("Best Used cars at the best price!"))
    print()

    Cont = input("Do you wish to continue or end? (CON,END): ").upper()
    if Cont == "CON":
        print()
        continue
    elif Cont == "END":
        print()
        print("Thank you for shopping with Honest Harry's car sales!")
        exit()
    else:
        print("Invalid Answer. Please re-enter")
