import csv
# import txtfile

class Library:
    def __init__(self,book_id,name_book,price_book):
        self.book_id = book_id
        self.name_book = name_book
        self.price_book = price_book

    def bookinfo(self):
        return [self.book_id,f"{self.name_book}",self.price_book]

    def issuer(self,issuer_name,issuer_contact,book_id):
        self.issuer_name = issuer_name
        self.issuer_contact = issuer_contact
        self.book_id = book_id

    def issuerinfo(self):
        return f"Book id - \"{self.book_id}\" issued by {self.issuer_name} metioned his/her contact as {self.issuer_contact}"

def addmenu():
    """Provide header before adding elements"""
    return ("WELCOME TO PORTAL....."
            "\n\tEnter Issued Book and Issuer Credentials!")
def writecsv():
    """Funtion to clear and rewrite in the main library file...."""
    with open("../../../../../Users/Shaurya Sharma/PycharmProjects/Class 11/csv file.csv", "w", newline="") as file:
        global bookid
        global boo_k
        global book_info
        w_o = csv.writer(file,delimiter="#")      # creation of csv writer object
        addmenu()
        print("\nBook Id")
        bookid = int(input(":-"))
        print("\nName of Book Issued")
        book = input(":-")
        print("\nCurrent issue price")
        price = int(input(":-"))
        boo_k = Library(bookid,book,price)                             #library object
        book_info = boo_k.bookinfo()
        w_o.writerow(book_info)

def writetext():
    """Function to clear and rewrite in the main issuer file...."""
    with open("../../../../../Users/Shaurya Sharma/PycharmProjects/Class 11/issuer.txt", "w") as file:
        print("Recheck The Record:- ", book_info)
        print("\nName of Issuer")
        nameissuer = input(":-")
        print("\nContact details *Mobile Number*")
        contact = int(input(":-"))

        boo_k.issuer(nameissuer, contact, bookid)
        a = boo_k.issuerinfo()
        print("Recheck Issuer Record:- ", boo_k.issuerinfo() + "\n")
        file.write(a)
        file.write("\n")



writecsv()
writetext()

