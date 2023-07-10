student_scores = {
   "ramesh" : 91, "suresh" : 80, "mahesh": 7
}
student_grades = {}
print("\n\n",student_scores)
print("\n\n",student_grades)
for i in student_scores:
    j = student_scores[i]
    if j > 90:
        student_grades[i] = "Outstanding"
    elif j > 80:
        student_grades[i] = "Exceeds Expectations"
    elif j > 70:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "fail"

print("\n\n",student_grades,"\n")