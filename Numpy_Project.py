import numpy as np

#-----------------------------
# Student Marks Analyzer
#----------------------------

#Student Names

students=np.array(["Swapnil","Tanvi","Priya","Daksh"])

#Marks : rows = students,columns = subjects

marks = np.array([
    [88,45,78], #Student Swapnil
    [98,99,96], #Student Tanvi
    [67,47,87], #Student Priya
    [55,76,22] #Student Daksh
])

subjects = np.array(["Maths","Python","Machine Learning"])

print("📊 STUDENT MARKS ANALYZER\n")
#-------------------------
# Display marks
#------------------------

print("Marks Table : ")
print(marks)

#-----------------------
# Subject - wise average
#axis=0 ---> column wise
#----------------------

subject_avg = np.mean(marks,axis=0)
print("\n 📘 Subject-wise Average:")
for i in range(len(subjects)):
    print(f"{subjects[i]} : {subject_avg[i]:.2f}")

#-------------------------
#student - wise average
#axis=1 ---> row wise
#-------------------------

student_avg = np.mean(marks,axis=1)
print("\n 👩‍🎓 Student-wise Average")
for i in range(len(students)):
    print(f"Student {students[i]} : {student_avg[i] :.2f}")

# student_avg[i]:.2f here colon separates the variable from the formatting rule this is python f-string formatting

#-----------------------
#Highest & Lowest marks
#-----------------------


print("\n 🏆 Highest marks:",np.max(marks))
print("\n 🏆 Lowest marks:",np.min(marks))

# np.marks=It finds the single biggest number from the ENTIRE marks array.


#-------------------------
#Class Topper
#-----------------------

#argmax() returns the INDEX (position) of the largest value — NOT the value itself.

topper_index = np.argmax(student_avg)
print("\n 🥇 Class Topper:", students[topper_index])
print(f"Topper Average : {student_avg[topper_index]:.2f}")

#----------------------
# Overall Class Average
#---------------------


#--------------------------------------------------------
# class_avg = np.mean(marks)
# Add all numbers
# 85 + 90 + 88
# 78 + 82 + 80
# 92 + 95 + 94
# 70 + 75 + 72
# = 1001
# Total elements = 12(4 students × 3 subjects = 12 numbers)
# 1001÷12=83.4166...
#-----------------------------------------------------



class_avg = np.mean(marks)
print("\n📈 Overall Class Average :",round(class_avg,2))


