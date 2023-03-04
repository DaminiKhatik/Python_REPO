class Book:   
    def __init__(self, title, author):     
        self.title = title       
        self.author = author
book1 = Book(title="Right Ho, Jeeves", author="P.G. Wodehouse")
print( book1.title)
print(book1.author)