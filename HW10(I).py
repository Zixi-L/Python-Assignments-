class LibraryPatron():
    def __init__(self, name):
        self.name = name
        self.booksCheckedOut = []
        

    def checkOutBook(self, checkOutLimit ,bookTitle):
        name = self.name
        if len(self.booksCheckedOut) >= self.checkOutLimit:
            print('Sorry',name,'you are at your limit of 2 books')
        else:
            self.booksCheckedOut.append(bookTitle[0])
            print(self.name,'has checked out', bookTitle[0])
        
            
    def returnBook(self, bookTitle): 
        name = self.name
        index = self.booksCheckedOut.index(bookTitle[0]) 
        returnBook = self.booksCheckedOut.pop(index)
        print(name,'has returned', returnBook)
        

    def printCheckedOutBooks(self):

        print(self.name,'has the following books checked out:')
        print(*self.booksCheckedOut,sep = '\n')

     
class AdultPatron(LibraryPatron):
    def __init__(self, name):
        LibraryPatron.__init__(self, name)
        self.checkOutLimit = 4 

    def checkOutBook(self ,bookTitle):
        checkOutLimit = self.checkOutLimit
        LibraryPatron.checkOutBook(self, checkOutLimit ,bookTitle)
        
        
class JuvenilePatron(LibraryPatron):
    def __init__(self, name):
        LibraryPatron.__init__(self, name)
        self.checkOutLimit = 2 
        
                  
    def checkOutBook(self, bookTitle):
        name = self.name
        if bookTitle[1] == 'Adult':
            print('Sorry', name, bookTitle[0],'is an Adult book')
        else:
            checkOutLimit = self.checkOutLimit
            LibraryPatron.checkOutBook(self, checkOutLimit, bookTitle)
        
        

book1 = ["Alice in Wonderland", "Juvenile"]
book2 = ["The Cat in the Hat", "Juvenile"]
book3 = ["Harry Potter and the Sorcerer's Stone", "Juvenile"]
book4 = ["The Hobbit", "Juvenile"]
book5 = ["The Da Vinci Code", "Adult"]
book6 = ["The Girl with the Dragon Tattoo", "Adult"]

patron1 = JuvenilePatron("Jimmy")
patron2 = AdultPatron("Sophia")

patron1.checkOutBook(book6)
patron1.checkOutBook(book1)
patron1.checkOutBook(book2)
patron1.printCheckedOutBooks()
patron1.checkOutBook(book3)
patron1.returnBook(book1)
patron1.checkOutBook(book3)
patron1.printCheckedOutBooks()
patron2.checkOutBook(book5)
patron2.checkOutBook(book4)
patron2.printCheckedOutBooks()


