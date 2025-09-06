import math

def ceil(x):
    return math.ceil(x)

def semesterGrade(midterm, final):
    # Weighted average (final counts twice)
    average = (midterm + 2 * final) / 3
    average = ceil(average)
    
    # Assign grade based on average
    if 90 <= average <= 100:
        grade = "A"
    elif 80 <= average <= 89:
        grade = "B"
    elif 70 <= average <= 79:
        grade = "C"
    elif 60 <= average <= 69:
        grade = "D"
    else:
        grade = "F"
    
    return average, grade

def main():
    midterm = float(input("Enter midterm grade: "))
    final = float(input("Enter final exam grade: "))
    avg, grade = semesterGrade(midterm, final)
    print(f"Semester average: {avg}")
    print(f"Semester grade: {grade}")

main()