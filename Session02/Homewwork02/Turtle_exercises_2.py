from turtle import *
# speed(0)
shape("turtle")
color("red")
for i in range(10):
    forward(5) # Tiến lên
    penup()     # Nhâc bút nét đứt
    forward(5)
    pendown()   # Hạ bút nét liền
    forward(5)

mainloop()

# có nghĩa là nhá. có phải đầu tiên ông forward(5) là đi thẳng đúng không. xong ông nhấc bút ông lên (gặp penup() ).
#  ông lại đi thêm 5 bước nữa là forward(5) nhưng lúc đấy đang penup() nên nó sẽ không ghi. xong ông lại hạ bút (pendown() )
#   xong lại forward(5) thì lúc đấy n lại ghi
