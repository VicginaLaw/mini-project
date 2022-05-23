import pymysql
from sqlalchemy import true
from tabulate import tabulate

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="pass1",
    database="mini-project"
)

def view_products():
    cursor = connection.cursor()
    sql = "SELECT * FROM Products"
    cursor.execute(sql)
    result = cursor.fetchall()
    print ("\nHere is the Product List: ")
    col_names = ["Product_ID", "Name", "Price"]
    print(tabulate(result, headers=col_names))
    cursor.close()

def view_couriers():
    cursor = connection.cursor()
    sql = "SELECT * FROM Couriers"
    cursor.execute(sql)
    result = cursor.fetchall()
    print ("\nHere is the Courier List: ")
    col_names = ["Courier_id", "Name", "Phone"]
    print(tabulate(result, headers=col_names))
    cursor.close()

def view_orders():
    while true:
        print ("\n----- View Order List -----")
        print ("[0] By Order ID")
        print ("[1] By Status")
        print ("[2] By Courier")
        print ("[3] Customer List\n")
        option = input("\nChoose an option: ")

        if option == "0":
            cursor = connection.cursor()
            sql = "SELECT * FROM Orders"
            cursor.execute(sql)
            result = cursor.fetchall()
            print ("\nHere is the Order List: ")
            col_names = ["Order_id", "Customer_name", "Customer_address", "Phone_number", "Courier", "Status", "Items"]
            print(tabulate(result, headers=col_names))
            cursor.close()
            break

        elif option == "1":
            cursor = connection.cursor()
            sql = "SELECT * FROM Orders ORDER BY Status"
            cursor.execute(sql)
            result = cursor.fetchall()
            print ("\nHere is the Order List: ")
            col_names = ["Order_id", "Customer_name", "Customer_address", "Phone_number", "Courier", "Status", "Items"]
            print(tabulate(result, headers=col_names))
            cursor.close()
            break

        elif option == "2":
            cursor = connection.cursor()
            sql = "SELECT * FROM Orders ORDER BY Courier"
            cursor.execute(sql)
            result = cursor.fetchall()
            print ("\nHere is the Order List: ")
            col_names = ["Order_id", "Customer_name", "Customer_address", "Phone_number", "Courier", "Status", "Items"]
            print(tabulate(result, headers=col_names))
            cursor.close()
            break

        elif option == "3":
            cursor = connection.cursor()
            sql = "SELECT order_id, customer_name, customer_address, phone_number FROM Orders"
            cursor.execute(sql)
            result = cursor.fetchall()
            print ("\nHere is the Order List: ")
            col_names = ["Order_id", "Customer_name", "Customer_address", "Phone_number"]
            print(tabulate(result, headers=col_names))
            cursor.close()
            break

        else: 
            invaild()
            continue

def view_order_status():
    cursor = connection.cursor()
    sql = "SELECT * FROM Order_status"
    cursor.execute(sql)
    result = cursor.fetchall()
    print ("\nHere is the Order Status List: ")
    col_names = ["Order_status_id", "Order_status"]
    print(tabulate(result, headers=col_names))
    cursor.close()

def add_new_product():
    while true:
        print ("\n----- Create New Product -----")

        try:
            new_product = input("Add a new product: ").title().strip()
            new_price = float (input(f"Set a price of {new_product}: ")) 
        
        except: 
            invaild()
            continue

        cursor = connection.cursor()
        sql = (f"INSERT INTO Products SET Name = '{new_product}', Price = {new_price}")
        cursor.execute(sql)
        connection.commit()
        cursor.close()

        print (f"\n{new_product} is added.")
        break

def add_new_courier():
    while true:
        print ("\n----- Create New Courier -----")

        new_courier = input("The name of new courier: ").title().strip()
        new_phone = input(f"The phone number of {new_courier}: ").strip() 

        if new_courier == "" or new_phone == "": 
            invaild()
            print ("Don't leave blank for each question!")
            continue

        cursor = connection.cursor()
        sql = (f"INSERT INTO Couriers SET Name = '{new_courier}', Phone = '{new_phone}'")
        cursor.execute(sql)
        connection.commit()
        cursor.close()

        print (f"\n{new_courier} is added.")
        break

