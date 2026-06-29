class Book():
    def __init__(self,book_id,title,author,publisher,genre,price,total_pages,available_copies):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.publisher=publisher
        self.genre=genre
        self.price=price
        self.total_pages=total_pages
        self.available_copies=available_copies

    def issue_book(self):
        if self.available_copies>0:
            self.available_copies-=1
            return "available copies are ",self.available_copies
        else:
            return "book not available "
        
        
    def return_book(self):
        self.available_copies+=1
        return "available copies are ",self.available_copies
        
    def show_details(self):
        return (
            "book id is ",self.book_id,
            "title of book is",self.title,
            "author of book is ",self.author,
            "publisher of book is ",self.publisher,
            "book 's genre is ",self.genre,
            "price of book is ",self.price,
            "total pages of book is ",self.total_pages,
            "book's available copies:-",self.available_copies
        )

        
    def update_price(self,price):
        self.price=price
        return "price of book ",self.price
        
    def check_availability(self):
        if self.available_copies<=0:
            print("not available rn ")
        else:
            print("Available!!")
            
            
obj1=Book(101,"gulliver","gurman","rk studios","horror",300000,500,5)
print(obj1.return_book())
            
obj1=Book(101,"gulliver","gurman","rk studios","horror",300000,500,5)
print(obj1.update_price(500))
            
obj1=Book(101,"gulliver","gurman","rk studios","horror",300000,500,5)
print(obj1.update_price(500))