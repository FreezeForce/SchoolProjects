# Define Fx to print menu
def printmenu():
    print("Welcome to MyCoffee Shop")
    print("__________MENU__________")
    print("Name          Cost")
    for x, y in Itemz_Pricez.items():
        print(x, '\t', y)


# Define Dictionary/Variables
total = 0
Itemz_Pricez = {'Coffee': 3.15, 'Latte': 5.25, 'Espresso': 5.55, 'Cappuccino': 4.55, 'Hot Chocolate': 3.55}

# FX for printing the menu
printmenu()

# Input Item Wanted
while True:
    print("\nWhat item would you like to order? ")
    D_Item = (input('Enter item name (or "99" to end)\n'))
    # End the program
    if D_Item == '99' or '':
        print("Thanks for shopping at MyCoffee Shop")
        break
    elif D_Item not in Itemz_Pricez.keys():
        print('That product - ' + D_Item + " - is not available")
    elif D_Item in Itemz_Pricez.keys():
        Amnt = int(input("How many would you like?\n"))
        IC = Itemz_Pricez.get(D_Item, )
        total = (IC * Amnt) + total
        print("Total for your order is " + str(total))

