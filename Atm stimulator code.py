pin=1234
balance=5000
user_pin=int(input("Enter your 4 digit pin : "))
if user_pin==pin:
   choice=int(input("1.Balance checking \n2.Deposite money \n3.Withdraw money \nEnter your choice (1-3) : "))
   if choice==1:
        print("Your current balance is : ",balance,"Rs")
   elif choice==2:
    	deposite=float(input("How much you want to deposite : "))
    	print("Deposite amount",deposite)
    	print("Your old balance is : ",balance)
    	print("Your available balance is : ",balance+deposite)
   elif choice==3:
        withdraw=float(input("How much you want to withdraw : "))
        if withdraw<=balance:
           print("You withdrawn : ",withdraw,"Rs")
           print("Your available balance is:",balance-withdraw)
        else:
           print("You have insufficient money! Your available balance is",balance,"Rs only!")  
   else:
        print("Please enter valid choice")
else:
    	print("Enter valid pin number")