# Welcome to our shop, what do you want (C, R, U, D)? R
Our_items = ["T-Shirt", "Sweater"]

choose = int(print("welcom to the shop, what you want (C, R, U, D)"))
# 1111111111111111111111111 Read
if choose == r:
    Our_items = ["T-Shirt", "Sweater]"
    print(Our_items)
# 2222222222222222222222222 Creat
if choose == c:

    Our_item = ["T-Shirt", "Sweater"]
    print(Our_items)

    new_item = int(input("Enter new item: "))
    Our_item.append(new_items)
    print(Our_items)

# 3333333333333333333333333 Update
if choose == u:
    i = int(input("Nhập vị trí muốn update"))
    u = int(input("Nhập dữ liệu muốn update"))

Our_items[1] = u
print(u)


# 44444444444444444444444444 Delete
if choose == d:
print("welcom to the shop, what you want (C, R, U, D)")
