students = [
    ("Amit", "Sharma"),
    ("Amit", "Verma"),
    ("Rahul", "Gupta"),
    ("Rahul", "Mehta"),
    ("Rahul", "Singh"),
    ("Priya", "Patel"),
    ("Priya", "Shah"),
    ("Neha", "Agarwal"),
    ("Neha", "Jain"),
    ("Ankit", "Yadav"),
    ("Ankit", "Mishra"),
    ("Rohit", "Kumar"),
    ("Rohit", "Malhotra"),
    ("Sneha", "Kulkarni"),
    ("Sneha", "Deshpande"),
    ("Vikas", "Rana"),
    ("Pooja", "Nair"),
    ("Suresh", "Iyer"),
    ("Kiran", "Reddy"),
    ("Manish", "Pandey")
]

""" create dictionary with key as
first name and values as
list of surnames
"""
name_dict = {}

"""
fill the values in the dictionary
if the name is for the first time put empty list
"""
for first, last in students:
    if first not in name_dict:
        name_dict[first] = []
    name_dict[first].append(last)

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


# list comp one line
# [print("There are %d students having first name %s" % (len(name_dict[key]), key)) for key in name_dict if len(name_dict[key]) > 1]
