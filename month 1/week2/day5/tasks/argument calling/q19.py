def emp(**yo):
    for Name,Age in yo.items():
        yo[Name]=Age
        return yo

ame=input("enter your name ")
ge=int(input("enter age "))
print(emp(Name=ame,Age=ge))