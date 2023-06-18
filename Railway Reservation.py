import mysql.connector as ms
import random
conn = ms.connect(host="localhost",user="root",passwd="1234",database="users")
cur = conn.cursor()
#following commented out lines are to be executed to create tables for user details and trains. Already created in my case.
#cur.execute("create table basic_details ( userid char(50),	username char(50),	passwd	char(50) )")
#conn.commit()
#cur.execute("insert into basic_details values(0,'null','null')")
#conn.commit()
#cur.execute("create table personal_details ( userid char(50),  firstname char(50),     lastname char(50),     dob char(20),     email char(100),     phno char(20),     gender char(20) )")
#conn.commit()
#cur.execute("create table address ( userid char(50),	houseno char(50),	street	char(50),	city char(50),	pincode int(6),	state char(50) )")
#conn.commit()
#cur.execute("create table trains ( trainno int(5),  trainname char(50),     starts char(50),     ends char(50),     firstac int(7),     secondac int(7),     sleeper int(7),	time char(20) )")
#conn.commit()
#cur.execute("insert into trains values('12681', 'Coimbatore Express', 'Chennai Central', 'Coimbatore Junction', '4000', '2500', '1000', '5 Hours')")
#conn.commit()
#cur.execute("insert into trains values('19409', 'Gorakhpur Express', 'Ahmedabad Junction', 'Gorakhpur Junction', '5000', '3000', '1500', '1 Day')")
#conn.commit()
#cur.execute("insert into trains values('12869', 'Howrah Superfast Express', 'Mumbai Cst', 'Howrah Junction', '6000', '3500', '2000', '2 Days')")
#conn.commit()
#cur.execute("insert into trains values('11125', 'Ind Gwaliar Express', 'Indore Junction Bg', 'Gwalior', '4700', '2700', '900', '10 Hours')")
#conn.commit()
#cur.execute("insert into trains values('12425', 'Jammu Rajdhani', 'New Delhi', 'Jammu Tawi', '5300', '3000', '950', '10 Hours')")
#conn.commit()
def existing_users():
    cur.execute("select username from basic_details")
    users = cur.fetchall()
    return users
def signup():
    print("-----BASIC DETAILS-----")
    while True:
        exist=0
        username = input("Enter User Name: ")
        for i in existing_users():
            if username in i:
                print("Username already exists! Please enter another")
                exist=1
                break
        if exist == 0:
            break
    passwd = input("Enter Password: ")
    while True:
        confirm = input("Enter Password Again(confirm): ")
        if confirm != passwd:
            print("Confirmation password incorrect! Please try again")
        else:
            break
    cur.execute("select max(userid) from basic_details")
    userid = 1 + cur.fetchall()[0][0]
    cur.execute("insert into basic_details values({},'{}','{}')".format(userid, username, passwd))
    conn.commit()
    print("-----PERSONAL DETAILS-----")
    firstname = input("Enter First name: ")
    lastname = input("Enter Last name: ")
    dob = input("Enter Date of Birth(DD/MM/YYYY): ")
    email = input("Enter Email: ")
    phno = input("Enter Phone number: ")
    gender = input("Enter Gender: ")
    cur.execute("insert into personal_details values({},'{}','{}','{}','{}','{}','{}')".format(userid, firstname, lastname, dob,email,phno,gender))
    conn.commit()
    print("-----ADDRESS-----")
    houseno = input("Enter House no.: ")
    street = input("Enter street: ")
    city = input("Enter City: ")
    pincode = input("Enter pincode: ")
    state = input("Enter State: ")
    cur.execute("insert into address values({},'{}','{}','{}',{},'{}')".format(userid, houseno, street, city, pincode,state))
    conn.commit()
    cur.execute("create table user{} ( bookid char(7), firstname char(50), lastname char(50), phno char(20), gender char(20), trainno int(5), trainname char(50),from_ char(50), to_ char(50), date char(20), time char(50), class char(10), fare int(10) );".format(userid))
    conn.commit()
    cur.execute("insert into user{} values('{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}','{}',{})".format(userid, "null", "null","null","null","null",0,"null","null","null","null","null","null",0))
    conn.commit()
    print("Registration Successful. Please login with your user name and password.")
