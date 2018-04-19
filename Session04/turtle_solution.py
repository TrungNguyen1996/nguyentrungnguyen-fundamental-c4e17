from turtle import *

color_list = ["red", "blue", "brown", "yellow", "grey"]
color_n = len(color_list)
for n in range(3, 12):
    selected_color = color_list[(n - 3) % color_n] #color_list # ?????????????????
    color(selected_color) # not const
    for i in range(n):
        forward(100)
        left(360 / n) # 360 / 5

mainloop()

# khi nafp vô thức thấy code giống 3 lần thì chắc chắn sẽ lặp dc

#qvtvt@gmail.com
