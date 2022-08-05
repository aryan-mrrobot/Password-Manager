import pickle
import pyperclip


user_id = input("enter your user ID (press 1 to create account) : ")

dictionary = {}

with open("Myproj\\pass_man.txt", "br") as filewrite :
    dictionary = pickle.load(filewrite)

if "1" in user_id:
    email = input("enter your user ID : ")

    with open("Myproj\\email.txt", "w") as f:
        f.write(email)

    password = input("enter your password : ")

    with open("Myproj\\pass.txt1", "w") as a:
        a.write(password)

with open("Myproj\\email.txt", "r") as fr:
    Store_email = fr.read()

if user_id == Store_email:
    password2 = input("Enter your password : ")
    with open("Myproj\\pass.txt1", "r") as ar:
        Store_pass = ar.read()

    if password2 == Store_pass:
        conf = input("To know the password press '1' to save password press '2' :")
        if "2" in conf:
            account = input("enter your account name : ")
            acc_pass = input("enter your password : ")

            confirmation = input("whould you like to save it (y/n) : ")

            if "y" in confirmation:
                dictionary[account] = acc_pass

                with open("C:\\Users\\aryan\Desktop\\password\\Myproj\\pass_man.txt", "bw") as readfile:
                    dictionary = pickle.dump(dictionary, readfile, protocol=2)
                print(f"Done! your {account}'s password has been saved")

            else:
                print("your data has not been saved....")

        if "1" in conf:
            email = input("which account's password you want to know :")

            with open("Myproj\\pass_man.txt", "br") as file :
                dictionary = pickle.load(file)
            
            if email in dictionary:
                print(f"your {email}'s password is {dictionary[email]}")
                pyperclip.copy(dictionary[email])
            else:
                print("this password is not saved")
