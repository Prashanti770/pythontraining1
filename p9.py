import csv

header = ['name','age','department']
rows=[['ram',23,'IT'],
      ['sita',24,'HR'],
      ]

filepath = "C:\Prashanti M\dept1.csv"

with open(filepath,'w', newline='') as deptfile: #newline is used to remove blank rows
      deptwrite = csv.writer(deptfile) #cretaing object for csv
      deptwrite.writerow(header)
      deptwrite.writerows(rows)



fields = ['Name', 'Branch', 'Year', 'CGPA']
rows = [ ['Nikhil', 'COE', '2', '9.0'],
         ['Sanchit', 'COE', '2', '9.1'],
         ['Aditya', 'IT', '2', '9.3'],
         ['Sagar', 'SE', '1', '9.5'],
         ['Prateek', 'MCE', '3', '7.8'],
         ['Sahil', 'EP', '2', '9.1']]
filepath = r"C:\Prashanti M\emp.csv"

with open(filepath,'w') as file:
    csvfile =csv.writer(file)

    csvfile.writerow(fields)
    csvfile.writerows(rows)

    for lines in csvfile:
        print(lines)



