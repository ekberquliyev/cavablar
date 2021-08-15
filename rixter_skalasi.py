def e_q(richter):
    Energy = 10 ** ( 1.5 * richter + 4.8)
    print ("Zəlzələ zamanı ayrılan enerji:", Energy, "coil")
    tnt = Energy/(4.184 * 10 ** 6)
    print(tnt, "partlayisina beraberdir")
e_q(1)
e_q(5)
e_q(9.1)
e_q(9.2)
e_q(9.5)
def richter():
    number = int(input("Please enter a Richter scale value:"))
    number_float = float(number)
    tnt_coil = 4.184 * (10 ** 6)
    richter_joules = 10 ** (1.5 * number_float + 4.8)
    tnt = richter_joules/tnt_coil
    return "Coil:",richter_joules,"TNT:",tnt
print (richter())