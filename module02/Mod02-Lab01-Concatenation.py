# ------------------------------------------------------------------------------------------ #
# Title: Creating Strings of Characters
# Desc: Shows how data types work
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
student_first_name: str = "Vic"
student_last_name: str = "Vu"
student_gpa: float = 3.9
message = student_first_name + " " + student_last_name
message += " has a " + str(student_gpa) + " grade point average (GPA)"

# Work with the data
print(message)

