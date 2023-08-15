# Imports
from cProfile import label
from tkinter import *

# Main Screen
master = Tk()
master.title('Champion Lyfe Banking App')

data_file = open("Bank Data.txt", "r")
trans_file = open("Transaction Log.txt", "w")


# Functions


def finish_register():
    reg_name = temp_name.get()
    reg_surname = temp_surname.get()
    reg_mobile = temp_mobile.get()
    data_file = open("Bank Data.txt", "r")

    if reg_name == "" or reg_surname == "" or reg_mobile == "":
        notif.config(fg="red", text="All fields required *")
        return

    for reg_name in data_file:
        if reg_name == temp_name:
            notif.config(fg="red", text="Account already exits")
            return
        else:
            data_file = open("Bank Data.txt", "w")
            data_file.write(temp_name.get() + '\n')
            data_file.write(temp_surname.get() + '\n')
            data_file.write(temp_mobile.get() + '\n')
            notif.config(fg="green", text="Account has been created successfully")
            data_file.close()


def register():
    # Vars
    global temp_name
    global temp_surname
    global temp_mobile
    global notif
    temp_name = StringVar()
    temp_surname = StringVar()
    temp_mobile = StringVar()

    # Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')

    # Labels
    Label(register_screen, text="Please enter your details below to register", font=('Arial', 12)).grid(row=0, sticky=N,
                                                                                                        pady=10)
    Label(register_screen, text="Name", font=('Arial', 12)).grid(row=1, sticky=W)
    Label(register_screen, text="Surname", font=('Arial', 12)).grid(row=2, sticky=W)
    Label(register_screen, text="Mobile", font=('Arial', 12)).grid(row=3, sticky=W)
    notif = Label(register_screen, font=('Arial', 12))
    notif.grid(row=5, sticky=N)

    # Entries
    Entry(register_screen, textvariable=temp_name).grid(row=1, column=0)
    Entry(register_screen, textvariable=temp_surname).grid(row=2, column=0)
    Entry(register_screen, textvariable=temp_mobile).grid(row=3, column=0)
    data_file = open("Bank Data.txt", "w")
    data_file.write(temp_name.get() + '\n')
    data_file.write(temp_surname.get() + '\n')
    data_file.write(temp_mobile.get() + '\n')
    data_file.close()

    # Buttons
    Button(register_screen, text="Register", command=finish_register, font=('Arial', 12)).grid(row=6, sticky=N, pady=10)


def login_session():
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()
    data_file = open("Bank Data.txt", "r")

    for login_name in data_file:
        if login_name == temp_name:
            data_file = open("Bank Data.txt", "r")
            data_file = data_file.read()
            data_file = data_file.split('\n')
            login_name = data_file[1]
            login_password = data_file[3]
           # data_file.close()

    # Account Dashboard
    if login_password == login_password:
        login_screen.destroy()
        account_dashboard = Toplevel(master)
        account_dashboard.title('Dashboard')
        # Labels
        label(account_dashboard, text="Account Dashboard", font=('Arial', 12)).grid(row=0, sticky=N, pady=10)
        label(account_dashboard, text="Welcome" + login_name, font=('Arial', 12)).grid(row=1, sticky=N, pady=5)
        # Buttons
        Button(account_dashboard, text="Account Dashboard", font=('Arial', 12), width=30).grid(row=2, sticky=N,
                                                                                               padx=10)
        Button(account_dashboard, text="Personal Details", font=('Arial', 12), width=30).grid(row=3, sticky=N,
                                                                                              padx=10)
        return
    else:
        login_notif.config(fg="red", text="Password incorrect!!")
        login_notif.config(fg="red", text="No account found!!")


def deposit(amount):
    # data_file = open("Bank Data.txt", "r")
    # trans_file = open("Transaction Log.txt", "w")
    with open(data_file, 'r+') as f:
        balance = float(f.readline())
        f.seek(0)
        f.write(str(balance + amount) + '\n')
        f.truncate()

    with open(trans_file, 'a') as f:
        f.write('Deposit: +{:.2f}\n'.format(amount))


def withdraw(amount):
    with open(data_file, 'r+') as f:
        balance = float(f.readline())
        if balance < amount:
            print('Insufficient funds')
            return
        f.seek(0)
        f.write(str(balance - amount) + '\n')
        f.truncate()

    with open(data_file, 'a') as f:
        f.write('Withdrawal: -{:.2f}\n'.format(amount))


def personal_details():
    # Vars
    data_file = open("Bank Data.txt", 'r')
    user_details = data_file.data.split('\n')
    details_name = user_details(0)
    details_surname = user_details(1)
    details_mobile = user_details(2)
    # Personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    # Labels
    Label(personal_details_screen, text="Personal Details", font=("Arial", 12)).grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text="Name: " + details_name, font=("Arial", 12)).grid(row=1, sticky=W)
    Label(personal_details_screen, text="Surname: " + details_surname, font=("Arial", 12)).grid(row=2, sticky=W)
    Label(personal_details_screen, text="Mobile: " + details_mobile, font=("Arial", 12)).grid(row=3, sticky=W)


def login():
    # Vars
    global temp_login_name
    global temp_login_password
    global login_screen
    global login_notif
    temp_login_name = StringVar()
    temp_login_password = StringVar()

    # Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Login')
    # Labels
    Label(login_screen, text="Login to your account", font=('Arial', 12)).grid(row=0, sticky=N, pady=10)
    Label(login_screen, text="Name", font=('Arial', 12)).grid(row=1, sticky=W)
    Label(login_screen, text="Password", font=('Arial', 12)).grid(row=2, sticky=W)
    login_notif = Label(login_screen, font=('Arial', 12))
    login_notif.grid(row=4, sticky=N)

    data_file = open("Bank Data.txt", "r")
    data_file = data_file.read()
    data_file = data_file.split('\n')
    temp_login_name = data_file[1]
    temp_login_password = data_file[3]

    # entries
    Entry(login_screen, textvariable=temp_login_name).grid(row=1, column=1, padx=5)
    Entry(login_screen, textvariable=temp_login_password, show="*").grid(row=2, column=1, padx=5)
    # Buttons
    Button(login_screen, text="Login", command=login_session, width=15, font=('Arial', 12)).grid(row=3, sticky=W,
                                                                                                 padx=5)


# Labels
Label(master, text="Champion Lyfe Banking app", font=('Arial', 14)).grid(row=0, sticky=N, pady=10)
Label(master, text="The most secure bank", font=('Arial', 10)).grid(row=1, sticky=N, pady=10)

# Buttons
Button(master, text="Register", font=('Arial', 12), width=20, command=register).grid(row=3, sticky=N)
Button(master, text="Login", font=('Arial', 12), width=20, command=login).grid(row=4, sticky=N, pady=11)

master.mainloop()