def signin():
    users = existing_users()
    while True:
        exist = 0
        username = input("Enter username: ")
        for i in users:
            if username in i:
                exist = 1
                break
        if exist == 0:
            print("Invalid Username! Try again")
            continue
        break
    cur.execute("select passwd from basic_details where username='{}'".format(username))
    checkpass = cur.fetchall()
    while True:
        passwd = input("Enter password:")
        if passwd != checkpass[0][0]:
            print("Wrong Password! Try Again")
            continue
        break
    cur.execute("select userid from basic_details where username='{}'".format(username))
    print("\nSIGNIN SUCCESSFUL")
    return cur.fetchall()[0][0]
def edit(userid):
    while True:
        print("1 - Password\n2 - Personal Details\n3 - Address\n4 - Exit")
        ch = int(input("Your choice(1-4): "))
        if ch == 1:
            passwd = input("Enter New Password: ")
            while True:
                confirm = input("Enter Password Again(confirm): ")
                if confirm != passwd:
                    print("Confirmation password incorrect! Please try again")
                else:
                    break
            cur.execute("update basic_details set passwd='{}' where userid={}".format(passwd,userid))
            conn.commit()
            print("Pasword Updated Successfully")
        elif ch == 2:
            while True:
                print("1 - First Name\n2 - Last Name\n3 - Date of birth\n4 - Email\n5 - Phone no.\n6 - Gender\n7 - Exit")
                ch = int(input("Your choice(1-7): "))
                if ch == 1:
                    firstname = input("Enter new First name: ")
                    cur.execute("update personal_details set firstname='{}' where userid={}".format(firstname,userid))
                    conn.commit()
                    print("First name Updated Successfully")
                elif ch == 2:
                    lastname = input("Enter new Last name: ")
                    cur.execute("update personal_details set lastname='{}' where userid={}".format(lastname,userid))
                    conn.commit()
                    print("Last name Updated Successfully")
                elif ch == 3:
                    dob = input("Enter new Date of Birth: ")
                    cur.execute("update personal_details set dob='{}' where userid={}".format(dob,userid))
                    conn.commit()
                    print("Date of Birth Updated Successfully")
                elif ch == 4:
                    email = input("Enter new email: ")
                    cur.execute("update personal_details set email='{}' where userid={}".format(email,userid))
                    conn.commit()
                    print("Email Updated Successfully")
                elif ch == 5:
                    phno = input("Enter new Phone number: ")
                    cur.execute("update personal_details set phno='{}' where userid={}".format(phno,userid))
                    conn.commit()
                    print("Phone number Updated Successfully")
                elif ch == 6:
                    gender = input("Enter new Gender: ")
                    cur.execute("update personal_details set gender='{}' where userid={}".format(gender,userid))
                    conn.commit()
                    print("Gender Updated Successfully")
                elif ch == 7:
                    break
                else:
                    print("Invalid Input! Try again")
        elif ch == 3:
            while True:
                print("1 - House No.\n2 - Street\n3 - City\n4 - Pincode\n5 - State\n6 - Exit")
                ch = int(input("Your choice(1-6): "))
                if ch == 1:
                    houseno = input("Enter new House no.: ")
                    cur.execute("update address set houseno='{}' where userid={}".format(houseno,userid))
                    conn.commit()
                    print("House no. Updated Successfully")
                elif ch == 2:
                    street = input("Enter new street: ")
                    cur.execute("update address set street='{}' where userid={}".format(street,userid))
                    conn.commit()
                    print("Street Updated Successfully")
                elif ch == 3:
                    city = input("Enter new City: ")
                    cur.execute("update address set city='{}' where userid={}".format(city,userid))
                    conn.commit()
                    print("City Updated Successfully")
                elif ch == 4:
                    pincode = int(input("Enter new Pincode: "))
                    cur.execute("update address set pincode={} where userid={}".format(pincode,userid))
                    conn.commit()
                    print("Pincode Updated Successfully")
                elif ch == 5:
                    state = input("Enter new State: ")
                    cur.execute("update address set state='{}' where userid={}".format(state,userid))
                    conn.commit()
                    print("State Updated Successfully")
                elif ch == 6:
                    break
                else:
                    print("Invalid Input! Try again")
        elif ch == 4:
            break
        else:
            print("Invalid Input! Try again")
