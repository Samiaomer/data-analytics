# Variables
student_name = "Samia"
student_major = "ARB"  # Change this to test different major codes

# Lookup major name and department office based on major code
if student_major == "BIOL":
    major_name = "Biology"
    department_office = "Science Bldg, Room 310"
elif student_major == "CSCI":
    major_name = "Computer Science"
    department_office = "Sheppard Hall, Room 314"
elif student_major == "ENG":
    major_name = "English"
    department_office = "Kerr Hall, Room 201"
elif student_major == "HIST":
    major_name = "History"
    department_office = "Kerr Hall, Room 114"
elif student_major == "MKT":
    major_name = "Marketing"
    department_office = "Westly Hall, Room 310"
elif student_major == "ARB":
    major_name = "Arabic"
    department_office = "Westly Hall, Room 320"
else:
    major_name = "<unknown>"
    department_office = ""

# Print results
print("Student Name:", student_name)
print("Major:", major_name)
if department_office != "":
    print("Department Office:", department_office)