from datetime import date

def calculateAge(someDate):
    today = date.today()
    age = today.year - someDate.year  
    if (someDate.month > today.month):
        age = age -1
    print("Das Alter ist: ", age)
    return age 