def book(userid):
    cur.execute("select trainno, trainname, starts, ends from trains")
    trains = cur.fetchall()
    print("(TrainNo., Train Name, Start, End)")
    for i in trains:
        print(i)
    while True:
        trainno = int(input("Please enter the train no. to book: "))
        exist = 0
        for i in trains:
            if trainno in i:
                exist = 1
                break
        if exist == 0:
            print("Invalid number! Try again")
            continue
        break
    date_d = input("Enter date of departure(DD/MM/YYYY): ")
    print("Please select a class\n1 - 1A\n2 - 2A\n3 - Sleeper")
    while True:
        cell_f = int(input("Your choice(1-3): "))
        if cell_f in [1,2,3]:
            break
        print("Invalid Input!Try Again")
    if cell_f == 1:
        cell = 'firstac'
    elif cell_f == 2:
        cell = 'secondac'
    else:
        cell = 'sleeper'
    cur.execute("select {},time from trains".format(cell))
    data = cur.fetchall()
    fare = data[0][0]
    time = data[0][1]
    print("Fare(Rs.):",fare)
    print("Time of journey:",time)
    while True:
        ch = input("Are you sure you want to book the train?(y,n):")
        if ch.lower() == 'n':
            print("Train NOT booked. Returning to main menu...")
            break
        elif ch.lower() == 'y':
            letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            numbers = '0123456789'
            bookid = ""
            for i in range(7):
                num = random.choice('12')
                if num == '1':
                    bookid += random.choice(letter)
                else:
                    bookid += random.choice(numbers)
            cur.execute("select * from personal_details where userid = {}".format(userid))
            detail_1 = cur.fetchall()
            print("Ticket Booked!")
            print("Please take a printout of the following ticket")
            print("----------Ticket Details----------")
            print("Booking ID:",bookid)
            print("First Name: '{}'".format(detail_1[0][1]))
            print("Last Name: '{}'".format(detail_1[0][2]))
            print("Phone no.: '{}'".format(detail_1[0][5]))
            print("Gender: '{}'".format(detail_1[0][6]))
            cur.execute("select * from trains where trainno={}".format(trainno))
            train_detail = cur.fetchall()
            print("Train No.: {}".format(train_detail[0][0]))
            print("Train Name: '{}'".format(train_detail[0][1]))
            print("Starting Location: '{}'".format(train_detail[0][2]))
            print("Ending Location: '{}'".format(train_detail[0][3]))
            print("Date of Departure: '{}'".format(date_d))
            print("Time of Journey: '{}'".format(time))
            print("Class: '{}'".format(cell))
            print("Fare(Rs.): {}".format(fare))
            print("----------Ticket Details----------")
            cur.execute("insert into user{} values('{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}','{}',{})".format(userid, bookid, detail_1[0][1],detail_1[0][2],detail_1[0][5],detail_1[0][6],train_detail[0][0],train_detail[0][1],train_detail[0][2],train_detail[0][3],date_d,time,cell,fare))
            conn.commit()
            break
        else:
            print("Invalid answer! Try Again")
def cancel(userid):
    cur.execute("select bookid from user{}".format(userid))
    ids = cur.fetchall()
    if len(ids) == 1:
        print("You have NO reservations!\n")
        return 0
    while True:
        bookid = input("Enter the booking ID of ticket: ")
        exist = 0
        for i in ids:
            if bookid in i:
                exist = 1
                break
        if exist == 0:
            print("Booking ID not found! Try Again")
            return 0
        break
    while True:
        ch = input("Are you sure you want to cancel the ticket?(y,n):")
        if ch.lower() == 'y':
            cur.execute("delete from user{} where bookid='{}'".format(userid,bookid))
            conn.commit()
            print("Ticket cancellation successful")
            break
        elif ch.lower() == 'n':
            print("Ticket NOT cancelled. Returning to main menu...")
            break
        else:
            print("Invalid answer! Try Again")
