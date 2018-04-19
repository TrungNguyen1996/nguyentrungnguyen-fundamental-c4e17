loop = True
wrong_count = 0

# x = x + 1 ~ x += 1

while loop:
    username = input("usename? ")
    password = input("password? ")

    if username != 'c4e':
        print("No such user")
        wrong_count += 1
    elif password != 'codethechange':
        print("wrong password")
        wrong_count += 1
    else:
        print("Welcome!!!")
        #break # chỉ tác động đến vòng lặp gần nhật
        loop = False

    if wrong_count > 3:
        loop = False
# break by python 3
# 1 while để nhập sai phải bắt nhập lại
# 2 Để nhập sai quá 3 lần là thoát
