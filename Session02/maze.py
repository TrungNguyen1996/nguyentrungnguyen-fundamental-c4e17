from turtle import *
shape("turtle")
for i in range(0, 400, 10): # 4 lần
    forward(i)    # độ dài
    left(90)        # quay
    forward(10+i)
mainloop()
