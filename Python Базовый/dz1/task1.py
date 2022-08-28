#Задание 1
#Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе издания и жанре.
# Создайте несколько разных книг. Определите для него операции проверки на равенство и неравенство, методы __repr__ и __str__.


class Books:
    def __init__(self, author, title, year_published, genre):
        self.author = author
        self.title = title
        self.year_published = year_published
        self.genre = genre

    # def book_info(self):
    #     print("rtyuiop[po")

    def __repr__(self):
        return f'({self.author}, {self.title}, {self.year_published}, {self.genre})'

    def __str__(self):
        return f"{self.author} will be write book {self.title} and published in {self.year_published} in {self.genre} genre."


book1 = Books("Jack London", "White Fang", 1906, "Adventure")
book2 = Books("Jack London", "Love of Life", 1907, "Drama")
book3 = Books("Herman Melville", " Moby Dick", 1851, "Novel")

print(repr(book1))
print(book3)


