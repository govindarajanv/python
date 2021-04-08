class Bookshelf:

    def __init__(self):
        self.__index = 0
        self.__books = []

    def add_books(self, other):
        self.__books.append(other)

    def __len__(self):
        return len(self.__books)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index == len(self.__books):
            raise StopIteration

        p = self.__books[self.__index]
        self.__index += 1
        return p

shelf = Bookshelf()
shelf.add_books("A")
shelf.add_books("B")
shelf.add_books("C")
shelf.add_books("D")

print (len(shelf))

for i in shelf:
    print (i)
