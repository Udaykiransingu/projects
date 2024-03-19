print("."*40)
#customers_details
Customer_name=["Ajay","sudheer","sivakumar","ravi","Sai"]
Customer_pin=[1243,6543,8765,4123,2341]
Balance_amount_of_customer=[17000,25000,65000,37500,78000]
Depositing=0
withdraw_amount=0
Bank_balance=0
section_1=1
section_2=5
i=0
#the below lines of code will help to run  code continuously
while True:
    #os.system("cls")
    print("."*40)
    print("==========BANK OF INDIA==================")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("~~       1.Open a account              ~~")
    print("~~       2.Withdraw money              ~~")
    print("~~       3.Deposit money               ~~")
    print("~~       4.Check customers and balance ~~")
    print("~~       5.Exit/Quit                   ~~")
    #the below statement takes the option from the user (or)customer.
    Option_number=input("select any one option from the above:")
    if Option_number=="1":
        print("user selected the 1st option")
# The line below will take the no:of customers from the user.
        NOC = eval(input("Number of Customers : "))
        i=i+NOC
        # The if condition will restrict the number of new account to 5.
        if i>5:
            print("\n")
            print("the customers registration is reached maximum or customers registration is too low")
            i=i-NOC
        else:
            #the while loop will run according to the no.of custoomers.
            while section_1<=i:
                #these few lines will take the information from customer and will append to the list.
                name=input("Enter your full name:")
                Customer_name.append(name)
                pin=str(input("Enter your pin:"))
                Customer_pin.append(pin)
                Bank_balance=0
                Depositing=eval(input("please add some money to open the account:"))
                Bank_balance=Bank_balance+Depositing
                Balance_amount_of_customer.append(Bank_balance)
                print("\nName= " , end=" ")
                print(Customer_name[section_2])
                print("Pin=", end=" ")
                print(Customer_pin[section_2])
                print("Balance=", end=" ")
                print(Balance_amount_of_customer[section_2], end=" ")
                print("-/rs")
                section_1=section_1+1
                section_2=section_2+1
                print("\n your name is added to customer_details")
                print("your pin will be added to customer_details")
                print("your bank_balance will be added to customer_details")
                print("**********your account creation was successful!**********")
                print("\n")
                print("Note! remember your name and pin and donot share to anyone")
                print("..........................................................")
                 # This statement below helps the user to go back to the start of the application (main menu).
        mainMenu = input("Please press enter key to go back to mainmenu or to exit")
    elif Option_number=="2":
        j=0
        print("user selected the 2nd option")
        # This while loop will prevent the user using the account if the username or pin is wrong.
        while j<1:
            k= -1
            name=input("please Enter your name:")
            pin=input("please Enter your pin:")
            # This while loop will keep the function running when variable k is smaller than length of the
            # customerNames list
            while k<len(Customer_name)-1:
                k=k+1
                # These two if conditions find where both the name and pin matches
                if name == Customer_name[k]:
                    if pin==Customer_pin[k]:
                        j=j+1
                        # These few statement would show the balance taken from the list.
                        print("Your Current Balance:", end=" ")
                        print(Balance_amount_of_customer[k], end=" ")
                        print("-/Rs\n")
                        Bank_balance = (Balance_amount_of_customer[k])
                        # Statement below would take the amount to withdraw from user.
                        withdraw_amount=eval(input("Enter the amount to withdraw:"))
                        # The if condition below would look whether the withdraw is greater than the balance_amount_of_customer.
                        if withdraw_amount>Bank_balance:
                            # This statement below would take a depositing from the customer.
                            Depositing = eval(input(
                                "Please Deposit a higher amount because your Balance given above is not sufficient : "))
                            # These few statements would update the value and show the balance to user.
                            Bank_balance=Bank_balance+Depositing
                            print("Your current balance amount is:",end="")
                            print(Bank_balance,end="")
                            print("-/rs\n")    #1000-500=500
                            Bank_balance=Bank_balance-withdraw_amount
                            print("-\n")
                            print("**********Your money withdrawl was successful!**********")
                            Balance_amount_of_customer[k]=Bank_balance
                            print("your present balance:",Bank_balance,end="")
                            print("-/rs\n\n")
                        else:
                            # Else condition mentioned above is to do withdrawal if the balance is greater than the
                            # withdraw amount.
                            Bank_balance=Bank_balance-withdraw_amount
                            # These few statement would update the values in the list and show it to the customer.
                            print("\n")
                            print("********** Withdraw was successful! **********")
                            Balance_amount_of_customer[k]=Bank_balance
                            print("your new balance is:",Bank_balance,end="")
                            print("-/Rs\n\n")
            if j<1:
                 # The if condition above would work when the pin or the name is wrong.
                print("your name and pin was not matching!\n")
                break
             # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu=input("please enter any key to go back for main menu or to exit")
    elif Option_number=="3":
        print("user selected the 3rd option")
        n=0
        # The while loop below would work when the pin or the username is wrong.
        while n<1:
            k=-1
            name=input("please enter your name:")
            pin=input("please enter your pin:")
            # The while loop below will keep the function running to find the correct user.
            while k<len(Customer_name)-1:
                k=k+1
                 # The two if conditions below would find whether both the pin and the name is correct.
                if name==Customer_name[k]:
                    if pin==Customer_pin[k]:
                        n=n+1
                         # These statements below would show the customer balance and update list values according to
                        # the depositings made.
                        print("your current balance is:",end="")
                        print(Balance_amount_of_customer[k],end="")
                        print("-/Rs")
                        Bank_balance=(Balance_amount_of_customer[k])
                         # This statement below takes the depositing from the customers.
                        Depositing=eval(input("Enter the money you want to deposit:"))
                        Bank_balance=Bank_balance+Depositing
                        Balance_amount_of_customer[k]=Bank_balance
                        print("\n")
                        print("**********your deposit was successful!**********")
                        print("your new balance=",Bank_balance,end="")
                        print("-/Rs\n\n")
            if n<1:
                print("your name and pin was not matching!\n")
                break
             # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu=input("please enter any key to go back to mainmenu or to exit")
    elif Option_number=="4":
        print("user selcted the 4th option")
        k=0
        print("customer names and balances given below: ")
        print("\n")
        # The while loop below will keeping running until all the customers and balances are shown.
        while k <= len(Customer_name) -1:
            print("*.customer=",Customer_name[k])
            print("*.balances=",Balance_amount_of_customer[k],end="")
            print("-/Rs")
            print("\n")
            k=k+1
             # This statement below helps the user to go  to the start of the application(main menu).
        mainMenu=input("please enter any key to go back to the mainmenu or to exit")
    elif Option_number=="5":
        #the below statements will be shown to the customer.
        print("user selected the 5th option")
        print("Thank you for visiting our bank!")
        print("\n")
        print("you can come again")
        print("Bye Bye")
        break
    else:
        # This else function above would work when a wrong function is chosen.
        print("Invalid option taken by customer!")
        print("please try again")
        # This statement below helps the user to go back to the start of the application (main menu).
        mainMenu=input("please enter any key to go back to mainmenu or to exit")  


                            
                         
