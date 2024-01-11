student_list = ["shubham", "mahesh", "prashant", "aditya", "pranil"]
print(student_list)

student_list.pop(1)
print("Pop operation " + str(student_list))

student_list.sort()
print("Sort operation " + str(student_list))

student_list.reverse()
print("reverse operation " + str(student_list))

student_list.append("nilesh")
print("add element at end  " + str(student_list))

student_list.insert(3, "swara")
print("add element at specific  " + str(student_list))

index = student_list.index("shubham")
print("get index of element  " + str(index))

student_list.sort(reverse=True)
print(student_list)

student_list.clear()
print(student_list)
