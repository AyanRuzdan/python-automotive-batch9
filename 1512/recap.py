"""
MICRO PROJECT: Command-line Student Score Analyzer
Demonstrates:
- Scripting vs programming (single-file executable script)
- Python history/features (commented)
- Environment setup assumptions
- Basic datatypes, variables, keywords, comments
- Operators, casting
- I/O, formatting
- Conditionals, loops, break/continue/pass
"""

# =========================
# Introduction to Scripting
# =========================
# This file is a SCRIPT:
# - Interpreted at runtime
# - No compilation step
# - Used for automation / small utilities

# =========================
# Python Features (Comment)
# =========================
# - Interpreted
# - Dynamically typed
# - High-level
# - Cross-platform
# - Large standard library

# =========================
# Pre-requisites Assumed
# =========================
# - Python 3.x installed
# - Terminal / IDE (VS Code, PyCharm)
# - Basic programming knowledge

# =========================
# Basic Datatypes
# =========================
student_count = 0          # int
average_score = 0.0        # float
course_name = "Python"     # str
is_active = True           # bool

# =========================
# Keywords (cannot be used as variable names)
# if, else, for, while, True, False, break, continue, pass

# =========================
# Operators
# =========================
# Arithmetic
# + - * / // % **
# Comparison
# == != > < >= <=
# Logical
# and or not
# Bitwise
# & | ^ << >>

# =========================
# I/O and Type Casting
# =========================
print("Student Score Analyzer")

student_count = int(input("Enter number of students: "))

total_score = 0

# =========================
# Loop Control Statements
# =========================
for i in range(student_count):
    score_input = input(f"Enter score for student {i + 1} (0-100): ")

    if score_input == "":
        pass  # placeholder, does nothing
        continue

    score = float(score_input)

    # =========================
    # Conditional Statements
    # =========================
    if score < 0:
        print("Invalid score, skipped")
        continue
    elif score > 100:
        print("Invalid score, skipped")
        continue
    else:
        total_score += score

# =========================
# While Loop Example
# =========================
retry = True
while retry:
    confirm = input("Confirm calculation? (y/n): ").lower()

    if confirm == "y":
        retry = False
    elif confirm == "n":
        print("Aborted")
        break
    else:
        print("Invalid input")

# =========================
# Calculations
# =========================
if student_count > 0:
    average_score = total_score / student_count
else:
    average_score = 0.0

# =========================
# Output Formatting
# =========================
print("\n--- Report ---")
print("Course:", course_name)
print("Students:", student_count)
print("Average Score: {:.2f}".format(average_score))

# f-string formatting
print(f"Status: {'PASS' if average_score >= 40 else 'FAIL'}")

# =========================
# End of Script
# =========================
