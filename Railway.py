import random
class Train():
    def __init__(self,train_num,source,destination,seats):
        self.train_num=train_num
        self.source=source
        self.destination=destination
        self.seats=seats
    
    def display_info(self):
        print(f"Train number:{self.train_num}")
        print(f"source:{self.source}")
        print(f"destination:{self.destination}")
        print(f"Available seats:{self.seats}")
        print() 

    def book_tickets(self,num_tickets):
        if num_tickets >self.seats:
            return None
        else:
            pnr_list=[]
            for i in range(num_tickets):
                pnr_list.append(random.randint(5000,10000))
            self.seats -=num_tickets
            return pnr_list
class Passenger:
    def __init__(self,name,age,gender,phone):
            self.name=name
            self.age=age
            self.gender=gender
            self.phone=phone
        
    def display_info(self):
            print(f"Name:{self.name}")
            print(f"Age:{self.age}")
            print(f"Gender:{self.gender}")
            print(f"Phone:{self.phone}")
           
class Ticket:
    def __init__(self,train,source ,destination,passengers,pnr):
        self.train=train
        self.source=source
        self.destination=destination
        self.passengers=passengers
        self.pnr=pnr
    
    def display_info(self):
        print(f"Train number:{self.train.train_num}")
        print(f"source:{self.source}")
        print(f"Destination:{self.destination}")
        print(f"PNR:{self.pnr}")
        for passenger in self.passengers:
            passenger.display_info()
        print()

class Account:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    
    def check_password(self,password):
        return self.password ==password

accounts=[
    Account("user1","password1"),
    Account("user2","password2")
]
logged_in_account=None

while True:
    print("1.create an account")
    print("2.Login")
    choice =input( "Enter choice:")
    if choice == "1":
        username =input("Enter username:")
        password = input("Enter password :")
        accounts.append(Account(username,password))
        
        print("Account created successfully !")
    
    elif choice == "2":
        username = input("Enter username:")
        password = input("Enter password :")
        for account in accounts:
            if account.username == username and account.check_password(password):
                logged_in_account=account
                break
        if logged_in_account is None:
            print("Invalid username or password")

        else:
            print(f"logged in as {logged_in_account.username} \n---available train detailes---\n")
            break
    
    else:
        print("Invalid choice:")

if logged_in_account is not None:
    trains=[
        Train("24357","Bhimavaram","Rajahmundry",30),
        Train("35689","Chennai","Vizag",60),
        
    ]


for train in trains:
    train.display_info()



while True:
    try:
        Train_num=input("Enter Train number:")
        num_tickets=int(input("Enter Number of tickets:"))
        if num_tickets <=0:
            raise ValueError("Number of tickets should be greater than 0")
        for train in trains:
            if train.train_num == Train_num:
                if num_tickets>train.seats:
                    raise ValueError("selected more tickets than availabe seats")
                break
        
        else:
            raise ValueError("Invalid Train number.")
        break
    except ValueError as e:
        print(f"Invalid Input:",{e})
       
train=None
for t in trains:
    if t.train_num == Train_num:
        train=t
        break

if train is None:
    print("Invalid Train number:")
else:
    Passengers =[]
    for i in range(num_tickets):
        print(f"\n Enter detailes for passesnger {i+1}:")
        while True:
            try:
                name =input("Name:")
                if not name:
                    raise ValueError("Name cannot be empty")
                age=int(input("Age:"))
                if age <=0 or age>120:
                    raise ValueError("Invalid Age")
                gender=input("Gender:")
                phone =input("Phone number:")
                if not phone or len(phone) !=10 or not phone.isdigit():
                    raise ValueError("Invalid phone number:")
                passenger=Passenger(name,age,gender,phone)
                Passengers.append(passenger)
                break
            except ValueError as e:
                print(f"Invalid input:{e}")

    pnr_list=train.book_tickets(num_tickets)
    if pnr_list is None:
        print("Tickets not available:")
    else:
        print("\n------ Booking Successful----\n\n your ticket detailes: \n")

        for i in range(num_tickets):
            ticket=Ticket(train,train.source,train.destination,[Passengers[i]],pnr_list[i])
            ticket.display_info()
            print(" \n --- Thank you --- \n ")
