for ran in range(1,101):
    count = 0
    for i in range(1,ran+1):
        if ran%i ==0:
            count +=1
    if count ==2:
        print(ran)
            