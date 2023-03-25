class Taggable:
    def tag(self):
        pass


class Book(Taggable):
    def __init__(self, author, title):
        if not title:
            raise ValueError('Title should not be empty')
        self.title = title
        self.author = author
        self.code = None

    def tag(self):
        return [word for word in self.title.split() if word.istitle()]


class Library:
    books = []
    code = 1

    def __init__(self, number, address):
        self.number = number
        self.address = address

    def __iadd__(self, book):
        book.code = Library.code
        Library.code += 1
        self.books.append(book)
        return self

    def __iter__(self):
        return iter(self.books)
