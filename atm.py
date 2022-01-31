# Creating an bank account through online.
import os
import random
from PIL import Image
class account:
    def __init__(self):
        print("Accounts we have in our bank are Current,savings,recurring deposit and fixed deposit")
        self.h=input("If you need any help(Genaral details of each account):")
        if(self.h =='yes'):
            print("""    1. Current account                           
            A current account is a deposit account for traders, business owners, and entrepreneurs, who need to make and
            receive payments more often than others. These accounts hold more liquid deposits with no limit on the number
            of transactions per day. Current accounts allow overdraft facility, that is withdrawing more than what is 
            currently available in the account. Also, unlike savings accounts, where you earn some interest, these are 
            zero-interest bearing accounts. You need to maintain a minimum balance to be able to operate current accounts.
    2. Savings account 
            A savings bank account is a regular deposit account, where you earn a minimum rate of interest. Here, the 
            number of transactions you can make each month is capped. Banks offer a variety of Savings Accounts based on
            the type of depositor, features of the product, age or purpose of holding the account, and so on.
            There are regular savings accounts, savings accounts for children, senior citizens or women, institutional 
            savings accounts, family savings accounts, and so many more.You have the option to pick from a range of 
            savings products. There are zero-balance savings accounts and also advanced ones with features like auto 
            sweep, debit cards, bill payments and cross-product benefits.A cross-product benefit is when you have a 
            savings account with a bank and get to avail special offers on opening a second account such as a demat account.
    3.Fixed deposit account
            To park your funds and earn a decent rate of interest on it, there are different types of accounts like fixed
            deposits and recurring deposits.A fixed deposit (FD) account allows you to earn a fixed rate of interest for
            keeping a certain sum of money locked in for a given time, that is until the FD matures. FDs range between a
            maturity period of seven days to 10 years. The rate of interest you earn on FDs will vary depending on the 
            tenure of the FD. Generally, you cannot withdraw money from an FD before it matures. Some banks offer a 
            premature withdrawal facility. But in that case, the interest rate you earn is lower.
    4. Recurring deposit account
            A recurring deposit (RD) has a fixed tenure. You need to invest a fixed sum of money in it regularly -- every 
            month or once a quarter -- to earn interest. Unlike FDs, where you need to make a lump sum deposit, the sum 
            you need to invest here is smaller and more frequent. You cannot change the tenure of the RD and the amount 
            to be invested each month or quarter. Even in the case of RDs, you face a penalty in the form of a lower 
            interest rate for premature withdrawal. The maturity period of an RD could range between six months to 10 years.""")
        self.name=input("Enter the Legal name:")
        self.address=input("Permanent Address:")
        self.ph=int(input("Phone no:"))
        self.mail=input("Mail-id:")
        self.dob=input("Data of Birth:")
        self.nation=input("Nationality:")
        self.occup=input("Occupation:")
        self.salary=int(input("Salary per Annum:"))
        self.ac_type = input("AC Type:")
        self.sign=input("Signature:")
        self.date=input("Date(open):")
        print('''1.Current AC\n2.Savings AC\n3.Recurring Deposit AC\n4.Fixed Deposit AC''')
        self.type = int(input("What type of account you need to create:"))
        if (self.type == 1):
            self.current()
        elif (self.type == 2):
            self.savings()
        elif (self.type == 3):
            self.recurring()
        elif (self.type == 4):
            self.fixed()
        else:
            print("Invalid option")
    def current(self):
        print("NOTE:For current account Interest is 0%.No Interest is there for current account.")
        self.proof()
        self.comp_add=input("Enter the company permanent Address:")
        self.com_turn=int(input("Company Turnover:"))
        self.comp_size=input("Company size:")
        while(True):# INFINITE LOOP
            try:
                self.coi = input("Upload the certificate of incorporation of your company:")
                self.coi_img = Image.open(self.coi)
                self.coi_img.show()
                self.brc=input("Upload the Business registeration certificate:")
                self.brc_img=Image.open(self.brc)
                self.brc_img.show()
                break
            except:
                print("Incorrect filename or format:Upload the files with correct file name and with their format.")
                continue
        self.owner=input("Ownership(mention no):")
        self.lab=int(input("How many labours working in your company:"))
        while(True):
            self.pay=int(input("Credit an amount of Rs.5000 as minimum balance in your account:"))
            if(self.pay>=5000):
                print("Transaction is successfull")
                print("Net.Balance in your account:{}".format(self.pay))
                break
            elif(self.pay<5000):
                print("The amount you credited is lower than the minimum balance.Minimum balance of an account is Rs.5000")
                continue
            else:
                print("Invalid Entry")
                continue
        self.detail()
    def savings(self):
        print("NOTE:Interest for saving account is 4% in our bank.You can check it..")
        self.calc=input("You need Interest calculator for saving account:")
        if(self.calc=='yes'):
            self.amount=int(input("Enter the amount:"))
            self.duration=int(input("For how many months you need to calculate:"))
            self.rate=int(input("Enter the rate of Interest(percentage):"))
            self.interest=self.amount*(self.rate/100)*(self.duration/12)
            print("Interest:{}".format(self.interest))
        self.proof()
        while (True):
            self.pay = int(input("Credit an amount of Rs.2000 as minimum balance in your account:"))
            if (self.pay >= 2000):
                print("Transaction is successfull")
                print("Net.Balance in your account:{}".format(self.pay))
                break
            elif (self.pay < 2000):
                print(
                    "The amount you credited is lower than the minimum balance.Minimum balance of an account is Rs.2000")
                continue
            else:
                print("Invalid Entry")
        self.detail()
    def recurring(self):
        print("NOTE:For this RD account you should monthly pay an amount.")
        print("NOTE:Interest for rd account is 6% in our bank.You can check it:")
        self.calc=input("You need Interest Calculator for Recurring deposit:")
        if(self.calc=='yes'):
            self.pa=int(input("Enter the amount you monthly pay:"))
            self.rate=int(input("Enter the rate of Interest(percentage):"))
            self.nom=int(input("Enter the number of months:"))
            self.rd=(self.pa*self.nom*(self.nom+1)*self.rate)/(2*12*100)
            self.total=self.pa*self.nom+self.rd
            print("Interest:{}".format(self.rd))
            print("Your Total amount including interest(maturity tenure):{}".format(self.total))
        self.proof()
        while (True):
            self.pay = int(input("Credit an amount of Rs.100 as minimum balance in your account:"))
            if (self.pay >= 100):
                print("Transaction is successfull")
                print("Net.Balance in your account:{}".format(self.pay))
                break
            elif (self.pay < 100):
                print("The amount you credited is lower than the minimum balance.Minimum balance of an account is Rs.100")
                continue
            else:
                print("Invalid Entry")
                continue
        print("Read the Instructions and Terms & Conditions")
        os.startfile("recurring.txt")
        self.detail()
    def fixed(self):
        print("NOTE:Fixed deposit is a one-time investment.Depositing the money"
              "on monthly basis is not an option.")
        self.fd=input("You need Interest Calculator for Fixed deposit:")
        if(self.fd=='yes'):
            self.am=int(input("Enter the amount:"))
            self.inte=int(input("Rate of Interest(percentage:"))
            self.In=(self.am*self.inte)/(100)
            print("Interest:{}".format(self.In))
            print("Total Amount:{}".format(self.am+self.In))
        self.proof()
        while (True):
            self.pay = int(input("Credit an amount of Rs.5000 as minimum balance in your account:"))
            if (self.pay >= 5000):
                print("Transaction is successfull")
                print("Net.Balance in your account:{}".format(self.pay))
                break
            elif (self.pay < 5000):
                print(
                    "The amount you credited is lower than the minimum balance.Minimum balance of an account is Rs.5000")
                continue
            else:
                print("Invalid Entry")
                continue
        self.detail()
    def proof(self):
        while (True):
            try:
                self.pan = input("Upload the PAN scanned copy:")
                self.pan_img = Image.open(self.pan)
                self.pan_img.show()
                self.aadhar = input("Upload the AADHAR scanned copy:")
                self.aadhar_img = Image.open(self.aadhar)
                self.aadhar_img.show()
                self.photo = input("Upload the Photo(passport size):")
                self.photo_img = Image.open(self.photo)
                self.photo_img.show()
                break
            except:
                print("Incorrect filename or format:Upload the files with correct file name and with their format.")
                continue
    def detail(self):
       while (True):
            self.i = 1
            self.captcha = ''
            while (self.i <= 5):
                self.captcha += chr(random.randint(65, 90))
                self.i += 1
            self.cap = input("Enter the captcha {}:".format(self.captcha))
            if (self.cap == self.captcha):
                print("Loading.....................")
                print("All the details are valid")
                print("Account is successfully created")
                print("ACCOUNT DETAILS:")
                print("                        SWIZZ BANK US                        ")
                print("Current Account")
                self.ac_no = random.randint(10000000000, 99999999999)
                self.cif_no = random.randint(10000000000, 99999999999)
                self.ifsc = 'SWIZ' + str(random.randint(1000000, 9999999))
                print("CIF No:{}".format(self.cif_no))
                print("AC No:{}".format(self.ac_no))
                print("IFSC Code:{}".format(self.ifsc))
                print("Phone No:{}".format(self.ph))
                print("Address:{}".format(self.address))
                print("Mail-id:{}".format(self.mail))
                print(
                    "Note:Cheque book and ATM Card will be sent through post according to your permanent address/company address.")
                break
            else:
                print("Captcha is wrong")
                print("Wait captcha will regenerate....")
                continue
            break


    @staticmethod
    def end():
        print("***Thank you for visiting***")
        print("For further details you can visit our head quater or near to our branch..")
        print("Address:285 Avenue of the Americas "
              "New York, NY 10019 United States")
print("                                                Welcome to Swizz Bank US\n                                             ")
print("Swizz Bank Corp/NY is a full-service bank. The bank accepts deposits,"
      " makes loans and provides other services for the public.")
print("**********Create an account**********")
ac=account()
ac.end()



