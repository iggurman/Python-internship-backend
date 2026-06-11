# ifs and nested ifs
# #Insurance eligibility: Age 18-60,M, Non-smoker, BMI between 18-30
#Insurance eligibility: Age 16-50,F, Non-smoker, BMI between 18-30

print("insurance eligibility ")
gender=str(input("Male or Female [M or F] "))
if gender=="m" or gender=="M":
    age=int(input("please enter your age:"))
    if age>=18 and age<=60:          
        smoke=str(input("Do You Smoke? [Y or N] "))
        if smoke=="N" or "n":
            bmi=int(input("Please enter your bmi: "))
            if bmi>=18 and bmi<=30:
                print("You are eligible for Insurance ")
            else:
                print("Bmi is not in the range of 18-30 so not eligible ")
        elif smoke=="y" or gender== "Y":
            print("Not eligible because of smoking ")
        else:
            print("invalid option ")
    else:
        print("age criteria not met ")
        
elif gender=="F" or gender=="f":
    age=int(input("please enter your age: "))
    if age>=16 and age<=50:          
        smoke=str(input("Do You Smoke? [Y or N]" ))
        if smoke=="N" or "n":
            bmi=int(input("Please enter your bmi:" ))
            if bmi>=18 and bmi<=30:
                print("You are eligible for Insurance" )
            else:
                print("Bmi is not in the range of 18-30 so not eligible" )
        elif smoke=="y" or gender== "Y":
            print("Not eligible because of smoking" )
        else:
            print("invalid option" )
    else:
        print("age criteria not met" )            
            # gender=str(input("please enter your gender:"))
else:
    print("invalid option please try again" )
    