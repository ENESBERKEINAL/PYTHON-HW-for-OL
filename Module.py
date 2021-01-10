try:
    import random
    list=[]
    input_value=int(input("How many info do you want to input: "))

    def add():
        for i in range(0,input_value):
            name = input("Pls enter the customer info: ")
            if name!="x":
                list.append(name)

    def show():
        print(list[random.randrange(0,len(list))])

except ValueError:
    print("Make sure the right input type")
except:
    print("Error")
    raise