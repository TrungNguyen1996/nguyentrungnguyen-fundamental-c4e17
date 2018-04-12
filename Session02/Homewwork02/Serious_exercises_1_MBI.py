c = int(input("Mời nhập chiều cao")) / 100 # đổi cm ra mét
n = int(input("Mời nhập cân nặng"))

BMI =  n / (c*c) # BMI = cân năng * (chiều cao * chiều cao)
print("BMI", BMI)

if BMI < 16:
    print("Thiếu cân nặng")
elif BMI = 16 < 18,5:
    print("Thiếu cân")
elif BMI = 18,5 < 25:
    print("Bình thường")
elif BMI = 25 <30:
    print("Thật cân đối")
else >30:
    print("Béo phì")
