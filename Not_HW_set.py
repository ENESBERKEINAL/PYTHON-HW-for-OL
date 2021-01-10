#it is a my python course in class codes
cal={}
for i in range(0,3):
    name=input("Pls enter the name:")
    phone=input("Pls enter the phone number:")
    cal[name]=phone
search=input("Enter the name for search in cal: ")
print(cal.get(search,"It is not in the list"))

for oge in cal:
    print(oge)
print("All list: ",cal)