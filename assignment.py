print("**Grading system**");
print("A = 71-100\nB = 61-70\nC = 51-60\nD = 41-50\nE = 31-40\nF = 0-30");
grade = int(input("Enter the student's grade:"));
if grade < 0 or grade > 100:
    print("invalid grade")
elif grade<=30:
    print("the student's grade is an F, he/she will retake the exam\n");
elif grade>30 and grade<=40:
    print("the student's grade is an E, he/she is strongly adviced to retake the exam\n");
elif grade>40 and grade<=50:
    print("the student's grade is a D, he/she should can retake the exam if not pleased with he/she's result\n");
elif grade>50 and grade<= 60:
    print("the student's grade is a C, he/she is not elgible to retake the exam\n");
elif grade>60 and grade<=70:
    print("the student's grade is a B, he/she performed really well hence is not eligible to retake the exam\n");
else:
    print("the student's grade is an A, he/she performed exceptionally\n");

    
