import random
import mysql.connector
mydb=mysql.connector.connect(

    host="localhost",
    user="root",
    password="Saravana2002",
    database="abc_bank_db"
)
mycursor=mydb.cursor()
#mycursor.execute("create database abc_bank_details")
#mycursore.execute("create table account_details(NAME varchar(255),Account_no varchar(255),Deposit_amount varchar(255),Withdraw_amount varchar(255),Available_balance varchar(255))")

class ATM():
    
    def __init__(self,name='',account_number='',amount=0,balance=500):
        print()
        print("************WELCOME TO ABC Bank***********")
        print()
        self.name=name,
        self.account_number=account_number,
        self.balance=balance
        self.amount=amount
    def account_detail(self):
        
        while(1):

            print("**********ACCOUNT DETAILS***********")

            self.name=input("Account holder: ").strip().lower()
            self.account_number=input("Account number: ").strip()
            print("Available balance: Rs.",self.balance)
            print()
            x="insert into account_details(Name,Account_no)values(%s,%s)"
            y=[self.name,self.account_number]
            mycursor.execute(x,y)
            mydb.commit()
            break
    
    def deposit_cash(self):
        while(1):

            self.amount=float(input("enter your deposit amount: Rs. "))
            
            self.balance=self.balance+self.amount
            print("current account balance: Rs.",self.balance)
            print()
            x="insert into account_details(deposit_amount)values(%s)"
            y=[self.amount]
            mycursor.execute(x,y)
            mydb.commit()
            break

    def withdraw_cash(self):
        while(1):
     
            self.amount=float(input("enter your withdraw amount: Rs. "))
            
            
            
            if  self.amount>self.balance:

                print("amount invalid!")
                print(f"your saving balance is Rs.{self.balance}")
                print("Try again... ")
                print()

            else:

                self.balance=self.balance-self.amount
                print(f"Rs.{self.amount} withdraw to your account")
                print("your balance is RS.",self.balance)
                print()
                x="insert into account_details(withdraw_amount)values(%s)"
                y=[self.amount]
                mycursor.execute(x,y)
                mydb.commit()
            
                break   

    def check_balance(self):
        while(1):
            print("Available balance: Rs.",self.balance)
            print() 
            x="insert into account_details(available_balance)values(%s)"
            y=[self.balance]
            mycursor.execute(x,y)
            mydb.commit()
            break
    
    def print_recipt(self):
        while(1):
            
            print("************ABC Bank***********")
            print()
            print("transaction number: ",{random.randint(10000,1000000)})
            print()
            print(f"account holder: {self.name}")
            print()
            print(f"Account number: {self.account_number}")
            print()
            print("Available balance: Rs.",self.balance)
            print()
            break
        
            

def main():

     
    a=ATM()

    while(1):
        
        print("***********TRANSACTIONS*************")
        print("1. account details")
        print("2. deposit")
        print("3. withdraw")
        print("4. check balance")
        print("5. print recipt")
        print("6. exit")
        print()

        d=int(input("enter your choice->"))
    
    
        if d==1:
            a.account_detail()
                
        elif d==2:
            a.deposit_cash()

        elif d==3:
            a.withdraw_cash()

        elif d==4:
            a.check_balance()

        elif d==5:
            a.print_recipt()

        elif d==6:
            quit()
        

            

def verify():
    
    pin=1234
    
    password=int(input("enter your pin:"))
    
    if pin==password:
       print("your pin is matched")
       main()
    
    else:
        print("error! your pin is not matched")
          




verify()           

    