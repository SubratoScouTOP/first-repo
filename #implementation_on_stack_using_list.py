stack = []
while True:
    print("\nChoose an operation:")
    print("1. Push (add item)")
    print("2. Pop (remove item)")
    print("3. Peek (view top item)")
    print("4. Show Stack")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        item1 = input("Enter first value: ")
        item2 = input("Enter second value: ")
        stack.extend([item1, item2])
        print("Item pushed to stack.")
    elif choice == "2":
        if len(stack) == 0:
            print("Stack is empty. Nothing to pop.")
        else:
            popped_item = stack.pop()
            print("Popped item:", popped_item)
    elif choice == "3":
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Top of the stack (peek):", stack[-1])
    elif choice == "4":
        print("Current Stack:", stack)
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")












































"""ck = []  
stack.append(["A","hello"])
print("Stack after pushing:", stack)
print("Top of the stack (peek):", stack[-1]) #as lifo
print("Popped item:", stack.pop())
print("Stack after popping:", stack)"""
