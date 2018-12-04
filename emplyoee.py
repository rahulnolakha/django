def analysize(ename,esal,edesig):

    if(edesig == 'm' or edesig == 'M'):
        bonus = (0.2)*esal
        totalSalary = esal + bonus
        return [esal,bonus,totalSalary]
        #return {"esal":esal,"bonus":bonus,"ts":totalSalary}

    elif(edesig == 'a' or edesig == 'A'):
        bonus = (0.1) * esal
        totalSalary = esal + bonus
        return [esal, bonus, totalSalary]

    else:
        bonus = (0.05) * esal
        totalSalary = esal + bonus
        return [esal, bonus, totalSalary]



ename = input("Enter Emplyoee Name : ")
esal = float(input("Enter Emplyoee salary : "))
edesig = input("Enter Emplyoee designation M or m or a or A or c or C : ")
l1 = analysize(ename,esal,edesig)
print("Employee Salary : "+str(l1[0]))
print("Employee Bonus : "+str(l1[1]))
print("Employee Total Salary : "+str(l1[2]))