class_journal = {
    "Layla": [89,91,86],
    "Tariq": [77,84,73],
    "Jana" : [100,97,94],
    "Ziad" : [62,71,75],
}

def average_grades(grades):
    return sum(grades) / len(grades)

for student, grades in class_journal.items():
    rounded_average = round(average_grades(grades), 2)
    print(f"{student}'s grades are: {grades}" f" with an average of: {rounded_average}")

max_average = max(average_grades(grades) for grades in class_journal.values())
top_students = [student for student, grades in class_journal.items() if average_grades(grades) == max_average]
print(f"The highest average grade in the class is: {top_students}: {round(max_average, 2)}")

