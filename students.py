import csv
from datetime import date
from datetime import datetime


studentName = input("Name des Studenten: ")
print("Name des Stundenten {}".format(studentName))

studentBirthdayInput = input("Geburtstdatum des Studenten (YYYY-MM-DD): ")
studentBirthday = date.fromisoformat(studentBirthdayInput)
print("Geburtstag des Studenten: {}".format(studentBirthdayInput))


def calculateAge(someDate):
    today = date.today()
    age = today.year - someDate.year  
    if (someDate.month > today.month):
        age = age -1
    print("Das Alter ist: ", age)
    return age 


def writeStudent(Name, Birthday):
    with open('students.csv', 'a', newline='') as csvFile:
        lineCount = 0
        studentwriter = csv.writer(csvFile)
        studentwriter.writerow([Name, Birthday])
        lineCount +=1
        print("Datei geschrieben")





studentAge = calculateAge(studentBirthday)

if studentAge < 18:
    print("Zu jung für die Datei!")
else:
    writeStudent(studentName, studentBirthday)

print("-------------------------")
print("Hier kommt die Datei:")
print("-------------------------")


with open('students.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
#        print(row)
        print("Name: {}, \t Geburtstag: {}".format(row[0], row[1]))