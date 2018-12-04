def posNeg(no1,no2,boolean):
    no3 = no1
    no4 = no2


    if(no3 < 0 and no4 > 0 or no3 > 0 and no4 < 0):
        return "True"


    elif(boolean == "T" and no3 < 0 and no4 < 0):
        return "True"
    else:
        return "False"


no1 = int(input("Enter no 1 : "))
no2 = int(input("Enter no 2 : "))
boolean = input("Enter T or F : ")
print("Your result : %s"%posNeg(no1,no2,boolean))