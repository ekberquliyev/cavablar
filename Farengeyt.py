def F(selsi, air_speed):
    farengeyt = selsi*1.8 + 32
    print (farengeyt,"Farengeyt")
    wct_index = 35.74 + 0.6215 * farengeyt - 35.75 * air_speed**0.16 + 0.4275 * farengeyt * air_speed**0.16
    print("Soyuq Kuleyin Temperaturunun indeksi: ",wct_index)

F(10, 15)
F(0, 25)
F(-10, 35)
def wct():
    air_temp = int(input("Havanın temperaturunu daxil edin: "))
    air_speed = int(input("Havanın sürətini daxil edin: "))
    wct_index = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
    return "Soyuq Kuleyin Temperaturunun indeksi: ", wct_index
print(wct())