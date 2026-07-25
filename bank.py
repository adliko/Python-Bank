import json


def registration():
    username = input("Username: ")
    password = input("Password: ")
    with open("users.json", "r") as file:
        users = json.load(file)
        for user in users:
            if username == user["username"]:
                print("username already taken")
                return
        newuser = {"username": username, "password": password, "balance": 1000, "history": []}
        users.append(newuser)
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)
        print("user created successfully")

def login():
    username = input("Enter username: ")
    password = input("enter your password: ")
    with open("users.json", "r") as file:
        users = json.load(file)
        for user in users:
            if username == user["username"]:
                if password == user["password"]:
                    print("login successful")
                    bankmenu(user)
                    return user
                else:
                    print("login failed")
                    return None

        print("username not exist")
def check_balance(cuser):
    print("your balance:",cuser["balance"])
def deposit(cuser):
    with open("users.json", "r") as file:
        users = json.load(file)
    for user in users:
        if user["username"] == cuser["username"]:
            amount = int(input("enter your deposit amount: "))
            user["balance"] += amount
            user["history"].append(f"Deposit +{amount}")
            print("your balance now:", user["balance"])
            break
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)
def withdraw(cuser):
    with open("users.json", "r") as file:
        users = json.load(file)
    for user in users:
        if user["username"] == cuser["username"]:
            amount = int(input("enter your withdraw amount: "))
            if user["balance"] < amount:
                print("withdraw failed")
                return
            user["balance"] -= amount
            cuser["balance"] = user["balance"]
            cuser["history"] = user["history"]
            user["history"].append(f"Withdraw -{amount}")
    print("your balance now:", user["balance"])
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

def transfer(cuser):
    receiver_name = input("to whem you send money: ")
    amount = int(input("how much money you want to transfer: "))
    sender = None
    receiver = None
    with open("users.json", "r") as file:
        users = json.load(file)
    for user in users:
        if user["username"] == cuser["username"]:
            sender = user
        if user["username"] == receiver_name:
            receiver = user

    if receiver is None:
        print("receiver does not exist")
        return
    if sender["balance"] < amount:
        print("not enough money")
        return
    sender["balance"] -= amount
    receiver["balance"] += amount
    sender["history"].append(f"Transfer to {receiver['username']} -{amount}")
    receiver["history"].append(f"Received from {sender['username']} +{amount}")
    with open ("users.json", "w") as file:
        json.dump(users, file, indent=4)
    print("transfer successful")
    print("your balance now:", sender["balance"])
def history(cuser):
    with open("users.json", "r") as file:
        users = json.load(file)
    for user in users:
        if user["username"] == cuser["username"]:
            for opperation in user["history"]:
                print(opperation)

def bankmenu(cuser):
    print("Welcome to the bank menu")
    print("\n===== ABDULLA BANK =====","\n1. Check balance","\n2. Deposit money","\n3. Withdraw money","\n4. Transfer money","\n5. Transaction history"
"\n6. Logout")
    while True:
        try:
            choice = int(input("Enter your choice: "))
        except:
            print("invalid choice")
        if choice == 1:
            check_balance(cuser)
        elif choice == 2:
            deposit(cuser)
        elif choice == 3:
            withdraw(cuser)
        elif choice == 4:
            transfer(cuser)
        elif choice == 5:
            history(cuser)
        elif choice == 6:
            print("you logged out")
            break
        else:
            print("invalid choice")


while True:
    try:
        hoice = input("enter your choice: ")
    except:
        print("invalid choice")
    if hoice == "1":
        registration()
    elif hoice == "2":
        cuser = login()
    elif hoice == "3":
        break
    else:
        print("invalid choice")

