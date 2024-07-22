class Book:
    def __init__(self, serial_number, title, author, quantity):
        self.serial_number = serial_number
        self.title = title
        self.author = author
        self.quantity = quantity
        self.borrowed = 0

    def get_serial_number(self):
        return self.serial_number

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_quantity(self):
        return self.quantity

    def get_borrowed(self):
        return self.borrowed

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_borrowed(self, borrowed):
        self.borrowed = borrowed


class Student:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []

    def get_name(self):
        return self.name

    def get_checked_out_books(self):
        return self.checked_out_books

    def check_out_book(self, book):
        if len(self.checked_out_books) >= 3:
            print("Sorry, you have already checked out the maximum number of books.")
            return

        if book.get_quantity() - book.get_borrowed() <= 0:
            print("Sorry, that book is not available.")
            return

        book.set_borrowed(book.get_borrowed() + 1)
        self.checked_out_books.append(book)

    def check_in_book(self, book):
        if book not in self.checked_out_books:
            print("You have not checked out that book.")
            return

        book.set_borrowed(book.get_borrowed() - 1)
        self.checked_out_books.remove(book)


class Library:
    def __init__(self):
        self.books = []
        self.students = []

    def add_book(self, book):
        self.books.append(book)

    def update_book_quantity(self, serial_number, new_quantity):
        for book in self.books:
            if book.get_serial_number() == serial_number:
                book.set_quantity(new_quantity)
                return
        print("Book not found.")

    def search_book_by_serial_number(self, serial_number):
        for book in self.books:
            if book.get_serial_number() == serial_number:
                print("Title: {}, Author: {}, Quantity: {}, Borrowed: {}".format(book.get_title(), book.get_author(), book.get_quantity(), book.get_borrowed()))
                return
        print("Book not found.")

    def search_books_by_author_name(self, author_name):
        for book in self.books:
            if book.get_author() == author_name:
                print("Title: {}, Serial Number: {}, Quantity: {}, Borrowed: {}".format(book.get_title(), book.get_serial_number(), book.get_quantity(), book.get_borrowed()))

    def show_all_books(self):
        for book in self.books:
            print("Title: {}, Serial Number: {}, Author: {}, Quantity: {}, Borrowed: {}".format(book.get_title(), book.get_serial_number(), book.get_author(), book.get_quantity(), book.get_borrowed()))

    def register_student(self, student):
        self.students.append(student)

    def show_all_students(self):
        for student in self.students:
            print("Name: {}".format(student.get_name()))

# Create a library instance
library = Library()

# Create book instances and add them to the library
book1 = Book("1", "Book 1", "Author 1", 5)
book2 = Book("2", "Book 2", "Author 2", 3)
book3 = Book("3", "Book 3", "Author 1", 2)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Create student instances and register them in the library
student1 = Student("John")
student2 = Student("Emily")

library.register_student(student1)
library.register_student(student2)

# Perform operations on the library, books, and students
library.show_all_books()  # Show all books in the library

library.search_book_by_serial_number("2")  # Search for a book by serial number

library.search_books_by_author_name("Author 1")  # Search for books by author name

student1.check_out_book(book1)  # Student 1 checks out a book

student1.check_out_book(book2)  # Student 1 checks out another book

student1.check_out_book(book3)  # Student 1 checks out the maximum number of books

student1.check_in_book(book1)  # Student 1 returns a book

library.show_all_students()  # Show all registered students in the library
