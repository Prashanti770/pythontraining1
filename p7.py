# file1 = open(r"C:\Users\USER\Documents\fh1.txt" , 'r')
# print(file1.read(10)) # reads upto mentioned index
#
# print(file1.readlines()) #reads and gives content in single line
#
# lines1 = file1.readlines()
# print(lines1[2])   #reads by line , gives mentioned line
#
# file1.close()

# file1 = open(r"C:\Users\USER\Documents\fh1.txt", 'w')
# file1.write("write to an existing file")
# file1.write("""Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!""")
# file1 = open(r"C:\Users\USER\Documents\fh1.txt", 'r')
# print(file1.readlines())
#
#
# file1 = open(r"C:\Users\USER\Documents\fh3.txt", 'a')
# file1.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# file1 = open(r"C:\Users\USER\Documents\fh3.txt", 'r')
# print(file1.readlines())


file1 = open(r"C:\Users\USER\Documents\fh4.txt", 'r+')
file1.write("write to an existing file")
file1.write("""Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!""")
print(file1.readlines())
file1.close()