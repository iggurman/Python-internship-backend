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
    },
    {
        "book_id": 105,
        "title": "Deep Learning",
        "author": "Ian Goodfellow",
        "available": False
    },
    {
        "book_id": 106,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "available": True
    },
    {
        "book_id": 107,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "available": True
    },
    {
        "book_id": 108,
        "title": "Computer Networks",
        "author": "Andrew S. Tanenbaum",
        "available": False
    }
]

print("__________________________")
print("\nLibrary Management System ")
print(f"__________________________")
print(f"\nMenu")

print("\n1. Add Book ")
print("2. View Books")
print("3. Search Book")
print("4. Issue Book")
print("5. Return Book")
print("6. Delete Book")
print("7. Exit")
user_option=int(input("Enter Option"))


if user_option==1:
    print("Add Book")
    while True:
        book_id=int(input("\nBook Id: "))
        while True:
            if book_id.isdigit():
                if book_id<0 or book_id>500:
                    print("Invalid Book id ")                
                    continue
                break
            else:
                continue
        break
        
        
    
    
    
    
    
    # while book_id>=500 or book_id<0:
    #     print("Invalid Book Id ")
    #     if book_id==chr(book_id):
    #         book_id=int(input("\nBook Id: "))
    # title=input("Title of Book: ")
    # author=input("Author Name: ")
    # available=input("availability")

        
