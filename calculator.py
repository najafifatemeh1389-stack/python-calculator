def getnumbers()->tuple[int,int]:
    """this function get two numbers and, then you can calculate the sum or
       multiplication or division or subtract of the numbers"""
    num1, num2 = (int(input("type the first number: ")),
                  int(input("type the second number: ")))
    return num1, num2
counter = 1
history_d = {}
while True:
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.exit")
    print("6.history")
    choice = int(input("type number of your choice: "))
    if choice == 5 :
        ans = input("you want end this app for sure?(yes/no): )")
        if ans == "yes":
            break
        elif ans == "no":
            continue
        else:
            print("please type yes or no")
    if choice < 1 or choice > 6:
        print("invalid choice")
    elif choice==1:
        a,b = getnumbers()
        result = a+b
        history_d.setdefault(counter, [f"{a} + {b} = {result}"])
        print(result)
        counter += 1
    elif choice == 2:
        a,b = getnumbers()
        result = a-b
        history_d.setdefault(counter, [f"{a} - {b} = {result}"])
        print(result)
        counter += 1
    elif choice == 3:
        a,b =getnumbers()
        result = a*b
        history_d.setdefault(counter, [f"{a} * {b} = {result}"])
        print(result)
        counter += 1
    elif choice == 4:
        a,b = getnumbers()
        if b==0:
            print("your second number can't be zero")
        else:
            result = a / b
            history_d.setdefault(counter, [f"{a} / {b} = {result}"])
            print(result)
            counter += 1
    elif choice == 6:
        print(history_d)
        clear = input("do you want to clear history?(yes/no): ")
        if clear == "yes":
            history_d.clear()

