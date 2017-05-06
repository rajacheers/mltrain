
#program-1
students_list = ['arthi','archana','ragu','mano']
print("students list : ",students_list)

print("count of Arthi: ",students_list.count('arthi'))
print("count of Archana: ",students_list.count('archana'))

students_list.append('Anu')
print("students list : ",students_list)

students_list1 = ['amal','arjun']
students_list.extend(students_list1)
print("students list : ",students_list)
