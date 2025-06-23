class_journal = {
    "Layla": [89,91,86],
    "Tariq": [77,84,73],
    "Jana" : [100,97,94],
    "Ziad" : [62,71,75],
}

new_grades = []

def average_grades(grades):
    return sum(grades) / len(grades)

while x != 0:
    x = input("Enter anything except 0 to add a new student, or 0 to exit: ")
    student = input("Enter the student's name: ")
    grade = float(input("Enter the student's grades: "))
    new_grades.append((student, grade))

for student, grades in class_journal.items():
    rounded_average = round(average_grades(grades), 2)
    print(f"{student}'s grades are: {grades}" f" with an average of: {rounded_average}")

max_average = max(average_grades(grades) for grades in class_journal.values())
top_students = [student for student, grades in class_journal.items() if average_grades(grades) == max_average]
print(f"The highest average grade in the class is: {top_students}: {round(max_average, 2)}")

for student, grades in class_journal.items():
    most_consistent_student = min(class_journal, key=lambda student: max(class_journal[student]) - min(class_journal[student]))
print(f"The most consistent student is: {most_consistent_student} with grades: {class_journal[most_consistent_student]}")

for student, grades in class_journal.items():
    if grades < 70:
        print(f"{student} has a grade below 70")

for student, grades in class_journal.items():
    G = 0
    G += len(grades)
print(f"{G} grades recorded.")

for student, grades in class_journal.items():
    sum=0
    sum += sum(grades)
    av = sum / G
print(f"The average grade for the class is: {round(av, 2)}")

