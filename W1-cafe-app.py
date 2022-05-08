# CREATE products list
product_list = ["Tea", "Coffee", "Salad", "Cookies"]

#Main Menu
def MMenu():
    print ("\n----- Main Menu -----")
    print ("[0] Exit App")
    print ("[1] Product Menu \n")

#Invaild Input
def invaild():
    print ("\n----- Invaild Answer -----")
    print ("Please enter a valid option! \n")

#Products Menu
def PMenu():
    print ("\n----- Production Menu -----")
    print ("[0] Return to Main Menu")
    print ("[1] View Products List")
    print ("[2] Create New Product")
    print ("[3] Update Existing Product")
    print ("[4] Delete Product \n")

def index():
    for i, product in enumerate(product_list):
        print(i, product)

while True:
    try:
        # PRINT main menu options
        MMenu()
        # GET user input for main menu option
        mm = int( input("Choose an option: \n"))

    except:
        invaild()
        continue

    if mm == 0: # EXIT app
        print ("\nExit app! Bye!")
        break

    elif mm == 1: #products menu
                
        try:
            PMenu()
            pm = int( input("Choose an option: \n"))
            
        except:
            invaild()
            continue
                
        if pm == 0: 
            continue
                    
        elif pm == 1:
            print (product_list)
            continue #wanna go back to pm

        elif pm == 2:
        # CREATE new product
            new_product = input("Add a new product: ")
            product_list.append(new_product)
            print (f"\n{new_product} is added.")
            print ("Here is the updated product list: ")
            print (product_list)
            continue

        elif pm == 3:
            try: 
                #print product list with number
                index()

                #UPDATE existing product
                update_choice = int (input ("\nType the number of item need to update: "))
                old_product = product_list [update_choice]
                new_product = input('Type name of new product: ').title()
                product_list[update_choice] = new_product

                print ("\nHere is the updated product list: ")
                print (product_list)
                continue
                
            except:
                invaild()
                continue
            
        elif pm == 4:
            try: 
            #print product list with number
                index()

            #DELETE product
                delete_choice = int (input ("Type the number of item need to delete: "))
                del product_list[delete_choice]

                print ("\nHere is the updated product list: ")
                print (product_list)
                continue

            except:
                invaild()
                continue