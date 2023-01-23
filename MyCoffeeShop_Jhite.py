# Header
print("Welcome to MyCoffee Shop")
print("__________MENU__________")
print("No.      Name          Cost")

# Define Lists
A_Items = ['Coffee', 'Latte', 'Espresso', 'Cappuccino', 'Hot Chocolate']
Item_Cost = [3.15, 5.25, 5.55, 4.55, 3.55]
total = 0

# Print the menu
for i in range(0,len(A_Items)):
    print(str(i+1) + "    " + str(A_Items[i]) + "       " + str(Item_Cost[i]))
# Input Item Wanted
while True:
    print("\nWhat item would you like to order? ")
    D_Item = int(input('Enter item number (or "99" to end)\n'))
    # End the program
    if D_Item == 99:
        print("Thanks for shopping at MyCoffee Shop")
        break
    # Invalid Item Number
    elif D_Item not in range(len(A_Items)+1):
        print("The Item you chose does not exist")
    # Math
    else:
        IC = Item_Cost[D_Item - 1]
        Amnt = int(input("How many would you like?\n"))
        total = (Amnt * IC) + total
        print("Total for your order is " + str(total))

