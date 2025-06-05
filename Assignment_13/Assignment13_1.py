class bookstore:

    Noofbooks = 0

    def __init__(self,a,b):
        bookstore.Noofbooks = bookstore.Noofbooks + 1
        self.name = a
        self.author = b

    def display(self):
        print("Name of books :", self.name )
        print("Name of Author :", self.author)
        print ("Number of books : ", bookstore.Noofbooks)

def main():

    obj1 = bookstore ("Linux system programming" , "Robert love")
    obj1.display()

    obj2 = bookstore (" C programming", "Dennis Ritchie")
    obj2.display()

if __name__=="__main__":
    main()    


