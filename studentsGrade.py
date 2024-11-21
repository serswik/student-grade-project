import csv

pass_mark = 70

def calculate_average_score(scores):
    return sum(scores) / len(scores)

def check_success(student, pass_mark):
    average_score = calculate_average_score(student["scores"])
    student["average_score"] = average_score
    if average_score >= pass_mark:
        student["status"] = "Успішний"
    else:
        student["status"] = "Неуспішний"
    return student

def print_student_results(students):
    for student in students:
        print(f"Студент (кв. номер: {student['ticket_number']}): {student['name']} {student['surname']}, Середній бал: {student['average_score']:.2f}, Статус: {student['status']}")

# Шлях до файлу з даними
file_path = r'C:\Users\serge\OneDrive\Рабочий стол\Studying\Уник3курс1семестр\Сарибога\students.csv'

students = []
with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        scores = [int(row[f'score{i}']) for i in range(1, 5)]
        students.append({
            "ticket_number": row['ticket_number'],
            "name": row['name'],
            "surname": row['surname'],
            "scores": scores
        })

students_with_status = [check_success(student, pass_mark) for student in students]

print("Результати студентів:")
print_student_results(students_with_status)

