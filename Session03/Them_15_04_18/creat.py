favs = ["Death note", "Inception", "Kungfu movie"]
print("Hi")
print(*favs)

new_fav = input("Name one thing you want to add: ")
favs.append(new_fav)
print(*favs, sep=", ")
