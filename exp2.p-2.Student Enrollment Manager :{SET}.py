ststudents_cet = {'Meena', 'Ram', 'Chetan', 'David', 'Monika'}
udents_jee = {'Ram', 'Chetan', 'Mamata', 'Omkar', 'Gauri'}
students_neet = {'Ram', 'David', 'Mamata', 'Gauri', 'Heena'}
union_students = students_cet | students_jee | students_neet
print("Students enrolled in at least one exam (Union):")
print(union_students)
intersection_students = students_cet & students_jee & students_neet
print("\nStudents enrolled in all three exams (Intersection):")
print(intersection_students)
difference_students_cet_jee = students_cet - students_jee
print("\nStudents enrolled in CET but not in JEE:")
print(difference_students_cet_jee)
difference_students_jee_neet = students_jee - students_neet
print("\nStudents enrolled in JEE but not in NEET:")
print(difference_students_jee_neet)
symmetric_difference_students = students_cet ^ students_jee ^ students_neet
print("\nStudents enrolled in exactly one of the exams (Symmetric Difference):")
print(symmetric_difference_students)
