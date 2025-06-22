#Classify a persons age group: child, teenager, adult, and senior

age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age < 20:
    print("Teenage")
elif age < 90:
    print("Adult")
else:
    print("Senior")



