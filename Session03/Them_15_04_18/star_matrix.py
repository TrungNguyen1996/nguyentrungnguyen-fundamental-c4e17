# m = int(input("Enter the m number?")) #Ask use enter the number
# n = int(input("Enter the n number")

# o x x x x
# x o x x x
# x x o x x
# x x x o x
# in
# for i in range(3):
#     for j in range(4):
#         if i==j:
#             print("o ", end='')
#         else:
#             print("x ", end='') # 1 cell = 1 o
#     # print("* ")
#     print() # in để xuống dòng, enter a new line
# # print("Hi") # in thử để đã xuống dòng

# chia dieu kien
# o x x x x
# x o x x x
# x x o x x
# x x x o x

# in so le o chéo trong đám x
for i in range(3):
    for j in range(4):
        if (i + j) % 2 == 0: # kiểm tra số dư chẵn thì in *
            print("x ", end='')
        else: # kiểm tra số dư chẵn thì in o
            print("o ", end='')
    print()


# In tam giác đổ chéo từ bên phải
