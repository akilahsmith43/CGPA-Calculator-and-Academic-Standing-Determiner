name = input("Enter your name \n")
major = input("Input your major \n")

grade1 = input("Enter the grade for subject1 (A, B, C, D, F): \n")
if grade1 == "A":
    c1_qpts = 4.0
elif grade1 == "B":
    c1_qpts = 3.0
elif grade1 == "C":
    c1_qpts = 2.0
elif grade1 == "D":
    c1_qpts = 1.0
elif grade1 == "F":
    c1_qpts = 0.0
else:
    print("error")
    exit()

grade2 = input("Enter the grade for subject2 (A, B, C, D, F): \n")
if grade2 == "A":
    c2_qpts = 4.0
elif grade2 == "B":
    c2_qpts = 3.0
elif grade2 == "C":
    c2_qpts = 2.0
elif grade2 == "D":
    c2_qpts = 1.0
elif grade2 == "F":
    c2_qpts = 0.0
else:
    print("error")
    exit()

grade3 = input("Enter the grade for subject3 (A, B, C, D, F): \n")
if grade3 == "A":
    c3_qpts = 4.0
elif grade3 == "B":
    c3_qpts = 3.0
elif grade3 == "C":
    c3_qpts = 2.0
elif grade3 == "D":
    c3_qpts = 1.0
elif grade3 == "F":
    c3_qpts = 0.0
else:
    print("error")
    exit()

CGPA = (c1_qpts *3 + c2_qpts * 3 + c3_qpts * 4) / 10

print(name.upper())
print(major.title())
print("CGPA: ",CGPA)

if CGPA >= 2.00:
    print("Academic Standing: Good")
elif CGPA >= 1.99:
    print("Academic Standing: Warning")
elif CGPA >= 1.74:
    print("Academic Standing: Probation")
else:
    print("Academic Standing: Suspension")


input ("Hit Enter to end program")





