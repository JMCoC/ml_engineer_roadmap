import random

names = ['Juan', 'Valeria', 'Jack', 'Mono', 'Santiago', 'Ana', 'Carlos', 'Maria', 'Luis', 'Elena', 'Pedro', 'Sofia', 'Diego', 'Lucia', 'Miguel', 'Carmen', 'Jorge', 'Patricia', 'Raul', 'Isabel']
grades = [grade for grade in range(10,110,10)]

def people_list(num_people):
    students = []
    for i in range(num_people):
        student = {
            "i" : i + 1,
            "name" : random.choice(names),
            "grade" : random.choice(grades)
        }
        students.append(student)
    return students

studentsList = [student for student in people_list(100)]
print(studentsList)
studentsHighGrades = [student["name"] for student in studentsList if student["grade"] >= 80]
print(studentsHighGrades)
studentsNamesGrades = {student["name"] : student["grade"] for student in studentsList if student["grade"] >= 80}
print(studentsNamesGrades)

def averageGradeGenerator(students):
    total, count = 0, 0
    for student in students:
        total += student["grade"]
        count += 1
        yield total / count

studentsAvg = [student for student in studentsList if student["grade"] >= 80]
average_gen = averageGradeGenerator(studentsAvg)
for avg in average_gen:
    print(avg)

print(f"Final average grade: {avg}")