"""Write a program that takes an integer n as input
and prints a right-angled triangle star pattern of height
n using nested loop
"""
# take integer input
n = int(input("Enter triangle height: "))

# define function to print the triangle using n as argument


def print_nested(n):
    print("Using nested loop")
    # validate input
    if n > 0:

        # outer loop to initialize the rows
        for i in range(n):

            # inner loop to print the star for each row
            for _ in range(i+1):

                # end prevents print function to go to newline
                print("*", end="")

            # empty print function only prints newline
            print()


# call the printing functions
print_nested(n)

print("\nUsing list comprehension")

""" using n as range going from 0 to n (n+1 excluded)
    call the print function inside the list
    use string multiplier instead of for loop
    """
[print("*"*i) for i in range(n+1)]
