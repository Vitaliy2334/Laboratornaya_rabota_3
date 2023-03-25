from PyQt5.QtWidgets import QMainWindow


def task1():
    from Task1 import Fraction
    frac = Fraction(7, 2)
    print(-frac)  # выводит -7/2
    print(~frac)  # выводит 2/7
    print(frac ** 2)  # выводит 49/4
    print(float(frac))  # выводит 3.5
    print(int(frac))  # выводит 3


def task2():
    from Task2 import Library, Book
    lib = Library(1, '51 Some str., NY')
    lib += Book('Leo Tolstoi', 'War and Peace')
    lib += Book('Charles Dickens', 'David Copperfield')
    for book in lib:
        print('[{}] {} "{}"'.format(book.code, book.author, book.title))
        print(book.tag())


def task4():
    from Task4 import StringFormatter
    formatter = StringFormatter("Hello 123 world! This is 456 a test.")
    formatter.remove_short_words(3)\
        .replace_digits()\
        .insert_spaces()\
        .sort_by_size()\
        .sort_lexicographically()
    print(formatter)  # вывод: ! * * * * * * . H T d e e h i l l l o o r s s t t w



def main():
    task1()
    task2()
    """
        Для третьего задания необходимо запускать файл Task3.py путём ввода в терминал команду: "py .\\Task3.py" 
        (один слеш вместо двух нужно использовать)
    """
    task4()


if __name__ == '__main__':
    main()

