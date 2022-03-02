from datetime import date
import calculateAgeUtil
import writeStudentUtil
import printCSV

studentName = input("Name des Studenten: ")
print("Name des Stundenten {}".format(studentName))

studentBirthdayInput = input("Geburtstdatum des Studenten (YYYY-MM-DD): ")
studentBirthday = date.fromisoformat(studentBirthdayInput)
print("Geburtstag des Studenten: {}".format(studentBirthdayInput))

studentAge = calculateAgeUtil.calculateAge(studentBirthday)

if studentAge < 18:
    print("Zu jung für die Datei!")
else:
    writeStudentUtil.writeStudent(studentName, studentBirthday)

printCSV.printCSV()