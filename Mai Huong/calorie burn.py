H = int(input("Nhập chiều cao (cm): "))
W = float(input("Nhập cân nặng (kg): "))
A = int(input("Nhập tuổi: "))
G = str(input("Nhập giới tính: "))

BMI = W/(H/100)**2
print("BMI = ", BMI)
if G == "Male":
    BMR = 66.47 + (13.75*W) + (5.0 * H) - (6.75 * A)
    print("BMR = ", BMR)
elif G == "Female":
    BMR = 665.09 + (9.56 * W) + (1.84 * H) - (4.67 * A)
    print("BMR = ", BMR)

