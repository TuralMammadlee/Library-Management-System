# Library-Management-System

This project is a simple Library Management System implemented in Python. It allows managing books and student records, checking out and returning books, and searching for books by serial number or author name.

Features
Add, update, and search for books.
Register and display students.
Check out and return books.
Display all books and students in the library.
Classes
Book
Represents a book in the library.

Attributes:
serial_number (str): The serial number of the book.
title (str): The title of the book.
author (str): The author of the book.
quantity (int): The total number of copies of the book.
borrowed (int): The number of copies currently borrowed.
Methods:
get_serial_number(): Returns the serial number of the book.
get_title(): Returns the title of the book.
get_author(): Returns the author of the book.
get_quantity(): Returns the total quantity of the book.
get_borrowed(): Returns the number of borrowed copies of the book.
set_quantity(quantity): Sets the total quantity of the book.
set_borrowed(borrowed): Sets the number of borrowed copies of the book.
Student
Represents a student in the library.

Attributes:
name (str): The name of the student.
checked_out_books (list): A list of books checked out by the student.
Methods:
get_name(): Returns the name of the student.
get_checked_out_books(): Returns a list of books checked out by the student.
check_out_book(book): Allows the student to check out a book.
check_in_book(book): Allows the student to return a book.
Library
Represents the library containing books and students.

Attributes:
books (list): A list of books in the library.
students (list): A list of students registered in the library.
Methods:
add_book(book): Adds a book to the library.
update_book_quantity(serial_number, new_quantity): Updates the quantity of a book based on its serial number.
search_book_by_serial_number(serial_number): Searches for a book by its serial number.
search_books_by_author_name(author_name): Searches for books by the author's name.
show_all_books(): Displays all books in the library.
register_student(student): Registers a student in the library.
show_all_students(): Displays all students registered in the library.
Usage
Here's how to use the Library Management System:

Create a Library Instance:
library = Library()
Create Book Instances and Add Them to the Library:

book1 = Book("1", "Book 1", "Author 1", 5)
book2 = Book("2", "Book 2", "Author 2", 3)
book3 = Book("3", "Book 3", "Author 1", 2)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
Create Student Instances and Register Them in the Library:

student1 = Student("John")
student2 = Student("Emily")

library.register_student(student1)
library.register_student(student2)
Perform Operations on the Library, Books, and Students:

library.show_all_books()  # Show all books in the library

library.search_book_by_serial_number("2")  # Search for a book by serial number

library.search_books_by_author_name("Author 1")  # Search for books by author name

student1.check_out_book(book1)  # Student 1 checks out a book

student1.check_out_book(book2)  # Student 1 checks out another book

student1.check_out_book(book3)  # Student 1 checks out the maximum number of books

student1.check_in_book(book1)  # Student 1 returns a book

library.show_all_students()  # Show all registered students in the library
Example
Here is an example demonstrating the usage of the Library Management System:

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
This example shows how to create a library, add books, register students, and perform various operations like checking out and returning books.
