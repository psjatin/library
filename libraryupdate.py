import csv, time
class Newrecord:
    def __init__(self):
        self.bookdetail = []
        self.issuerdetail = []
        self.timedetail = []

    def add_book(self,bookid,bookname,price):
        self.bookname = bookname
        self.bookid = bookid
        self.price = price

        self.bookdetail.append([bookid,bookname,price])

    def issuer(self,bookid,issuername,contact):
        self.bookid = bookid
        self.issuername = issuername
        self.contact = contact
        self.issuerdetail.append(f"Book id - {bookid} issued by {issuername} provided contact {contact}")

    def time(self):
        formated_time = time.strftime("%H:%M:%S %a %Y-%m-%d")
        self.timedetail.append(formated_time)

def createrecord(bookid , bookname , bookprice):
    """Simple function"""
    with open("csv_file.csv","a",newline="") as file:
        csvwriter = csv.writer(file,delimiter="#")
        a = Newrecord()
        a.add_book(bookid,bookname,bookprice)
        rec = a.bookdetail
        csvwriter.writerow(rec)

def createtextrecord(bookid,issuername,issuercontact):
    """text function"""
    with open("issuer.txt","a") as file:
        a_ = Newrecord()
        a_.time()
        a_.issuer(bookid,issuername,issuercontact)
        tim = a_.timedetail
        rec = a_.issuerdetail()
        recc = rec[0]
        print(recc)
        file.write(f"{tim} --||-- {recc}")
        file.write("\n")

while True:
    ak = int(input("Enter :-"))
    if ak == 1:
        bookid = int(input("Bookid:-"))
        bookname = input("Book Name:-")
        pri_ce = int(input("Book Price:-"))

        issuername = input("Issuer Name:-")
        isucontact = int(input("Issuer contact:-"))
        createrecord(bookid,bookname,pri_ce)
        createtextrecord(bookid,issuername,isucontact)
    else:
        break








