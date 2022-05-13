try:
    products_txt = open("products.txt", "r")
    products = [product.strip() for product in products_txt.readlines()]

    couriers_txt = open("couriers.txt", "r")
    couriers = [courier.strip() for courier in couriers_txt.readlines()]

except:
    print ("Failed to open file.")

def invaild():
    print ("\n----- Invaild Answer -----")
    print ("Please enter a valid option! \n")

def index_products():
    for i, product in enumerate(products):
        print(i, product)

def index_couriers():
    for i, courier in enumerate(couriers):
        print(i, courier)

def update_products():
    with open("products.txt", "w") as products_txt:
        for update_product in products:
            products_txt.write(update_product + "\n")
    products_txt.close()

def update_couriers():
    with open("couriers.txt", "w") as couriers_txt:
        for update_courier in couriers:
            couriers_txt.write(update_courier + "\n")
    couriers_txt.close()

while True:
    try:
        print ("\n----- Main Menu -----")
        print ("[0] Save Change and Exit App")
        print ("[1] Products Menu")
        print ("[2] Couriers Menu\n")

        mm = int( input("Choose an option: \n"))

    except:
        invaild()
        continue

    if mm == 0: # EXIT app
        print ("\nExit app! Bye!")
        break

    while mm == 1: # products menu
        
        try:
            print ("\n----- Products Menu -----")
            print ("[0] Return to Main Menu")
            print ("[1] View Products List")
            print ("[2] Create New Product")
            print ("[3] Update Existing Product")
            print ("[4] Delete Product \n")

            pm = int( input("Choose an option: \n"))
            
        except:
            invaild()
            continue 

        if pm == 0: #RETURN to main menu
            break

        elif pm == 1: #PRINT products list
            print ("\nHere is the product list: ")
            print (products)
            continue

        elif pm == 2: # CREATE new product
            new_product = input("Add a new product: ").title()
            print (f"\n{new_product} is added.")
            print ("Here is the updated product list: ")
            products.append(new_product)
            print (products)

            with open("products.txt", "a+") as products_txt:
                products_txt.write("\n" + new_product)
                products_txt.close()
    
            continue

        elif pm == 3: #UPDATE existing product
            try:
                index_products()

            except: 
                invaild()
                continue   

            update_product = int (input ("\nType the number of item need to update: "))
            old_product = products[update_product]
            new_product = input('Type name of new product: ').title()
            products[update_product] = new_product

            print ("\nHere is the updated product list: ")
            print (products)

            update_products()
            continue

        elif pm == 4: #DELETE product
            try: 
                index_products()
            
                delete_product = int (input ("Type the number of item need to delete: "))
                del products[delete_product]

                print ("\nHere is the updated product list: ")
                print (products)

                update_products()
                continue

            except:
                invaild()
                continue

    while mm == 2: # couriers menu
        try:
            print ("\n----- Couriers Menu -----")
            print ("[0] Return to Main Menu")
            print ("[1] View Couriers List")
            print ("[2] Create New Courier")
            print ("[3] Update Existing Courier")
            print ("[4] Delete Courier \n")
            cm = int( input("Choose an option: \n"))
            
        except:
            invaild()
            continue

        if cm == 0: #RETURN to main menu
            break

        elif cm == 1: #PRINT couriers list
            print ("\nHere is the couriers list: ")
            print (couriers)
            continue

        elif cm == 2: # CREATE new courier
            new_courier = input("Add a new courier: ").title()
            print (f"\n{new_courier} is added.")
            print ("Here is the updated courier list: ")
            couriers.append(new_courier)
            print (couriers)

            with open("couriers.txt", "a+") as couries_txt:
                couries_txt.write("\n" + new_courier)
                couries_txt.close()

        elif cm == 3: #UPDATE existing courier
            try:
                index_couriers()

            except: 
                invaild()
                continue   

            update_courier = int (input ("\nType the number of item need to update: "))
            old_courier = couriers[update_courier]
            new_courier = input('Type name of new product: ').title()
            couriers[update_courier] = new_courier

            print ("\nHere is the updated courier list: ")
            print (couriers)
    
            update_couriers()
            continue

        elif cm == 4: #DELETE courier
            try:
                index_couriers()

                delete_courier = int (input ("Type the number of item need to delete: "))
                del couriers[delete_courier]

                print ("\nHere is the updated product list: ")
                print (couriers)

                update_couriers()
                continue

            except:
                invaild()
                continue