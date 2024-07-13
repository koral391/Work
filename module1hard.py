grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = tuple(students)
b = sorted(a)
average_score1 = sum(grades[0]) / len(grades[0])
average_score2 = sum(grades[1]) / len(grades[1])
average_score3 = sum(grades[2]) / len(grades[2])
average_score4 = sum(grades[3]) / len(grades[3])
average_score5 = sum(grades[4]) / len(grades[4])
grades [0] = average_score1
grades [1] = average_score2
grades [2] = average_score3
grades [3] = average_score4
grades [4] = average_score5

dictionary = dict([(b[0], grades[0]), (b[1], grades[1]),(b[2], grades[2]),(b[3], grades[3]),(b[4], grades[4])])
print(dictionary)