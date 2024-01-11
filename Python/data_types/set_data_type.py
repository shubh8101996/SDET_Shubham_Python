emp_name = {"shubham", "mahesh", "prashant", "aditya", "pranil"}
# emp_id = [1, 454, 2234]


emp_name.add("eshwar")
print(emp_name)

# emp_name.update(emp_id)
# print(emp_name)

# print(emp_name.pop())   //start element is delete

print(emp_name.discard("shubham"))  # specific element is delete if not does not raise error
print(emp_name)

print(emp_name.discard("aditya"))  # specific element is delete if not raise error
print(emp_name)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
