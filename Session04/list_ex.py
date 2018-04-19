menu = ['pho', 'com rang', 'my xao', 'bun rieu']
print(menu)
# Creat
# menu.append('hu tieu')
# print("After append")
# print(menu)

# # for i chạy chỉ số
# for i in range(len(menu)):
#     print(menu[i])
# # foreach chạy giá trị
# for item in menu:

# for enum chạy cả chỉ số cả giá trị

name = "Nguyen"
age = 22
status = "Doc than"
address = "Doi can"

# str + int ????????? 17 4 18  8 12 ch
message = '''{0}
{1} tuoi
tinh trang quan he: {2}
song o {3}''' .format(name, age, status, address )


# print(name + "," + str(age) + status + address) ???????????????????? Thiếu

# for i, item in enumerate(menu):
#     message = "{0}, {1}".format(i + 1, item)
#     print(i + 1, item)
