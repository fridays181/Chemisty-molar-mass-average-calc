def bars():
    print("-0=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=0-")

def tut():
    bars()
    print("The way to use this calcutor is simple")
    print("Input how many element masses you have")
    print("Type each in(go one by one the machine knows how many you have)")
    print("From this info youll know the total molar mass")
    print("Than input the elemental masses again and for each one youll find out what percent it is")
    print("The only restrictions are use whole numbers(round the elemental masses) and only use numbers(no letters)")


def howmany():
    global howmanycheck
    global total
    total = 0
    howmanycheck = int(input("How many mass's do you have to input: "))
    bars()
    for i in range(howmanycheck):
        num = int(input("What is the molar mass: "))
        total = total + num
    print("The total is: ")
    print(total)
    bars()



#the end division
def question():
    global u
    u = int(input("Whats the numerator(The molar mass's you inputed at the top): "))

def main():
    global u
    global mm
    global total
    m = u / total
    mm = m * 100
    print("Your average for this element is: " )
    print(mm)
    bars()
    
def final():
    global howmanycheck
    bars()
    y = int(input("Do you want to use the machine(enter 1) or get a quick run down on how to use the software(enter 2): "))
    if y == 1:
        howmany()
        for i in range(howmanycheck):
            question()
            main()
        x = input("Press anything to run the calculator again: ")
        final()
    else:
        tut()
        final()
final()
