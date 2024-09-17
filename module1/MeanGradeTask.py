#Задача "Средний балл"
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
res = students.sort()
mean1 = sum(grades[0])/len(grades[0])
mean2 = sum(grades[1])/len(grades[1])
mean3 = sum(grades[2])/len(grades[2])
mean4 = sum(grades[3])/len(grades[3])
mean5 = sum(grades[4])/len(grades[4])
mean_grades_of_students = {students[0]: mean1, students[1]: mean2, students[2]:mean3, students[3]:mean4, students[4]:mean5}
print(mean_grades_of_students)

#Dict1 = dict(zip(students, mean_grades_of_students))