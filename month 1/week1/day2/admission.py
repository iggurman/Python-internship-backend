# Check admission eligibility:
# Marks ≥ 60 OR Sports Certificate = Yes

marks=int(input("Enter Your Marks "))
certificate=input("Do you have a certificate (Yes/No) ")

if marks>=60 or certificate==("yes"or"Yes"):
    print("Admission Granted")
else:
    print("Sorry not eligible for the admission")
    
