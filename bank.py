##f = open("tarixce.txt")
##f.close()
print("""(1)Total
(2)Deposit
(3)Withdraw
(4)Cancel""")
while (True):
    e = input("Secdiyiniz emeliyyati daxil edin: ")
    if e == "1":
        with open("bank.txt") as y:        
           lines = y.readlines()
           print(lines)
           x = lines[0].split(",")
           print(x)
           total_money = 0
           for number in x:
               number_int = int(number)
               total_money += number_int 
           print(total_money)
               
        y.close()
    if e == "2":
        with open("bank.txt") as y:
            lines = y.readlines()
            print(lines)
            x = lines[0].split(",")
            print(x)
            deposit_money = 0
            for number in x:
                number_int =int(number)
                if number_int > 0:
                    deposit_money +=number_int
            print(deposit_money)


        y.close()
    if e == "3":
        with open("bank.txt") as y:
            lines = y.readlines()
            print(lines)
            x = lines[0].split(",")
            print(x)
            withdraw_money = 0
            for number in x:
                number_int = int(number)
                if number_int < 0:
                    withdraw_money +=number_int
            print(withdraw_money)

    if e == "Cancel":
        break
