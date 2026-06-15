print(f"==========================================")
print("Student Management System")

students = []

#menu
while True:
    print(f"==========================================")
    print("1. Add Student")
    print("2. view Result ")
    print("3. View Structure")
    print("4. Exit")
    print(f"==========================================")

    
    choice=input("Enter Choice ")
    if choice=="1":
#_______________________________________________________________
#this was just option 1 "add student"
        stu_name=input("Enter name of the student ")

        #subjects input
        while True:
            eng = int(input("Enter marks for English: "))
            if eng<0 or eng>100:
                print(f"{eng} is invalid marks entered ")
                continue
            break


        while True:
            hindi = int(input("Enter marks for Hindi: "))
            if hindi<0 or hindi>100:
                print(f"{hindi} is invalid marks entered ")
                continue
            break

        while True:
            maths = int(input("Enter marks for Maths: "))
            if maths<0 or maths>100:
                print(f"{maths} is invalid marks entered ")
                continue 
            break

        while True:
            science = int(input("Enter marks for Science: "))
            if science<0 or science>100:
                print(f"{science} is invalid marks entered ")
                continue 
            break

        while True:
            sanskrit = int(input("Enter marks for Sanskrit: "))
            if sanskrit<0 or sanskrit>100:
                print(f"{sanskrit} is invalid marks entered ")
                continue 
            break


        marks=[eng,hindi,maths,science,sanskrit]
        print(f"-----------------------------------------")
        failed=0
        for mark in marks:
            if mark < 35:
                failed += 1
        print(f"Failed Subjects= {failed}")
        
        #total marks 
        total=sum(marks)
        print(f"Total marks of the student is {total}")

        #avg marks 
        avg=total/len(marks)
        print(f"The average of 5 subjects is {avg}")

        #percentage
        percent=(total/500)*100
        print(f"Percentage obtained by the student is {percent}")
        
        while True:
            attendance=float(input("Enter Attendance % "))
            if attendance<0 or attendance>100:
                print(f"{attendance} is not a valid attendance! Please Enter valid attendance")
                continue
            break
        
        #attendance criteria
        if attendance>=75:
            eligibility="Eligible"
        else:
            eligibility="Not Eligible"    
        print(f"Eligibility: {eligibility}")
        
        #PASS or Fail
        if attendance>=75 and failed==0:
            result_status="PASS"
        else:
            result_status="FAIL"
        print(f"Result status = {result_status}")
        
        #performance criteria
        if percent >= 90:
            performance = "Excellent"
        elif percent >= 80:
            performance = "Very Good"
        elif percent >= 70:
            performance = "Good"
        elif percent >= 60:
            performance = "Average"
        elif percent>=35:
            performance = "Needs Improvement"
        else:
            performance="Failed!"
            
        #Highest and lowest marks 
        highest=max(marks)
        lowest=min(marks)
        print(f"Highest Marks are {highest}")
        print(f"Lowest Marks are {lowest}")
        

        #grade
        if percent>=90:
            grade="A+"
        elif percent>=80:
            grade="A"
        elif percent>=70:
            grade="B"
        elif percent>=60:
            grade="C"
        elif percent>=35:
            grade="I"
        else:
            grade="FAIL"
        print(f"Student received grade: {grade}")


        #dictionary for students management
        student={
        "Name":stu_name,
        "Marks":marks,
        "Percentage":percent,
        "Average":avg,
        "Total Marks": total,
        "Grade obtained":grade,
        "Attendance": attendance,
        "Eligibility": eligibility,
        "Failed Subjects": failed,
        "Highest Marks": highest,
        "Lowest Marks": lowest,
        "Result Status": result_status,
        "Performance": performance,
        }
        students.append(student)
        print("========================================================")

#________________________________________________________
    #option 2
    elif choice=="2":
        if len(students)==0:
            print("No students exist")
        else:
            for student in students:
                print("=======================")
                print("RESULT CARD")
                print("=======================")
                
                #ALL THE VALUES 
                print(f"Name of English: {student['Name']}")
                print(f"Marks of English: {eng}")
                print(f"Marks of Hindi: {hindi}")
                print(f"Marks of Maths: {maths}")
                print(f"Marks of Science: {science}")
                print(f"Marks of Sanskrit: {sanskrit}")
                print(f"Percentage: {student['Percentage']}")
                print(f"Average: {student['Average']}")
                print(f"Total Marks: {student['Total Marks']}")
                print(f"Grade obtained: {student['Grade obtained']}")
                print(f"Attendance: {student['Attendance']}")
                print(f"Eligibility: {student['Eligibility']}")
                print(f"Failed Subjects: {student['Failed Subjects']}")
                print(f"Highest Marks: {student['Highest Marks']}")
                print(f"Lowest Marks: {student['Lowest Marks']}")
                print(f"Result Status: {student['Result Status']}")
                print(f"Performance: {student['Performance']}")
                print("========================================================")
                
    elif choice=="3":
        #total number of students 
        total_students=len(students)
        
        #passed students and failed students
        passed_students=0
        failed_students=0
        
        for student in students:
            if student["Result Status"]=="PASS":
                passed_students+=1
            else:
                failed_students+=1
                
        #class average
        total_percent=0
        
        for student in students:
            total_percent+=student["Percentage"]
            
        if total_students>0:
            class_avg=total_percent/total_students
        else:
            class_avg=0
            
            
        #topper student
        topper_name=""
        topper_percent= 0
        
        for student in students:
            if student["Percentage"]>topper_percent:
                topper_percent=student["Percentage"]
                topper_name=student["Name"]

        print("============================")
        print("VIEW STATISTICS")
        print("============================")
        print(f"Total Students = {total_students}")
        print(f"Passed Students = {passed_students}")
        print(f"Failed Students = {failed_students}")
        print(f"Class Average = {class_avg}")
        print(f"Topper is {topper_name} with {topper_percent} percentage")
        
    #OPTION 4 EXIT
    elif choice=="4":
        print("========================================================")
        print("Thankyou for using Student Management System ")
        print("========================================================")

        break
    else:
        print("Enter correct choice ")
        continue
        
