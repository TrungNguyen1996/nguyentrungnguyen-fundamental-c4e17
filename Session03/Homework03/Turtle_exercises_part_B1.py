from turtle import *
speed(0)
# Given the following list: colors = ['red', 'blue', 'brown', 'yellow', 'grey']

# Tam giác đỏ
color("red")
for i in range(3):
    forward(50)
    left(120)

# Vuông lam
color("blue")
for i in range(4):
    forward(50)
    left(90)

# Ngũ giác nâu
color("brown")
for i in range(5):
    forward(50)
    left(72)

# Lục giác vàng
color("yellow")
for i in range(6):
    forward(50)
    left(60)

# Thập giác xám
color("grey")
for i in range(7):
    forward(50)
    left(51.4285714286)

mainloop()
# C4E17 buổi 3 btvn 16 4 18
