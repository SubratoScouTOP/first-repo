class LibraryManagementSystem:
    def __init__(self,bookname, author, price, quantity):
        self.bookname = bookname
        self.author = author
        self.price = price
        self.quantity = quantity

    def get_bookname(self):
        return self.bookname
    def get_author(self):
        return self.author
    def get_price(self):
        return self.price
    def get_quantity(self):
        return self.quantity
    def set_bookname(self, bookname):
        self.bookname = bookname
    def set_author(self, author):
        self.author = author    
    def set_price(self, price):
        self.price = price
    def set_quantity(self, quantity):
        self.quantity = quantity
    def display_book_info(self):
        print(f"Book Name: {self.bookname}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")

print("Welcome to the Library Management System")
book1 = LibraryManagementSystem("Python Programming", "John Doe", 500, 10)
book1.display_book_info()
book2 = LibraryManagementSystem("Data Structures", "Jane Smith", 600, 5)
book2.display_book_info()
book3 = LibraryManagementSystem("Machine Learning", "Alice Johnson", 800, 2)
book3.display_book_info()
book4 = LibraryManagementSystem("Web Development", "Bob Brown", 700, 8)
book4.display_book_info()
