import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Saravana2002",
    database="kcf_hotel_db"
)
mycursor=mydb.cursor()
#mycursor.execute("create database kcf_hotel_db")
#mycursor.execute("create table details(name varchar(255),address varchar(255),booking_date varchar(255),depature_date varchar(255),roomno int)")

class hotelfarecal:

    def __init__(self,rt='',s=0,r=0,a=1800,name='',address='',booking_date='',depature_date='',rno=''):

        print ("\n\n*****WELCOME TO KCF HOTEL*****\n")
 

        self.rt=rt

        self.r=r
        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.booking_date=booking_date
        self.depature_date=depature_date
        self.rno=rno
    def inputdata(self):
       
        self.name=input("\nEnter your name:").strip().lower()
        self.address=input("\nEnter your address:").strip().lower()
        self.booking_date=input("\nEnter your check in date:").strip()
        self.depature_date=input("\nEnter your checkout date:").strip()
        self.rno=int(input("Your room no.:"))

        x="insert into details(name ,address,booking_date ,depature_date,roomno )values(%s,%s,%s,%s,%s)"
        
        y=(self.name,self.address,self.booking_date,self.depature_date,self.rno)
        mycursor.execute(x,y)
        mydb.commit()


    def roomrent(self):

        print ("We have the following rooms for you:-")

        print ("1.  class A---->rs 6000 PN\-")

        print ("2.  class B---->rs 5000 PN\-")

        print ("3.  class C---->rs 4000 PN\-")

        print ("4.  class D---->rs 3000 PN\-")

        x=int(input("Enter Your Choice Please->"))

        n=int(input("How many days you can stay:"))

        if(x==1):

            print ("you can choose class A")

            self.s=6000*n

        elif (x==2):

            print ("you can choose class B")

            self.s=5000*n

        elif (x==3):

            print ("you can choose class C")

            self.s=4000*n

        elif (x==4):
            print ("you can choose class D")

            self.s=3000*n

        else:

            print ("please choose a room")

        print ("your room rent is =",self.s,"\n")

    def restaurentbill(self):

        print("*****RESTAURANT MENU*****")

        print("1.water----->Rs20","2.tea----->Rs10","3.breakfast combo--->Rs90","4.lunch---->Rs110","5.dinner--->Rs150","6.Exit")


        while (1):

            c=int(input("Enter your choice:"))


            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+20*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+10*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+90*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+110*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+150*d

            elif (c==6):
                break
            else:
                print("Invalid option")

        print ("Total food Cost=Rs",self.r,"\n")

    

    def display(self):
        print ("******HOTEL BILL******")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.booking_date)
        print ("Check out date",self.depature_date)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.s)
        print ("Your Food bill is:",self.r)
       

        self.rt=self.s+self.r

        print ("Your sub total bill is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal bill is:",self.rt+self.a,"\n")
        self.rno+=1

            
def main():

    a=hotelfarecal()
    

    while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate roomrent")

        print("3.Calculate restaurant bill")

        print("4.Show total cost")

        print("5.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.restaurentbill()

        if (b==4):

            a.display()

        if (b==5):

            quit()



main()

        

        

















       
 