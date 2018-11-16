<<<<<<< HEAD
from pymongo import MongoClient

#uri = "mongodb://192.168.1.74"
#client = MongoClient(uri)
client = MongoClient('localhost', 27017)
db = client.newDatabase
collection = db.collection

def main():
    print("Press 1 to login and 2 to register if you don't already have an account.")
    response = input()
    if response == "1":
        login()
    elif response == "2":
        register()
    main()

def register():
    username = input("Username: ")
    while db.collection.find_one({"username": username}) != None:
        username = input("Username taken, choose another.\nUsername: ")
    password1 = input("Password: ")
    password2 = input("Retype password: ")
    while password1 != password2:
        password1 = input("Passwords don't match, retype.\nPassword: ")
        password2 = input("Retype password: ")
    email = input("Email: ")
    while db.collection.find_one({"email": email}) != None:
        email = input("Email taken, use another.\nEmail: ")
    db.collection.insert_one({"username": username,
                           "password": password2,
                           "email": email,
                           "friends": [],
                           "requests": []})
    account(username)

def login():
    username = input("Username: ")
    password = input("Password: ")
    user = db.collection.find_one({"username": username, "password": password})
    if user == None:
        print("Username and password do not match any account.")
        login()
    account(username)

def account(username):
    print("\n%s's account\n" % username)
    print("To change password, press 1.",
          "To search users, press 2.",
          "To show friends, press 3.",
          "To show friend requests, press 4.",
          "To log out, press 5.")
    response = input()
    if response == "1":
        password1 = input("Password: ")
        password2 = input("Retype password: ")
        while password1 != password2:
            password1 = input("Passwords don't match, retype.\nPassword: ")
            password2 = input("Retype password: ")
        db.collection.update({"username": username}, {"$set": {"password": password2}})
        print("Password changed.")
        account(username)
    elif response == "2":
        searched_user = input("Type in username: ")
        user = db.collection.find_one({"username": searched_user})
        if user == None:
            print("User does not exist.")
            account(username)
        else:
            send_request = input("Send %s a friend request? (1 for yes, 2 for no)" % searched_user)
            if send_request == "1":
                db.collection.update({"username": user["username"]}, {"$push": {"requests": username}})
                print("Request sent.")
            account(username)
    elif response == "3":
        friends_list = db.collection.find_one({"username": username}, {"friends": 1})
        for friend in friends_list["friends"]:
            print(friend)
        account(username)
    elif response == "4":
        requests_list = db.collection.find_one({"username": username}, {"requests": 1})
        for request in requests_list["requests"]:
            print(request)
            accept_request = input("Accept request? (1 for yes, 2 for no)")
            db.collection.update({"username": username}, {"$pull": {"requests": request}})
            if accept_request == "1":
                db.collection.update({"username": username}, {"$push": {"friends": request}})
                db.collection.update({"username": request}, {"$push": {"friends": username}})
                print("%s accepted." % request)
        account(username)
    elif response == "5":
        main()

=======
from pymongo import MongoClient

#uri = "mongodb://192.168.1.74"
#client = MongoClient(uri)
client = MongoClient('localhost', 27017)
db = client.newDatabase
collection = db.collection

def main():
    print("Press 1 to login and 2 to register if you don't already have an account.")
    response = input()
    if response == "1":
        login()
    elif response == "2":
        register()
    main()

def register():
    username = input("Username: ")
    while db.collection.find_one({"username": username}) != None:
        username = input("Username taken, choose another.\nUsername: ")
    password1 = input("Password: ")
    password2 = input("Retype password: ")
    while password1 != password2:
        password1 = input("Passwords don't match, retype.\nPassword: ")
        password2 = input("Retype password: ")
    email = input("Email: ")
    while db.collection.find_one({"email": email}) != None:
        email = input("Email taken, use another.\nEmail: ")
    db.collection.insert_one({"username": username,
                           "password": password2,
                           "email": email,
                           "friends": [],
                           "requests": []})
    account(username)

def login():
    username = input("Username: ")
    password = input("Password: ")
    user = db.collection.find_one({"username": username, "password": password})
    if user == None:
        print("Username and password do not match any account.")
        login()
    account(username)

def account(username):
    print("\n%s's account\n" % username)
    print("To change password, press 1.",
          "To search users, press 2.",
          "To show friends, press 3.",
          "To show friend requests, press 4.",
          "To log out, press 5.")
    response = input()
    if response == "1":
        password1 = input("Password: ")
        password2 = input("Retype password: ")
        while password1 != password2:
            password1 = input("Passwords don't match, retype.\nPassword: ")
            password2 = input("Retype password: ")
        db.collection.update({"username": username}, {"$set": {"password": password2}})
        print("Password changed.")
        account(username)
    elif response == "2":
        searched_user = input("Type in username: ")
        user = db.collection.find_one({"username": searched_user})
        if user == None:
            print("User does not exist.")
            account(username)
        else:
            send_request = input("Send %s a friend request? (1 for yes, 2 for no)" % searched_user)
            if send_request == "1":
                db.collection.update({"username": user["username"]}, {"$push": {"requests": username}})
                print("Request sent.")
            account(username)
    elif response == "3":
        friends_list = db.collection.find_one({"username": username}, {"friends": 1})
        for friend in friends_list["friends"]:
            print(friend)
        account(username)
    elif response == "4":
        requests_list = db.collection.find_one({"username": username}, {"requests": 1})
        for request in requests_list["requests"]:
            print(request)
            accept_request = input("Accept request? (1 for yes, 2 for no)")
            db.collection.update({"username": username}, {"$pull": {"requests": request}})
            if accept_request == "1":
                db.collection.update({"username": username}, {"$push": {"friends": request}})
                db.collection.update({"username": request}, {"$push": {"friends": username}})
                print("%s accepted." % request)
        account(username)
    elif response == "5":
        main()

>>>>>>> ba7aa7af552c0ae9c19fd3ea74f3cad2c8a1c07a
main()