mylist = [1,2,3]
len(mylist)
"""
class Sample():
    pass
mysample = Sample()
len(mysample)#TypeError: object of type 'Sample' has no len()
"""

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

b = Book("Python rocks","Jose",200)
print(b)#<__main__.Book object at 0x0000028F9EB83FD0>
print(str(b))#<__main__.Book object at 0x000001A3455D7B20> type是字串

class Book02():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")

book = Book02("Harry potter","Jenis",250)
print(book)#Harry potter by Jenis  印出初始化內容
str(book)#Harry potter by Jenis
print(len(book))#250
del b#A book object has been deleted

