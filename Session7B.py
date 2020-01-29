students = ["John", "Jenny", "Jim", "Jack", "Joe"]
print(students, hex(id(students)))

newStudents = students + ["Fionna", "George"]
print(newStudents, hex(id(newStudents)))

students = students + ["Fionna", "George"]
print(students, hex(id(students)))
