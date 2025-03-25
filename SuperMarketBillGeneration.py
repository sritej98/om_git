name = input("Enter your name:")
lists = '''
FLOUR   Rs 10/kg
DAL  Rs 8/kg
BEER    Rs 30/liter
MANGOES   Rs 25/kg
AVACADOS Rs 40/kg
CANDY Rs 12/pack
BORNVITA  Rs 200/bottle
'''
price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []
items = {'FLOUR':50,'DAL':45,'BEER':200,'MANGOES':25,'AVACADOS':70,'CANDY':20,'BORNVITA':75}
while True:
    option = input("press 1 for list or 2 to exit:")
    if option == '2':
        print("Thank you for shopping")
        break
    elif option == '1':
        print(lists)
    while True:
        inp1 = input("To buy press 1 or press 2 to exit:")
        if inp1 == '2':
            print("thank you for shopping")
            break
        elif inp1 == '1':
            item = input("choose your items:").upper()
            while True:
                quantity_input = input("Enter quantity:")
                if quantity_input.isdigit():
                    quantity = int(quantity_input)
                    break
                else:
                    print("please enter a valid quantity")
            if item in items:
                price = quantity * items[item]
                pricelist.append((item,quantity,items[item],price)) 
                totalprice += price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
            else:
                print("selected item is not available. sorry for the inconvenience")
if totalprice > 0:
    tax = (totalprice*12)/100
    finalamount = tax+totalprice
    print(25 * "=", "OmSai Supermarket",25 * "=")
    print(28 * " ", "USA")
    print("Name:",name, 30 * " ")
    print(75 * "-")
    print("sno", 10 * " ",'items',8 * " ",'quantity', 8 * " ", 'price')
    for i in range(len(pricelist)):
        print(i, 13 * " ", ilist[i], 8 * " ", qlist[i], 8 * " ", plist[i])
    
    print(50 * "-", 'Total amount:', 'Rs', totalprice)
    print("Tax amount", 50 * " ",'Rs', tax)
    print(75 * "-")
    print(50 * "-", 'Final amount:', 'Rs', finalamount)
    print(75 * "-")
    print(20 * " ", "Thank you and visit again")
    print(75 * "-")


    




            