def search(userid):
    while True:
        print("1 - Personal Details\n2 - Reservations\n3 - Printout a Ticket\n4 - Exit")
        ch = int(input("Your choice(1-4): "))
        if ch == 1:
            cur.execute("select * from personal_details where userid = {}".format(userid))
            detail_1 = cur.fetchall()
            print("First Name: '{}'".format(detail_1[0][1]))
            print("Last Name: '{}'".format(detail_1[0][2]))
            print("Date of Birth: '{}'".format(detail_1[0][3]))
            print("Email: '{}'".format(detail_1[0][4]))
            print("Phone no.: '{}'".format(detail_1[0][5]))
            print("Gender: '{}'".format(detail_1[0][6]))
            cur.execute("select * from address where userid = {}".format(userid))
            detail_2 = cur.fetchall()
            print("House no.: '{}'".format(detail_2[0][1]))
            print("Street: '{}'".format(detail_2[0][2]))
            print("City: '{}'".format(detail_2[0][3]))
            print("Pincode: '{}'".format(detail_2[0][4]))
            print("State: '{}'".format(detail_2[0][5]))
            break
        elif ch == 2:
            cur.execute("select bookid, trainno, trainname, from_, to_, date, time, class, fare from user{} where bookid not in ('null')".format(userid))
            data = cur.fetchall()
            if len(data) == 0:
                print("\nYou have NO reservations!\n")
                continue
            print("(BookingID, TrainNo., TrainName, Start, End, Date, TimeofJourney, Class, Fare(Rs.))")
            for i in data:
                print(i)
            break
        elif ch == 3:
            cur.execute("select bookid from user{}".format(userid))
            ids = cur.fetchall()
            if len(ids) == 1:
                print("\nYou have NO reservations!\n")
                continue
            while True:
                bookid = input("Enter the booking ID of ticket: ")
                exist = 0
                for i in ids:
                    if bookid in i:
                        exist = 1
                        break
                if exist == 0:
                    print("Booking ID not found! Try Again")
                    continue
                break
            cur.execute("select * from user{} where bookid='{}'".format(userid,bookid))
            data = cur.fetchall()
            print("----------Ticket Details----------")
            print("Booking ID:",bookid)
            print("First Name: '{}'".format(data[0][1]))
            print("Last Name: '{}'".format(data[0][2]))
            print("Phone no.: '{}'".format(data[0][3]))
            print("Gender: '{}'".format(data[0][4]))
            print("Train No.: {}".format(data[0][5]))
            print("Train Name: '{}'".format(data[0][6]))
            print("Starting Location: '{}'".format(data[0][7]))
            print("Ending Location: '{}'".format(data[0][8]))
            print("Date of Departure: '{}'".format(data[0][9]))
            print("Time of Journey: '{}'".format(data[0][10]))
            print("Class: '{}'".format(data[0][11]))
            print("Fare(Rs.): {}".format(data[0][12]))
            print("----------Ticket Details----------")
            break
        elif ch == 4:
            break
        else:
            print("Invalid option")
def after_signin(userid):
    while True:
        print("-----MAIN MENU-----")
        print("1 - Book a ticket\n2 - Cancel a ticket\n3 - Search for reservations, ticket and personal details\n4 - Edit Personal Information\n5 - Log out")
        ch = int(input("Your choice(1-5): "))
        if ch == 1:
            book(userid)
        elif ch == 2:
            cancel(userid)
        elif ch == 3:
            search(userid)
        elif ch == 4:
            edit(userid)
        elif ch == 5:
            print("Logout Successful")
            break
        else:
            print("Invalid input! Try Again")
def welcome():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("+++++Welcome to Railway Reservation+++++")
    print("++++++++++++++++++++++++++++++++++++++++")
    while True:
        print("\n1 - SignIn\n2 - SignUp\n3 - Exit")
        ch = int(input("Your choice(1-3): "))
        if ch == 1:
            after_signin(signin())
        elif ch == 2:
            signup()
        elif ch == 3:
            print("ThankYou. Please visit us again.")
            break
        else:
            print("Invalid Input! Try again")
try: 
    welcome()
    conn.close()
except Exception as e:
    print(e)
    conn.close()
