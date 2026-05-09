name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

clean_name_1 = name_1.title()
clean_name_2 = name_2.title()
clean_name_3 = name_3.title()

clean_salary_1 = int(salary_1.replace("$", "").replace(",", ""))
clean_salary_2 = int(salary_2.replace("$", "").replace(",", ""))

print(clean_name_1, clean_salary_1)
print(clean_name_2, clean_salary_2)
print(clean_name_3)

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

# lower case
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# title case
print(name_1.title())
print(name_2.title())
print(name_3.title())

salary_1 = "$82,500"
salary_2 = "$74,000"

# remove $
print(salary_1.replace("$", ""))
print(salary_2.replace("$", ""))

# check data type
clean_salary_1 = salary_1.replace("$", "")
clean_salary_2 = salary_2.replace("$", "")

print(type(clean_salary_1))
print(type(clean_salary_2))

# convert to integer in one line
salary_1_int = int(salary_1.replace("$", "").replace(",", ""))

print(salary_1_int)
print(type(salary_1_int))