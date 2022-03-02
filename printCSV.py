import csv


def printCSV():
    print("-------------------------")
    print("Hier kommt die Datei:")
    print("-------------------------")


    with open('students.csv') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            print("Name: {}, \t Geburtstag: {}".format(row[0], row[1]))