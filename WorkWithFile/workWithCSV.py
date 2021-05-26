import csv

with open("workWithCSV.csv", "w") as table:
    spamwriter = csv.writer(table, delimiter = ",")
    spamwriter.writerow(["one", "two", "three"])
    spamwriter.writerow(["four", "five", "six"])
    # spamreader = csv.reader(table, delimiter = ",") 
    # for row in spamreader:
    #     print(", ".join(row))

print("Done")
