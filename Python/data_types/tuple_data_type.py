emp_name = ("shubham", "mahesh", "prashant", "aditya", "pranil")
print(emp_name)

print(emp_name.count("aditya"))

print(emp_name.index("mahesh"))
print(len(emp_name))

print(max(emp_name))
print(min(emp_name))
print(sorted(emp_name))

# Please note that tuples are immutable in Python,
# so methods like append(), extend(), insert(), and remove() (which modify the tuple) are
# not applicable to tuples. If you need those operations, consider using a list instead.
