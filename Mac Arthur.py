while(True):
    doguldugu_ay = input("Doguldugunuz ayi daxil edin: ")
    yas = input("Yasinizi daxil edin: ")

    if not doguldugu_ay.isdigit():
        print ("Duzgun daxil edin1: ")
        continue
    elif not yas.isdigit():
        print ("Duzgun daxil edin2: ")
        continue
    else:
        if  int(doguldugu_ay) > 12:
            print ("Duzgun daxil edin3: ")
            continue
        
        else:
            ay = int(doguldugu_ay )
            yas1 = int(yas)

            xususi_reqem = (ay * 2 + 5) * 50 + yas1 - 365
            print(xususi_reqem)
            evvelki_reqem = xususi_reqem + 115
            if evvelki_reqem >1000:
                print(f"ay: {str(evvelki_reqem)[0:2]}, yas1: {str(evvelki_reqem)[2:]}")
            else:
                print(f"ay: {str(evvelki_reqem)[0]}, yas1: {str(evvelki_reqem)[1:]}")
            

