import random
print("""Oyuna xos gelmisiniz.
Zehmet olmasa 'Rock', 'Paper', 'Scissor' daxil edin""")
hesab = [0,0]
while(True):
    print(f"COMPUTER {hesab[0]} - USER {hesab[1]}" )
    user_choice = (input("enter your choice: "))
    print(f"YOUR CHOICE-{user_choice}")

    choice_list = ["Rock","Paper","Scissor"]
    comp_choice = random.choice(choice_list)
    print(f"COMP CHOICE-{comp_choice}")

    if comp_choice == user_choice:
          print("**Draw**")
    #ILK 3 ELIF COMPUTERIN QAZANILMASI USULUDU
    elif comp_choice == "Rock" and user_choice == "Scissor":
        hesab[0] += 1 
        print ("**losts**")
        
    elif comp_choice == "Paper" and user_choice == "Rock":
        hesab[0] += 1 
        print ("**losts**")
        
    elif comp_choice == "Scissor" and user_choice == "Paper":
        hesab[0] += 1 
        print ("**losts**")
        
    #BU 3 ELIF USERIN QAZANILMASI USULUDU
    elif user_choice == "Rock" and comp_choice == "Scissor":
        hesab[1] += 1
        print ("**wins**")

    elif user_choice == "Paper" and comp_choice == "Rock":
        hesab[1] += 1
        print ("**wins**")

    elif user_choice == "Scissor" and comp_choice == "Paper":
        hesab[1] += 1
        print ("**wins**")
    
    
    else:
        print("heleki melum deil")
