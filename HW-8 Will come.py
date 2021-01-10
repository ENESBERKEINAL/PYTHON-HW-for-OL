try:
    cal = {}
    i = 1
    def search(a):
        return print(cal.get(a,"NOT FOUND!"))

    print("We are here for library dic")
    while(i<=5):
        print("\nBook ",i)
        name=input("Pls enter the book name: ")
        info=input("Pls enter the book's info: ")
        cal[name]=info
        i+=1
    print(cal)
    while True:
        searching = input("Which book want to search in library: ")
        if (searching) == "x":
            break
        search(searching)

except:
    print("Error")
    raise
