# Write a class structure that implements a library. Classes:
#   1) Library - name, books = [], authors = []
#   2) Book - name, year, author (author must be an instance of Author class)
#   3) Author - name, country, birthday, books = []
# Library class
# Methods:
#   - new_book(name: str, year: int, author: Author) - returns an instance of Book class and
# adds the book to the books list for the current library.
#   - group_by_author(author: Author) - returns a list of all books grouped by the specified author
#   - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        author.books.append(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name='{self.name}')"

    def __str__(self):
        return f"Library: {self.name}"


class Book:
    num_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.num_books += 1

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author={self.author})"

    def __str__(self):
        return f"{self.name} ({self.year}) by {self.author.name}"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}')"

    def __str__(self):
        return f"{self.name} ({self.country}, born {self.birthday})"


# create some authors
author1 = Author("J.K. Rowling", "UK", "July 31, 1965")
author2 = Author("George R.R. Martin", "USA", "September 20, 1948")
author3 = Author("J.R.R. Tolkien", "UK", "January 3, 1892")

# create a library and add some books
library = Library("My Library")

book1 = library.new_book("Harry Potter and the Philosopher's Stone", 1997, author1)
book2 = library.new_book("Harry Potter and the Chamber of Secrets", 1998, author1)
book3 = library.new_book("A Song of Ice and Fire", 1996, author2)
book4 = library.new_book("The Lord of the Rings", 1954, author3)

# print out the library and all the books
print(library)
print(library.books)

# group books by author
print(library.group_by_author(author1))
print(library.group_by_author(author2))

# group books by year
print(library.group_by_year(1997))
print(library.group_by_year(1998))

# print out the number of books
print(Book.num_books)


