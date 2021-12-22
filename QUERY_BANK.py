import datetime
import random as r
import math 

x=r.randint(100000000,999999999)
#user=input("Enter 1 for old user and enter 2 for new user:")
#button 1 for existing user button 2 for new user 

'''
# existing user:
    enter account number and name 
    then it should show my fixed / recurring deposits 
# new user 
    Asks to enter name account number is generated 
    then asks if fixed or recurring :
        fixed:
            amount 
            time 
            rate- we must set
        recurring:
            monthly( only monthly) deposit 
            rate -  set by us 
            time     



'''

class BankAccount:
        def __init__(self,name,accno):
            self.name=name
            self.accno=accno
        # def welcome(self):
        #     print("Welcome",self.name,"how are you doing! Your account number is:",self.accno)
            
            
####################################################################

class FixedDeposit(BankAccount):
    
    
        def __init__(self,name,accno,duration,amount,rate_of_interest):
            BankAccount.__init__(self,name,accno)
            self.duration=duration
            self.amount=amount
            self.rate_of_interest=rate_of_interest
            
        def display(self):
            A=self.amount+((self.amount*self.duration*self.rate_of_interest)/100)
            # print("===========================Query Bank============================")
            now = datetime.datetime.now()
            time=now.strftime("%Y-%m-%d %H:%M:%S")
            bill= open("User.txt", "a+")

            disp="\n ============================================================\n Hello",'\t',str(self.name),'\n',"Welcome , your account number is :",str(self.accno),'\n',"Your deposited amount is :",str(self.amount),'\n\t',"Your interest rate on fixed deposit is :",str(self.rate_of_interest),'%','\n\t',"Your duration of payment is :",str(self.duration),'years','\n\t',"Your duration starts from :",time,'\n\t',"Your FD for the tenure ",str(self.duration)," years is :",str(A),"\n ============================================================"
            d=disp
            disp1=self.accno
            bill.writelines(d)
            
            
            b=open(str(disp1) + '.txt','w')
            
            S=str("Details of Account number :" + str(disp1))
            
            b.writelines(S)
            b.writelines('\n')
            b.writelines("\n ***********************FIXED DEPOSIT*********************** \n")
            b.writelines(d)
            b.close()
            bill.close()

            
            
            print("Hello",self.name,"Welcome , your account number is :",self.accno)
            print("Your deposited amount is :",self.amount)
            print("Your interest rate on fixed deposit is :",self.rate_of_interest,'%')
            print("Your duration of payment is :",self.duration,'years')
            print("Your duration starts from :",time)
            print("Your FD for the tenure",self.duration,"years is :",A)
            print("====================================================================")
            
####################################################################



class RecurringDeposit(BankAccount):
        def __init__(self,name,accno,duration,monthly_payment,rate_of_interest):
            BankAccount.__init__(self,name,accno)
            self.monthly_payment=monthly_payment
            self.duration=duration
            self.rate_of_interest=rate_of_interest

            
        def display(self):
            A=(self.monthly_payment)*(1+math.pow(self.rate_of_interest,self.duration))
            N=(self.duration)/7
            A=(self.monthly_payment)*math.pow((1+(self.rate_of_interest/N)),(N*self.duration))
            
            print("===========================QUERY BANK============================")
            now = datetime.datetime.now()
            time=now.strftime("%Y-%m-%d %H:%M:%S")
            bill= open("User.txt", "a+")
            #disp1="Account Number :",str(self.accno)
            disp="\n Hello",'\t',str(self.name),'\n',"Welcome , your account number is :",str(self.accno),'\n',"Your monthly installment is :",str(self.monthly_payment),'\n\t',"Your interest rate on fixed deposit is :",str(self.rate_of_interest),'%','\n\t',"Your duration of payment is :",str(self.duration),'years','\n\t',"Your duration starts from :",time,'\n\t',"Your RD for the tenure ",str(self.duration)," years is :",str(A),"\n ====================================="
            d=disp
            disp1=self.accno
            bill.writelines(d)
            
            b=open(str(disp1) + '.txt','w')
            S=str("Details of Account number :" + str(disp1))
        
            b.writelines(S)
            b.writelines('\n')
            b.writelines("\n ***********************RECURRING DEPOSIT*********************** \n")            
            b.writelines(d)

            b.close()
            
            bill.close()
        
            
            
            print("Hello",self.name,"Welcome , your account number is :",self.accno)
            print("Your deposited amount is :",self.monthly_payment)
            print("Your interest rate on recurring deposit is :",self.rate_of_interest)
            print("Your tenure of payment is :",self.duration,"years")
            print("Your duration starts from :",time)
            print("Your RD for the tenure",self.duration,"years is :",A)
            print("====================================================================")


####################################################################


def inp_fixed():
    print("==========Welcome to Query Bank your one stop for all financial needs=========== ")
    name=input("Enter name :")
    x=r.randint(100000000,999999999)
    duration=int(input("Enter duration in years :"))
    amount=int(input("Enter amount :"))
    rate_of_interest=5.00
    user=FixedDeposit(name,x,duration,amount,rate_of_interest)
    user.display()




def inp_rec():
    print("==========Welcome to Query bank your one stop for all financial needs=========== ")
    name=input("Enter name :")
    x=r.randint(100000000,999999999)
    duration=int(input("Enter duration in years :"))
    monthly_payment=int(input("Enter amount :"))
    rate_of_interest=7.00
    user=RecurringDeposit(name,x,duration,monthly_payment,rate_of_interest)
    user.display()


####################################################################


def start():
    print("==========Welcome to Query Bank your one stop for all financial needs=========== ")
    print("Enter 1 for New User : ")
    print("Enter 2 for Old User : ")
    n=int(input("Enter your choice ::: "))
    if n==1:
        print("Enter 1 for Choosing Fixed Deposit : ")
        print("Enter 2 for Choosing Recurring Deposit : ")
        m=int(input("Enter your choice ::: "))
        if m==1:
            inp_fixed()
        if m==2:
            inp_rec()
        
    
    if n==2:

       print("====================QUERY BANK=====================")
       
       ac=int(input("Enter your account number :"))
       
       print("======================================================")
       print("\n")
       
       print("Welcome Account number  :",ac)
       
       now = datetime.datetime.now()
       time=now.strftime("%Y-%m-%d %H:%M:%S")
       
       print("\n")
       
       print("Login time is :",time)
       
       print("======================================================")
       print('\n')
       
       f=open(str(ac) + '.txt', 'r')
       
       print(f.read()) 
       
       f.close()
            
####################################################################
      
start()

















