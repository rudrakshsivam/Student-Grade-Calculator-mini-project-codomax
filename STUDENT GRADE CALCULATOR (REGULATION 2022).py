#STUDENT GRADE CALCULATOR (REGULATION 2022)
grades = {"O":10,"A+":9,"A":8,"B+":7,"B":6,"C":5,"U":0,"W":0}
total = 0
n = int(input("How many Subjects: "))
for i in range(n):
    sub = input("Subject: ")
    grade = input("Grade:").upper()
    while grade not in grades:
        grade = input("Try again !").upper()
    point=grades[grade]
    total=total+point
    print("Subject:",sub,"grade:",grade)
gpa=total/n
print("GPA:",gpa)
