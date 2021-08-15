num_1 = int(input("Please input the order of square: "))
num_2 = int(input("Please input the top left number: "))
tmp = num_2
print("The Latin Squera is:")
for i in range(num_1):
    num_2 += i
    if num_2 > num_1:
        num_2 = num_2 - num_1
        
    for e in range(num_1):        

        print(num_2, end=" ")
        num_2 += 1
        if num_2 > num_1:
            num_2 = 1
   
    num_2 = tmp
    print("")
