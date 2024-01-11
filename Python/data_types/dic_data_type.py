my_dict = {'a': 1, 'b': 2}
student_list = ["shubham", "mahesh", "prashant", "aditya", "pranil"]

my_dict.setdefault('c', 1)
print(my_dict)

print(my_dict.items())

new_dict = dict.fromkeys(student_list, 0)
print(new_dict)
