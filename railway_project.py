import random
import pickle
import sys


signed_in=False #global variable
user_id = 0
password=''


class train:
    def __init__(self,name='',num=0,arr_time='',dep_time='',src='',des='',day_of_travel='',seat_present_in_1AC=0,seat_present_in_2AC=0,seat_present_in_SL=0,fare_1ac=0,fare_2ac=0,fare_sl=0):
        self.name=name
        self.num=num
        self.arr_time=arr_time
        self.dep_time=dep_time
        self.src=src
        self.des=des
        self.day_of_travel=day_of_travel
        self.seats={'1AC':seat_present_in_1AC,'2AC':seat_present_in_2AC,'SL':seat_present_in_SL}
        self.fare={'1AC':fare_1ac,'2AC':fare_2ac,'SL':fare_sl}
    def print_seat_availability(self):
        print("number of seats available in 1AC:-"+str(self.seats['1AC']))
        print("number of seats available in 2AC:-"+str(self.seats['2AC']))
        print("number of seats available in SL:-"+str(self.seats['SL']))
    def check_availability(self,coach='',ticket_num=0):
        coach=coach.upper()
        if coach not in ('SL','1AC','2AC'):
            print_seat_availability()
            coach = input("Enter the coach(1AC/2AC/SL) :-")
        else:
            if self.seats[coach]==0:
                return False
            elif self.seats[coach]>=ticket_num:
                return True
            else:
                return False
    def book_tickets(self,coach='',no_of_tickets=0):
        self.seats[coach]-=no_of_tickets
        return True
class ticket:
    def __init__(self,train,user,ticket_num,coach):
        self.pnr=str(train.num)+str(user.user_id)+str(random.randint(100,999))
        self.train_num=train.num
        self.coach=coach
        self.user_id=user.user_id
        self.train_name=train.name
        self.user_name=user.name
        self.ticket_num=ticket_num
        user.history.update({self.pnr:self})
        ticket_dict.update({self.pnr:self})

class user:
    def __init__(self,user_id=0,name='',hometown='',cell_num='',password=''):
            self.user_id=user_id
            self.name=name
            self.hometown=''
            self.cell_num=''
            self.password=password
            self.history={}
class acceptors:
    '''class containing functions for accepting and
    validating values properly'''
    def accept_user_id():
        user_id=0
        try:
            user_id=int(input("Enter the user_id:-"))
        except ValueError:
            print("please enter user_id properly.")
            return acceptors.accept_user_id()
        else:
            return user_id
    def accept_password():
        password=input("Enter your password:-")
        return password 
    
    def accept_train_num():
        train_num=0
        try:
            train_num=int(input("Enter the train number:-"))
        except ValueError:
            print("please enter the train number properly.")
            return acceptors.accept_train_num()
        else:
            return train_num
        

    def accept_menu_option():
        option=input("Enter your option:-")
        if option not in ('1','2','3','4','5','6','7','8'):
            print("please enter a valid option.")
            return acceptors.accept_menu_option()
        else:
            return int(option)
        
    def accept_coach():
        coach=input("Enter the coach:-")
        coach=coach.upper()
        if coach not in ('SL','1AC','2AC'):
            print("please enter coach properly.")
            return acceptors.accept_coach()
        else:
            return coach
    def accept_prompt():
        prompt=input("confirm?(y/n) :-")
        if prompt not in('y','n'):
            print("please enter the proper choice.")
            return acceptors.accept_prompt()
        return prompt
    def accept_ticket_num():
        ticket_num=0
        try:
            ticket_num=int(input("Enter the number of tickets:-"))
            if ticket_num<0:
                raise ValueError
        except ValueError:
            print("Enter proper ticket number.")
            return acceptors.accept_ticket_num()
        else:
            return ticket_num
    def accept_pnr():
        pnr=input("Enter your PNR number:-")
        if pnr not in ticket_dict:
            print("please enter the correct PNR number:-")
            return acceptors.accept_pnr()
        else:
            return pnr
def book_ticket():
        if not signed_in:
            login('p')
        check_seat_availability('p')
        choice=acceptors.accept_train_num()
        trains[choice].print_seat_availability()
        coach=acceptors.accept_coach()
        ticket_num=acceptors.accept_ticket_num()
        if trains[choice].check_availability(coach,ticket_num):
            print("You have to pay:-",trains[choice].fare[coach]*ticket_num," ")
            prompt=acceptors.accept_prompt()
            if prompt=='y':
                trains[choice].book_ticket(coach,ticket_num)
                print("Booking successful!\n\n")
                tick=ticket(trains[choice],users[user_id],ticket_num,coach)
                print("Please note PNR number:-",tick.pnr,"\n\n")
                menu()
            else:
                print("Exciting...\n\n")
                menu()
        else:
            print(ticket_num,"tickets are not available")
            menu()