def add_new_order():
    while true:
        print ("\n----- Create New Order -----")

        name = input ("Customer Name: ").title().strip()
        address = input ("Customer Address: ").title().strip()
        phone = input ("Customer Phone: ").strip()

        if name == "" or address == "" or phone == "":
            invaild()
            print ("Don't leave blank for each question!")
            continue

        view_products()
        print("\nPlease Chooose the items! If more than one item, please use comma to separate them. e.g '1,3,4'")
        item = input ("Type in the Product IDs:").strip()

        if item == "" :
            invaild()
            print ("Don't leave blank for each question!")
            continue

        view_couriers()
        try:
            courier = int(input ("Courier ID [INDEX ONLY]: "))
        except:
            invaild()
            print ("Don't leave blank for each question and INDEX ONLY!")
            continue
            

        cursor = connection.cursor()
        sql = (f"INSERT INTO Orders SET Customer_name = '{name}', Customer_address = '{address}', Phone_number = '{phone}', Courier = {courier}, Status = 1, Items = '{item}'")
        cursor.execute(sql)
        connection.commit()
        cursor.close()

        print ("\nThe Order is added.")
        break

def delete_product():
    while true:
        try: 
            print ("\n----- Delete Product -----")
            view_products()
            del_item = int (input("\nThe ID of product need to delete [INDEX ONLY]: "))

        except:
            invaild()
            print("Please input the INDEX only.")
            continue

        cursor = connection.cursor()
        sql = (f"DELETE FROM Products WHERE Product_id = {del_item}")
        cursor.execute(sql)
        connection.commit()
        cursor.close()

        print ("\nThe product is deleted.")
        break

def delete_courier():
    print ("\n----- Delete Courier -----")
    view_couriers()    
    del_item = int (input("\nThe ID of courier need to delete: "))

    cursor = connection.cursor()
    sql = (f"DELETE FROM Couriers WHERE Courier_id = {del_item}")
    cursor.execute(sql)
    connection.commit()
    cursor.close()
            
    print ("\nThe Courier is deleted.")

def delete_order():
    while true:
        try: 
            print ("\n----- Delete Order -----")
            view_orders()            
            del_item = int (input("\nThe ID of order need to delete [INDEX ONLY]: "))

        except:
            invaild()
            print("Please input the INDEX only.")
            continue

        cursor = connection.cursor()
        sql = (f"DELETE FROM Orders WHERE Order_id = {del_item}")
        cursor.execute(sql)
        connection.commit()
        cursor.close()

        print("\nThe Order is deleted")
        break

def update_order_status():
    print ("\n----- Update Existing Order Status -----")
    view_orders()            
    order_update = int (input ("\nThe ID of order need to update: "))

    view_order_status()            
    status_update = int (input ("\nType in the updated status ID: "))

    cursor = connection.cursor()
    sql = (f"UPDATE Orders SET Status = {status_update} WHERE Order_id = {order_update}")
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    print("\nThe Order Status is Updated")

def update_order():
    while true:
        try: 
            print ("\n----- Update Existing Order Status -----")
            view_orders()            
            order_update = int (input ("\nThe ID of order need to update[INDEX ONLY]: "))

        except:
            invaild()
            print("Please input INDEX only!")
            continue

        try:
            view_order_status()            
            status_update = int (input ("\nType in the updated status ID: "))
        except:
            invaild()
            print("Please input INDEX only!")
            continue

        cursor = connection.cursor()
        sql = (f"UPDATE Orders SET Status = {status_update} WHERE Order_id = {order_update}")
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        
        print("\nThe Order Status is Updated")
        break

