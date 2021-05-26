import __utilities__ as util
import csv

name, age = util.biographies()

fields = ["Names", "Age"]
rows = [name, age]
filename = input("File to be called: ")
filename = filename + ".csv"

with open(filename, "w") as csvfile:
    filewriter = csv.writer(csvfile, delimiter = ",")
    filewriter.writerow(fields)
    filewriter.writerow(rows)

print(f"Name: {name} \nAge: {age}")
print(filename)
print("Done")





# # importing the csv module 
# import csv 
# import os

# # field names 
# fields = ['Name', 'Branch', 'Year', 'CGPA'] 

# # data rows of csv file 
# rows = [['Nikhil', 'COE', '2', '9.0'], 
#         ['Sanchit', 'COE', '2', '9.1'], 
#         ['Aditya', 'IT', '2', '9.3'], 
#         ['Sagar', 'SE', '1', '9.5'], 
#         ['Prateek', 'MCE', '3', '7.8'], 
#         ['Sahil', 'EP', '2', '9.1']] 

# # name of csv file 
# filename = "university.csv"

# # writing to csv file 
# with open(filename, 'w') as csvfile: 
# 	# creating a csv writer object 
#     csvwriter = csv.writer(csvfile) 
	
#     # writing the fields 
#     csvwriter.writerow(fields) 
	
#     # writing the data rows 
#     csvwriter.writerows(rows)

