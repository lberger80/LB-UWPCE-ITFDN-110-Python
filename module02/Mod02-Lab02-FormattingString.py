# ---------------------------------------------------------------------------- #
# Title: Mod02-Lab02-Formatting
# Desc: This lab demonstrates using the format() function
# Change Log: (Who, When, What)
#   Lora Berger, 2024-10-21, Create Script
# ---------------------------------------------------------------------------- #
"""
* Use the format() function or f-string instead of concatenation
* Use the following data: Vic Vu, 3.9 GPA and Sue Jones, 4.0 GPA
"""
# Define the program data variables
student_first_name = "Vic"
student_last_name = "Vu"
student_gpa = 3.9
message = f"Student {student_first_name} {student_last_name} has a \
{student_gpa} grade point average (GPA)"

# Output program data
print(message)

# Define the program data variables
student_first_name = "Sue"
student_last_name = "Jones"
student_gpa = 4.0
message = f"Student {student_first_name} {student_last_name} has a \
{student_gpa} grade point average (GPA)"

# Output program data
print(message)