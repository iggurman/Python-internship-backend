# Check scholarship eligibility:
# Marks ≥ 80 AND Attendance ≥ 75

mark=int(input("Enter your Marks "))
attendance=int(input("Enter your Attendance "))

if mark >= 80 and attendance >= 75:
    print("Eligible for a Scholarship")

elif mark >= 80 and attendance < 75:
    print("Due to less attendance, not eligible for a scholarship")

elif mark < 80 and attendance >= 75:
    print("Due to less marks, not eligible for a scholarship")

else:
    print("Due to less marks and attendance, not eligible for a scholarship")

