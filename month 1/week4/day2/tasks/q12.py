class LibraryBook:
    def __init__(self, copies):
        self.__available_copies = copies

    def issue_book(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
        else:
            print("No copies available")

    def return_book(self):
        self.__available_copies += 1

    def get_available_copies(self):
        return self.__available_copies


b = LibraryBook(5)

print(b.get_available_copies())

b.issue_book()
print(b.get_available_copies())

b.return_book()
print(b.get_available_copies())