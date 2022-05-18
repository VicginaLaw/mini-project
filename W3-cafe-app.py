try: #load data 
    products_txt = open("products.txt", "r")
    products = [product.strip() for product in products_txt.readlines()]

    couriers_txt = open("couriers.txt", "r")
    couriers = [courier.strip() for courier in couriers_txt.readlines()]

except:
    print ("Failed to open file.")

def invaild():
    print ("\n----- Invaild Answer -----")
    print ("Please enter a valid option! \n")
    
def index_list(list):
    for i, item in enumerate(list):
        print(i, item)

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

def Main_Menu():
    print ("\n----- Main Menu -----")
    print ("[0] Save Change and Exit App")
    print ("[1] Products Menu")
    print ("[2] Couriers Menu")
    print ("[3] Order Menu\n")

def Print_Menu(menu):
    print (f"\n----- {menu} Menu -----")
    print ("[0] Return to Main Menu")
    print (f"[1] View {menu} List")
    print (f"[2] Create New {menu}")
    print (f"[3] Update Existing {menu}")
    print (f"[4] Delete {menu} \n")

def Order_Menu():
    print ("\n----- Order Menu -----")
    print ("[0] Return to Main Menu")
    print ("[1] View Orders List")
    print ("[2] Create New Order")
    print ("[3] Update Existing Order Status")
    print ("[4] Update Existing Order") 
    print ("[5] Delete Order\n")

def order_format(customer_name, customer_address, customer_phone, courier_index, status):
    return {
        "Customer_name": customer_name, 
        "Customer_address": customer_address, 
        "Customer_phone": customer_phone, 
        "Courier": int(courier_index), 
        "Status": status}

def update_order(key):
    print (f"{key}: " + int(chosen_order[key]))
    update_key = input ("Update: ")
    if update_key == "":
        pass
    else: chosen_order[key] = update_key

def update_item(item):
    try:
        update_item = int(input("\nType the index of item need to update: "))
        old_item = item[update_item]
        new_item = input("Type name of new item: ").title().strip()
        item[update_item] = new_item
        print (f"\n{old_item} changed to {new_item}.")

    except IndexError:
        invaild()
    except ValueError:
        invaild()

def delete_item(item):
    try:
        delete_item = int (input ("Type the index of item need to delete: "))
        del item[delete_item]
        print (f"{item[delete_item]} is deleted.")

    except IndexError:invaild()
    except ValueError:invaild()

Order_List = [{
"Customer_name": "John",
"Customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
"Customer_phone": "0789887334",
"Courier": 2,
"Status": "Preparing"
}]

Status_list = ("Preparing", "Ready to dispatch", "Dispatched", "Done")

while True:
    Main_Menu()
    try:
        mm = int( input("Choose an option: \n"))
    except NameError: 
        invaild()
        continue
    except ValueError:
        invaild()
        continue
    
    if mm == 0: # EXIT app
        print ("\nExit app! Bye!")
        break

    while mm == 1: # products menu
        Print_Menu("Product")
        try:
            pm = int( input("Choose an option: \n"))
            
        except: invaild()

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
            index_list(products)
            update_item(products)
            update_products()

        elif pm == 4: #DELETE product
            index_list(products)
            delete_item(products)
            update_products()

        elif pm > 4:
            invaild()

    while mm == 2: # couriers menu
        try:
            Print_Menu("Courier")
            cm = int( input("Choose an option: \n"))
            
            if cm == 0: #RETURN to main menu
                break

            elif cm == 1: #PRINT couriers list
                print ("\nHere is the couriers list: ")
                print (couriers)

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
                index_list(couriers)
                update_item(couriers)
                update_couriers()

            elif cm == 4: #DELETE courier
                index_list(couriers)
                delete_item(couriers)
                update_couriers()

            elif cm > 4: invaild()

        except:invaild()

    while mm == 3: # order menu
        try:
            Order_Menu()
            om = int( input("Choose an option: \n"))
            
        except:invaild()

        if om == 0: break #RETURN to main menu
    
        elif om == 1: #PRINT orders dictionary
            print ("\nHere is the orders list: ")
            print (Order_List)

        elif om == 2: #Create New Order
            print ("\nCreating New Order")
            customer_name = input ("Customer Name:").title()
            customer_address = input ("Customer Address:").title()
            customer_phone = input ("Customer Phone:").title()
            
            try:
                index_list(couriers)
                courier_index = int(input ("Courier Index: "))

            except: 
                invaild() 

            status = "Preparing"
            
            New_Order = order_format(customer_name, customer_address, customer_phone, courier_index, status)
            Order_List.append(New_Order)
            print ("\nNew order is added.")
            print (New_Order)

        elif om == 3: # UPDATE existing order status
            try:
                index_list(Order_List)
                order_update = int (input ("\nType the index of order need to update: "))
            
            except: 
                invaild() 

            update_list = Order_List[order_update]

            try:
                index_list(Status_list)
                update_status = int (input ("\nType the order status: "))

            except: 
                invaild() 
            
            # UPDATE status for order
            update_list["Status"] = Status_list[update_status]
            update_list = Order_List[order_update]
            print ("\nThe order is updated.")

        elif om == 4: #UPDATE existing order
            index_list(Order_List)
            the_order = input ("Please input the index of order need to update: ")
            chosen_order = Order_List[int(the_order)]

            update_order("Customer_name")
            update_order("Customer_address")
            update_order("Customer_phone")
            print (chosen_order)

            #update courier
            print ("\nCourier: " + str(chosen_order["Courier"]))
            try:
                index_list(couriers)
                update_courier = (input ("Update [INDEX ONLY]: "))
            except:
                invaild() 
            if update_courier == "": pass
            else: chosen_order["Courier"] = int(update_courier)

            #update status
            print ("\nStatus: " + str(chosen_order["Status"]))
            index_list(Status_list)
            status_index = (input ("Update [INDEX ONLY]: "))
            if status_index == "": pass
            else: chosen_order["Status"] = Status_list[int(status_index)]
            
            print ("\nHere is the updated order: ")
            print (chosen_order)

        elif om == 5: #DELETE Order
            index_list(Order_List)
            try:
                delete_item = int (input ("Type the index of item need to delete: "))
                del Order_List[delete_item]
                print ("Order is deleted.")

            except IndexError:invaild()
            except ValueError:invaild()
    
    while mm > 3:
        invaild()
        break