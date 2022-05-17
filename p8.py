#csv file in python
import csv
fileloc="C:\Prashanti M\emp.csv"

with open(fileloc, 'r', encoding="utf8",errors='ignore') as csvfile: #reading csv file and storing in csvfile

    #creating reader object for csv file
    csvread = csv.reader(csvfile)
    for csvlines in csvread:
        #to read data from file
        print(csvlines)

    print("Total no. of rows: %d" % (csvread.line_num))



import csv
#
#
# fields = ['Name', 'Branch', 'Year', 'CGPA']
# rows = [ ['Nikhil', 'COE', '2', '9.0'],
#          ['Sanchit', 'COE', '2', '9.1'],
#          ['Aditya', 'IT', '2', '9.3'],
#          ['Sagar', 'SE', '1', '9.5'],
#          ['Prateek', 'MCE', '3', '7.8'],
#          ['Sahil', 'EP', '2', '9.1']]
# filepath = r"C:\Prashanti M\emp.csv"
#
# with open(filepath,'w') as file:
#     csvfile =csv.writer(file)
#
#     csvfile.writerow(fields)
#     csvfile.writerows(rows)
#
#     for lines in csvfile:
#         print(lines)
#
