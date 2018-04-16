from getpass import getpass

while True: # Ấn ctrl c để thoát
    print("Welcome to superuse gateway!")
    username = input("Enter the username: ")
    password = getpass("Enter password: ") # getpass.getpass

    if username != "c4e":
        print("No such user")
    else:
        #Valid username
        if password != "codethechange":
            print("Wrong password")
        else:
            print("welcome, c4e")
            break

# Hỏi thêm về vòng while 13 4 18
# while to là vong lặp vô tận