def update_product():
    while true:
        try: 
            print ("\n----- Update Existing Product -----")

            view_products()
            existing_product = int (input ("\nThe ID of product need to update: "))
            print ("\nPlease press ENTER to skip the details DONT'T NEED to update.")
            update_name = input ("Update Product Name: ").title().strip()
            update_price =  input ("Update Product Price: ")

        except: 
            invaild()
            continue

        if len(update_name) == 0 and len(update_price) > 0:
            cursor = connection.cursor()
            sql = f"UPDATE Products SET Price = {float(update_price)} WHERE Product_id = {existing_product}"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            print ("\nThe Product is updated.")
            break

        elif len(update_price) == 0 and len(update_name) > 0:
            cursor = connection.cursor()
            sql = f"UPDATE Products SET Name = '{update_name}' WHERE Product_id = {existing_product}"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            print ("\nThe Product is updated.")
            break

        elif len(update_name) > 0 and len(update_price) > 0:
            cursor = connection.cursor()
            sql = f"UPDATE Products SET Name = '{update_name}', Price = {float(update_price)} WHERE Product_id = {existing_product}"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            print ("\nThe Product is updated.")
            break

        else: 
            print ("Nothing updated.")
            break

def update_courier():
    while true:
        try: 
            print ("\n----- Update Existing Product -----")
            view_couriers()
            existing_couriers = int (input ("Please input the ID of courier need to update: "))
            update_name = input ("Update Courier Name: ").title().strip()
            update_phone = input ("Update Courier Phone: ").strip()

        except: 
            invaild()
            continue

        if len(update_name) == 0 and len(update_phone) > 0:
            cursor = connection.cursor()
            sql = f"UPDATE Couriers SET Phone = '{update_phone}'  WHERE Courier_id = {existing_couriers}"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            print ("\nThe Courier is updated.")
            break

        elif len(update_phone) == 0 and len(update_name) > 0:
            cursor = connection.cursor()
            sql = f"UPDATE Couriers SET Name = '{update_name}' WHERE Courier_id = {existing_couriers}"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            print ("\nThe Courier is updated.")
            break

        elif len(update_name) > 0 and len(update_phone) > 0:
            cursor = connection.cursor()
            sql = f"UPDATE Couriers SET Name = '{update_name}', Phone = '{update_phone}' WHERE Courier_id = {existing_couriers}"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            print ("\nThe Courier is updated.")
            break

        else: 
            print ("Nothing updated.")
            break

def Main_Menu():
    print ("\n----- Main Menu -----")
    print ("[0] Exit App")
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

def invaild():
    print ("\n----- Invaild Answer -----")
    print ("Please enter a valid input!")

while True:
    Main_Menu()
    
    try:
        mm = int( input("Choose an option: \n"))
    except:
        invaild()
        continue

    if mm == 0:
        print ("\nExit app! Bye!")
        break
    
    while mm == 1:
        Print_Menu("Product")
        try:
            pm = int( input("Choose an option: \n"))
            
        except:
            invaild() 
            continue

        if pm == 0: #RETURN to main menu
            break

        elif pm == 1: #PRINT products
            view_products()        

        elif pm == 2: # CREATE new product
            add_new_product()

        elif pm == 3: #UPDATE existing product
            update_product()

        elif pm == 4: #DELETE courier
            delete_product()

        elif pm > 4: invaild()

    while mm == 2:
        Print_Menu("Courier")
        try:
            cm = int( input("Choose an option: \n"))
        except:
            invaild()
            continue

        if cm == 0: break

        elif cm == 1:
            view_couriers()

        elif cm == 2: # CREATE new courier
            add_new_courier()

        elif cm == 3: #UPDATE existing courier
            update_courier()

        elif cm == 4: #DELETE courier
            delete_courier()

        elif cm > 4: invaild()
    
    while mm == 3: # orders menu
        Order_Menu()
        try:
            om = int( input("Choose an option: \n"))
        except NameError: 
            invaild()
            continue
        except ValueError:
            invaild()
            continue

        if om == 0: break

        elif om == 1:
            view_orders()

        elif om == 2: # CREATE order
            add_new_order()

        elif om == 3: # UPDATE existing order status
            update_order_status()

        elif om == 4: #UPDATE existing order
            update_order()

        elif om == 5: #DELETE order
            delete_order()

        elif om > 5: invaild()
    
    if mm > 3: 
        invaild()
        continue