f = open("Ex4A_ReadWriteFiles/about_me.txt", "a")
f.close()

f = open("Ex4A_ReadWriteFiles/about_me.txt", "a")
f.write("\nPerfect night out: Dinner at a rooftop restaurant,\n")
f.write("then a live concert, ending with a walk by the waterfront.\n")
f.close()

f = open("Ex4A_ReadWriteFiles/about_me.txt", "r")
print(f.read())
f.close()

f = open("Ex4A_ReadWriteFiles/about_me.txt", "r")
print(f.read(50))
print(f.read(50))
f.close()

f = open("Ex4A_ReadWriteFiles/about_me.txt", "r")

print(f.readline(10))   # first 10 characters of line 1
print(f.readline())     # rest of line 1

for i in range(1, 5):
    print(f.readline())  # prints next 4 lines one at a time

f.close()

f = open("Ex4A_ReadWriteFiles/about_me.txt", "r")

print(f.readlines(1))    # returns line 1 as a list
print(f.readlines(1))    # returns line 2 as a list
print(f.readlines(10))   # returns enough complete lines to cover 10 bytes
print(f.readlines(100))  # returns enough complete lines to cover 100 bytes
print(f.readlines(-1))   # returns ALL remaining lines

f.close()

f = open("Ex4A_ReadWriteFiles/about_me.txt", "r")

# a) First 50 characters
first_50 = f.read(50)

# b) Next 4 lines captured into a list
lines_list = []
for i in range(1, 5):
    lines_list.append(f.readline())

# c) Next ~100 bytes worth of complete lines
next_100 = f.readlines(100)

f.close()

print("First 50 characters:", first_50)
print("Next four lines, as list by line:", lines_list)
print("Next 100 characters, as list by line, rounded up to complete lines:", next_100)