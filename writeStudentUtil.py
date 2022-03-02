import csv

def writeStudent(Name, Birthday):
    with open('students.csv', 'a', newline='') as csvFile:
        studentwriter = csv.writer(csvFile)
        studentwriter.writerow([Name, Birthday])
        print("Datei geschrieben")