class Book:
    def __init__(self, title, author, price):
        # `self` is the reference to the newly constructed object
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        # this method is automatically called by Python whenever an object of this class is treated like a str
        # `self` is the reference to the object being treated as str
        # Java/C#/JavaScript --> overriding the toString()
        return f'Book(title="{self.title}", author="{self.author}", price={self.price})'


if __name__ == '__main__':
    b1 = Book('Let us C', 'Y Kanitkar', 299)  # Java or C#: Book b1 = new Book();  # C++: Book b1; Book *b1 = new Book;
    print(f'b1 is {b1}')
    # print(f'type of b1 is {type(b1)}')
    # print(f'attributes in b1 are {dir(b1)}')
    # b1.title = 'Let us C'
    # b1.author = 'Yashwant Kanitkar'
    # b1.price = 299
    # print(f'attributes in b1 are {dir(b1)}')
    b2 = Book('Python cookbook', 'John Doe', 789)
    # print(f'attributes in b2 are {dir(b2)}')
    print(b2)

