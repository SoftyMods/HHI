f = open("HHI.txt", "r")
HHI = float(f.read())
f.close()

x = "a"

def writeHHI(HHI):
    # Write HHI to file HHI.txt with the value of HHI
    f = open("HHI.txt", "w")
    f.write(str(HHI))
    f.close()

print("The current HHI is: " + str(HHI))
print("")
while True:
    x = input("Good or Bad? ")
    if x == "+":
        HHI += 0.5
        writeHHI(HHI)
        print(HHI)
    elif x == "++":
        HHI += 1
        writeHHI(HHI)
        print(HHI)
    elif x == "+++":
        HHI += 2
        writeHHI(HHI)
        print(HHI)
    elif  x == "-":
        HHI -= 0.5
        writeHHI(HHI)
        print(HHI)
    elif  x == "--":
        HHI -= 1
        writeHHI(HHI)
        print(HHI)
    elif  x == "---":
        HHI -= 2
        writeHHI(HHI)
        print(HHI)
    else:
        print("Inalid input type + or -")
        print(HHI)

