import re as regex
import getpass

file = open("username_password_hidden.txt", "r")
text = "".join(file.readlines())
file.close()

usernames = regex.findall("(?<=Username=).*?u.*?r", text)
passwords = regex.findall("(?<=Password=).*?\d{4}", text)

for i in range(len(usernames)):
    usernames[i] = regex.search("u.*?r", usernames[i])[0]
for i in range(len(passwords)):
    passwords[i] = regex.search("\d{4}", passwords[i])[0]

inputtedUsername = input("Username: ")
inputtedPassword = getpass.getpass("Password: ")
if inputtedUsername in usernames and inputtedPassword in passwords:
    print("You have logged in sucessfully!")
else:
    print("Incorrect username or password")
