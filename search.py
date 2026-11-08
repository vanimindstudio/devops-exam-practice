def search_students(students, query):
    return [
        student for student in students
        if query.lower() in student.lower()
    ]


students = ["Alex", "Andrew", "John", "Michael"]

print(search_students(students, "an"))
