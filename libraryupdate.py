import csv, time
class Newrecord:
    def __init__(self):
        self.bookdetail = []
        # self.issuerdetail = []
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
        return f"Book id - {bookid} issued by {issuername} provided contact {contact}"

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
        player = Newrecord()
        player.time()
        rec = player.issuer(bookid,issuername,issuercontact)
        tim = player.timedetail
        print("\n-----"+rec)
        file.write(f"{tim[0]} --||-- {rec}")
        file.write("\n")

def searchcsv(bookid,bookname,bookdate):
    """function to search record..... """
    f = open("csv_file.csv","r")
    v = open("issuer.txt","r")
    lis_csv = []             #input append from csv file
    lis_txt = []             #input append from text file
    searchedcsv = False
    searchtext = False
    r_o = csv.reader(f,delimiter="#")
    vread = v.readlines()
    for row in r_o:
        print(row)    #123
        if row[0] == bookid and row[1] == bookname:
            lis_csv.append(row)
            searchedcsv = True
    for row2 in vread:
        a = row2.split(" ")
        print(a)
        if a[2] == bookdate and a[7] == bookid:
            searchtext = True
            lis_txt.append(a)

    if searchedcsv and searchtext:
        print("Found..")
        for i in lis_csv:
            print(i)
        for i in lis_txt:
            print(i)
    else:
        print("Not Found Fortunately")

    f.close()
    v.close()


searchcsv(456,"Shawshank Khushi","2024-08-01")