def cancel_ticket():
    pnr=acceptors.accept_pnr()
    if pnr in ticket_dict:
        check_pnr(pnr)
        print("Cancel the tickets?")
        prompt=acceptors.accept_prompt()
        if prompt=='y':
            if signed_in:
                print("Ticket cancelled.\n")
                trains[ticket_dict[pnr].train_num].seats[ticket_dict[pnr].coach]+=ticket_dict[pnr].train_num
                del users[ticket_dict[pnr].user_id].history[pnr]
                del ticket_dict[pnr]
            else:
                login('p')
                print("Ticket cancelled.\n")
                trains[ticket_dict[pnr].train_num].seats[ticket_dict[pnr].coach]+=ticket_dict[pnr].train_num
                del users[ticket_dict[pnr].user_id].history[pnr]
                del ticket_dict[pnr]
        else:
            print("\nTicket not cancelled\n")
    menu()
def check_seat_availability(flag=""):
    src=input("Enter the source station:-")
    des=input("Enter the destination station:-")
    flag_2=0
    for i in trains:
        if trains[i].src==src and trains[i].des==des:
            print("Train name:-",trains[i].name," ","number",trains[i].num," ","Day of Travel:-",trains[i].day_of_travel)
            flag_2+=1
    if flag_2==0:
        print("\nNo trains found between the stations you entered.\n")
        menu()
    if flag=="":
        train_num=acceptors.accept_train_num()
        trains[train_num].print_seat_availability()
        menu()
    else:
        pass
def check_pnr(pnr=''):
    if pnr=='':
        pnr=acceptors.accept_pnr()
        print()
        print("User name:-",ticket_dict[pnr].user_name)
        print("Train name:-",ticket_dict[pnr].train_name)
        print("Train number:-",ticket_dict[pnr].train_num,"source:-",trains[ticket_dict[pnr].train_num].src,"Destination:-",trains[ticket_dict[pnr].train_num].des)
        print("no.of tickets booked:-",ticket_dict[pnr].ticket_num)
        print()
def create_new_acc():
    user_name=input("Enter your name:-")
    password=input("Enter your password:-")
    user_id=random.randint(1000,9999)
    hometown=input("Enter your hometown:-")
    cell_num=input("Enter your phone number:-")
    u=user(user_id,user_name,hometown,cell_num,password)
    print("your user Id is:-",user_id)
    users.update({u.user_id:u})
    menu()

def login(flag=''):
    global user_id
    global password
    user_id=acceptors.accept_user_id()
    password=acceptors.accept_password()
    if user_id in users and users[user_id].password==password:
        print("\nWelcome ",users[user_id].name,"!\n")
        global signed_in
        signed_in=True
    else:
        print("\nNo such user Id/Wrong password!\n")
        return login()
    if flag=='':
        menu()
    else:
        pass
def check_prev_bookings():
    if not signed_in:
        login('p')
    for i in users[user_id].history:
        print("\nPNR number=",i)
        check_pnr(i)
    menu()
def end():
    s()
    print("----------------------------------------THANKING YOU!----------------------------------------")
    print("---------------------------------------------------------------------------------------------")
    sys.exit()

t1=train('odisha',12345,'12:34','22:12','ctc','kgp','wed',30,23,43,2205,320,234)
t2=train('howrah',1265,'02:34','hwr','kol','mon',33,4,12,3434,435,234)
t3=train('bangalore',22353,'11:56','3:12','ctc','ban','fri',33,24,77,455,325,533)
trains={t1.num:t1,t2.num:t2,t3.num:t3}
u1=user(1111,'uday','guntur','7995344856','uday')
u2=user(1212,'rajesh','bangalore','9848320123','rajesh')
users={u1.user_id:u1,u2.user_id:u2}
ticket_dict={}


def load():
	global  trains,users,ticket_dict
	with open("data.pkl","rb") as f:
		trains = pickle.load(f)
		users = pickle.load(f)
		ticket_dict = pickle.load(f)




def s():
	with open("data.pkl","wb") as f:
		pickle.dump(trains,f)
		pickle.dump(users,f)
		pickle.dump(ticket_dict,f)




print("-----------------------------------------WELCOME TO RAILWAY RESERVATION PORTAL-------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------")
load()


def menu():
    print("choose one of the following option:-")
    print("1.Book tickets")
    print("2.Cancel tickets")
    print("3.Check PNR")
    print("4. Check seat availabity")
    print("5.Creat new account")
    print("6.Check previous bookings")
    print("7.Login")
    print("8.Exit")
    func={1:book_ticket,2:cancel_ticket,3:check_pnr,4:check_seat_availability,5:create_new_acc,6:check_prev_bookings,7:login,8:end}
    option=acceptors.accept_menu_option()
    func[option]()

menu()