# list of tuples of student names
student_names = [
    ("Amit", "Sharma"),
    ("Vikas", "Rana"),
    ("Amit", "Verma"),
    ("Rahul", "Gupta"),
    ("Rahul", "Mehta"),
    ("Pooja", "Nair"),
    ("Rahul", "Singh"),
    ("Priya", "Patel"),
    ("Priya", "Shah"),
    ("Neha", "Agarwal"),
    ("Neha", "Jain"),
    ("Ankit", "Yadav"),
    ("Kiran", "Reddy"),
    ("Ankit", "Mishra"),
    ("Rohit", "Kumar"),
    ("Rohit", "Malhotra"),
    ("Sneha", "Kulkarni"),
    ("Sneha", "Deshpande"),
    ("Suresh", "Iyer"),
    ("Manish", "Pandey")
]

""" create dictionary with key as
first name and values as
list of surnames
----------------------------------
name_dict = {
    first_name1 : [lastname1, lastname2],
    first_name2 : [lastname3, lastname4],
    }
"""
name_dict = {}

"""
fill the values in the dictionary
if the name is for the first time put empty list
"""
for first_name, last_name in student_names:
    if first_name not in name_dict:
        name_dict[first_name] = []
    name_dict[first_name].append(last_name)

# show dict contents
for first_name in name_dict:
    print(first_name, len(name_dict[first_name]))


"""
filter out first names which have
more than 1 surname with
if conditionals
"""
for first_name in name_dict:
    if len(name_dict[first_name]) > 1:
        print(f"There are %d students having first name %s" %
              (len(name_dict[first_name]), first_name))
        for surname in name_dict[first_name]:
            print(surname, end=" ")
        print()


# list comp one line
# [print("There are %d students having first name %s" % (len(name_dict[key]), key)) for key in name_dict if len(name_dict[key]) > 1]
