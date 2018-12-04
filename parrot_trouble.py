def parrot_trouble(isTalking,time):
    if(time >= 8 and time <=20 and isTalking =="Y" or isTalking == "N"):
        print("Yor are not in trouble")
    elif(time <= 7 or time >20 and isTalking =="Y"):
        print("Yor are in trouble")

    elif (time <= 7 or time > 20 and isTalking == "N"):
        print("Yor are not in trouble")


isTalking = input("Parrot is Talking Y or N : ")
time = int(input("Enter time between 0 to 23: "))
parrot_trouble(isTalking, time)