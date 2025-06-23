class_journal = {
    "Layla": [89,91,86],
    "Tariq": [77,84,73],
    "Jana" : [100,97,94],
    "Ziad" : [62,71,75],
}
new_grades = []
G=0
s=0

def average_grades(grades):
    return sum(grades) / len(grades)

x = int(input("Enter any nb except 0 to add a new student, or 0 to exit: "))
while x != 0:
    print("to exit press enter without entering a name")
    student = input("Enter the student's name: ")
    if student == "":
        break
    grade = float(input("Enter the student's grades: "))
    new_grades.append((student, grade))

if new_grades != []:
    for student, grade in new_grades:
        if student in class_journal:
            class_journal[student].append(grade)
        else:
            class_journal[student] = [grade]

with open("class_journal.txt", "w") as file:

    for student, grades in class_journal.items():
        rounded_average = round(average_grades(grades), 2)
        file.write(f"{student}'s grades are: {grades}" f" with an average of: {rounded_average}\n")

    max_average = max(average_grades(grades) for grades in class_journal.values())
    top_students = [student for student, grades in class_journal.items() if average_grades(grades) == max_average]
    file.write(f"The highest average grade in the class is: {top_students}: {round(max_average, 2)}\n")

    for student, grades in class_journal.items():
        most_consistent_student = min(class_journal, key=lambda student: max(class_journal[student]) - min(class_journal[student]))
    file.write(f"The most consistent student is: {most_consistent_student} with grades: {class_journal[most_consistent_student]}\n")

    for student, grades in class_journal.items():
        if any(grade < 70 for grade in grades):
            file.write(f"{student} has a grade below 70\n")

    for student, grades in class_journal.items():
        G += len(grades)
    file.write(f"{G} grades recorded.\n")

    for student, grades in class_journal.items():
        s += sum(grades)
        av = s / G
    file.write(f"The average grade for the class is: {round(av, 2)}")