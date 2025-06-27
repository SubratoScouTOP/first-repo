#menu (use list) 
#order (use list)
#order in queue(use queue)
#order in progress can use stack 
#order completed queue
#for billing use numpy 

import numpy as np
menu = {"Pizza": 150, "Burger": 100, "Pasta": 120, "Fries": 60, "Coke": 40}
orders = []           # list of (customer_name, item)
cancel_stack = []     # stack: LIFO
waiting_queue = []    # queue: FIFO using list

print(" Welcome to the Restaurant (Simple Version with NumPy)")
while True:
    print("\nMenu:")
    print("1. Show Menu")
    print("2. Place Order")
    print("3. Cancel Last Order (Stack)")
    print("4. View All Orders")
    print("5. Add to Waiting Queue")
    print("6. Serve Waiting Customer (Queue)")
    print("8. Generate Bill using NumPy")
    print("9. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("\n Menu:")
        for item, price in menu.items():
            print(f"{item}: {price}")
    
    elif choice == "2":
        name = input("Enter your name: ")
        item = input("Enter item to order: ")
        if item in menu:
            order = (name, item)
            orders.append(order)
            cancel_stack.append(order)
            print(f" Order placed: {item} by {name}")
        else:
            print(" Item not found in menu.")

    elif choice == "3":
        if cancel_stack:
            last = cancel_stack.pop()
            orders.remove(last)
            print(f" Last order cancelled: {last}")
        else:
            print("No order to cancel.")

    elif choice == "4":
        print("\n Current Orders:")
        if not orders:
            print("No orders yet.")
        else:
            for o in orders:
                print(f"{o[0]} ordered {o[1]}")

    elif choice == "5":
        name = input("Enter customer name to add to waiting queue: ")
        waiting_queue.append(name)
        print(f" {name} added to waiting list.")

    elif choice == "6":
        if waiting_queue:
            served = waiting_queue.pop(0)  # remove first
            print(f" {served} has been served.")
        else:
            print("No customers in queue.")

    elif choice == "8":
        if not orders:
            print("No orders to bill.")
        else:
            prices = [menu[item] for _, item in orders]
            arr = np.array(prices)
            print("\n Billing Summary:")
            print("Items Ordered:", prices)
            print("Total Amount: ", np.sum(arr))
            print("Average Price: ", np.mean(arr))
            print("Highest Price: ", np.max(arr))
            print("Lowest Price: ", np.min(arr))
    
    elif choice == "9":
        print(" Thank you for visiting!")
        break
    
    else:
        print("Invalid input. Please try again.")














































"""import numpy as np
menu = {"Pizza": 150,"Burger": 100,"Pasta": 120,"Fries": 60,"Coke": 40}
orders = []           # list of (customer_name, item)
cancel_stack = []     # stack: LIFO
waiting_queue = []    # queue: FIFO using list
unique_customers = set()  # set for unique names
print(" Welcome to the Restaurant (Simple Version with NumPy)")
while True:
    print("\nMenu:")
    print("1. Show Menu")
    print("2. Place Order")
    print("3. Cancel Last Order (Stack)")#subrato
    print("4. View All Orders")
    print("5. Add to Waiting Queue")
    print("6. Serve Waiting Customer (Queue)")
    print("8. Generate Bill using NumPy")#subrato
    print("9. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("\n Menu:")
        for item, price in menu.items():#subrato
            print(f"{item}:{price}")
    elif choice == "2":
        name = input("Enter your name: ")
        unique_customers.add(name)
        item = input("Enter item to order: ")
        if item in menu:
            order = (name, item)
            orders.append(order)
            cancel_stack.append(order)
            print(f" Order placed: {item} by {name}")
        else:
            print(" Item not found in menu.")#subrato

    elif choice == "3":
        if cancel_stack:
            last = cancel_stack.pop()
            orders.remove(last)
            print(f" Last order cancelled: {last}")
        else:
            print("No order to cancel.")

    elif choice == "4":
        print("\n Current Orders:")
        if not orders:
            print("No orders yet.")
        else:
            for o in orders:
                print(f"{o[0]} ordered {o[1]}")

    elif choice == "5":
        name = input("Enter customer name to add to waiting queue: ")
        waiting_queue.append(name)
        print(f" {name} added to waiting list.")

    elif choice == "6":
        if waiting_queue:
            served = waiting_queue.pop(0)  # remove first
            print(f" {served} has been served.")
        else:
            print("No customers in queue.")

    elif choice == "7":
        print("Unique Customers:")
        for c in unique_customers:
            print(c)
    elif choice == "8":
        if not orders:
            print("No orders to bill.")
        else:
            prices = [menu[item] for _, item in orders]
            arr = np.array(prices)
            print("\n Billing Summary:")
            print("Items Ordered:", prices)
            print("Total Amount: ", np.sum(arr))
            print("Average Price: ", np.mean(arr))
            print("Highest Price: ", np.max(arr))
            print("Lowest Price: ", np.min(arr))
    elif choice == "9":
        print(" Thank you for visiting!")
        break
    else:
        print("Invalid input. Please try again.")"""





















































""""""
"""menu = {"Pizza": 150,"Burger": 100, "Pasta": 120, "Fries": 60,"Coke": 40}
orders = []
cancel_stack = []
from collections import deque
waiting_queue = deque()
unique_customers = set()
print("  Welcome to the Restaurant!")
while True:
    print("\nMain Menu:")
    print("1. Show Menu")
    print("2. Place Order")
    print("3. Cancel Last Order (Stack)")
    print("4. View All Orders")
    print("5. Add to Waiting Queue")
    print("6. Serve Waiting Customer (Queue)")
    print("7. Show Unique Customers (Set)")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("\n Menu:")
        for item, price in menu.items():
            print(f"{item}: ₹{price}")
    elif choice == "2":
        name = input("Enter customer name: ")
        unique_customers.add(name)
        item = input("Enter item to order: ")
        if item in menu:
            order = (name, item)  # Tuple to store order details
            orders.append(order)
            cancel_stack.append(order)
            print(f" Order placed for {item} by {name}")
        else:
            print(" Item not found in menu.")

    elif choice == "3":
        if cancel_stack:
            last_order = cancel_stack.pop()
            orders.remove(last_order)
            print(f" Last order cancelled: {last_order}")
        else:
            print("No orders to cancel.")

    elif choice == "4":
        print("\n All Orders:")
        if not orders:
            print("No orders yet.")
        else:
            for o in orders:
                print(f"{o[0]} ordered {o[1]}")

    elif choice == "5":
        cname = input("Enter customer name to add to waiting queue: ")
        waiting_queue.append(cname)
        print(f" {cname} added to waiting queue.")

    elif choice == "6":
        if waiting_queue:
            served = waiting_queue.popleft()
            print(f"{served} has been served.")
        else:
            print("No one is in the queue.")

    elif choice == "7":
        print("👥 Unique Customers:")
        for cust in unique_customers:
            print(cust)

    elif choice == "8":
        print("Thank you! Visit again. ")
        break

    else:
        print("Invalid choice. Please try again.")"""
