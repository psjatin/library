import csv
# import txtfile
import time
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
    with open("csv_file.csv", "w", newline="") as file:
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
        print("Recheck The Record:- ", book_info)
        w_o.writerow(book_info)

def writetext():
    """Function to clear and rewrite in the main issuer file...."""
    with open("issuer.txt", "w") as file:
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")        #will give time while recording entry
        tim = formatted_time
        print("\nName of Issuer")
        nameissuer = input(":-")
        print("\nContact details *Mobile Number*")
        contact = int(input(":-"))

        boo_k.issuer(nameissuer, contact, bookid)
        a = boo_k.issuerinfo()
        print("Recheck Issuer Record:- ", boo_k.issuerinfo() + "\n")
        file.write(formatted_time + "\n\t")
        file.write(a)
        file.write("\n")


def appendcsv():
    """Function helps append in records in the file..."""
    with open("csv_file.csv","a",newline="") as file:
        # writer object creation
        w_o = csv.writer(file,delimiter="#")
        addmenu()
        global newboo_k
        global newbookid
        print("\nBook Id")
        newbookid = int(input(":-"))
        print("\nName of Book Issued")
        newbook = input(":-")
        print("\nCurrent issue price")
        newprice = int(input(":-"))
        newboo_k = Library(newbookid,newbook,newprice)
        newboo_kinfo = newboo_k.bookinfo()
        print("Recheck The Record:- ",newboo_kinfo)
        w_o.writerow(newboo_kinfo)
def appendtext():
    """Funtion storing issuer data in the textfile..."""
    with open("issuer.txt","a") as file:
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
        tim = formatted_time
        print("\nName of Issuer")
        nameissuer = input(":-")
        print("\nContact details *Mobile Number*")
        contact = int(input(":-"))

        newboo_k.issuer(nameissuer, contact, newbookid)
        a = newboo_k.issuerinfo()
        print("Recheck Issuer Record:- ", a + "\n")
        file.write(formatted_time + "\n\t")
        file.write(a)
        file.write("\n")

def fileclean():
    """pocket funtion to clean files"""
file = open("csv_file.csv","w",newline="")
file.close()
file2 = open("issuer.txt","w")
file2.close()

def readcsv():
    """Reading book record..."""
    with open("csv_file.csv","r",newline= "") as file:
        # reader object
        r_o = csv.reader(file,delimiter="#")
        for row in r_o:
            print(row)

def readtext():
    """Reading issuer records..."""
    with open("issuer.txt","r") as file:
        for line in file:
            print(line.strip())


def searchcsv(ask):
    """Function to search book record..."""
    with open("csv_file.csv","r",newline="") as file:
        searched = False
        list_objects = []          #empty list
        r_o = csv.reader(file,delimiter= "#")
        for row in r_o:
            list_objects.append(row)
        # ask = input("Enter Book Id to be searched:-")
        for i in list_objects:
            if i[0] == str(ask):
                print(i)
                searched = True
        if not searched:
            print("Record is not present...")

def searchtext(ask):
    with open("issuer.txt","r") as file:
        emp_list = []
        searched = False
        for line in file:
            emp_list.append(line.strip())
        for i in emp_list:
            if str(ask) in i:
                print(i)
                searched = True
