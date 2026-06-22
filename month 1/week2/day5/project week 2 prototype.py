# Project 2: Library Management System
# Topics Covered
# String 
# List 
# Dictionary  
# Loops 
# Features
# 1. Add Book
# 2. View Books
# 3. Search Book
# 4. Issue Book
# 5. Return Book
# 6. Delete Book
# 7. Exit
# Data
# book = {
#     "book_id": 101,
#     "title": "Python",
#     "author": "Guido",
#     "available": True
# }

#created a list of dictionaries 
# Library Management System

books = [
    {
        "book_id": 101,
        "title": "Python",
        "author": "Guido",
        "available": True
    },
    {
        "book_id": 102,
        "title": "Data Structures",
        "author": "Mark Allen",
        "available": True
    },
    {
        "book_id": 103,
        "title": "Machine Learning Basics",
        "author": "Andrew Ng",
        "available": False
    },
    {
        "book_id": 104,
        "title": "Artificial Intelligence",
        "author": "Stuart Russell",
        "available": True
    }
]

# Lambda function for searching book by ID
find_book = lambda bid: next((book for book in books if book["book_id"] == bid),
    None
)


def add_book():
    print("\n----- Add Book -----")

    book_id = int(input("Enter Book ID: "))

    if not (1 <= book_id <= 500):
        print("Invalid Book ID. Must be between 1 and 500.")
        return

    if find_book(book_id):
        print("Book ID already exists.")
        return

    title = input("Enter Title: ")
    author = input("Enter Author: ")

    new_book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(new_book)
    print("Book Added Successfully!")


def view_books():
    print("\n----- All Books -----")

    if not books:
        print("No books available.")
        return

    for book in books:
        status = "Available" if book["available"] else "Issued"

        print(f"""
Book ID   : {book['book_id']}
Title     : {book['title']}
Author    : {book['author']}
Status    : {status}""")


def search_book():
    print("\n----- Search Book -----")

    book_id = int(input("Enter Book ID: "))

    book = find_book(book_id)

    if book:
        print("\nBook Found")
        print(f"Book ID : {book['book_id']}")
        print(f"Title   : {book['title']}")
        print(f"Author  : {book['author']}")
        print(f"Status  : {'Available' if book['available'] else 'Issued'}")
    else:
        print("Book not found.")


def issue_book():
    print("\n----- Issue Book -----")

    book_id = int(input("Enter Book ID: "))

    book = find_book(book_id)

    if not book:
        print("Book not found.")
        return

    if book["available"]:
        book["available"] = False
        print("Book issued successfully.")
    else:
        print("Book is already issued.")


def return_book():
    print("\n----- Return Book -----")

    book_id = int(input("Enter Book ID: "))

    book = find_book(book_id)

    if not book:
        print("Book not found.")
        return

    if not book["available"]:
        book["available"] = True
        print("Book returned successfully.")
    else:
        print("Book is already available.")


def delete_book():
    print("\n----- Delete Book -----")

    book_id = int(input("Enter Book ID: "))

    book = find_book(book_id)

    if not book:
        print("Book not found.")
        return

    books.remove(book)
    print("Book deleted successfully.")


def menu():
    while True:
        print("""
=================================
    Library Management System
=================================
1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit
""")

        choice = input("Enter Option: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            issue_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            delete_book()

        elif choice == "7":
            print("Thank you for using Library Management System.")
            break

        else:
            print("Invalid Option. Try Again.")


# Start Program
menu()