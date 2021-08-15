def population():
    year = int(input("enter a year: "))
    year_day = year*365
    day_hour = year_day*24
    hour_minute = day_hour*60
    minute_seconds = hour_minute*60
    print("Daxil etdiyiniz ilde olan saniyeler: ", minute_seconds)
    new_birth = minute_seconds/8
    print("Yeni doguslarin sayi: ", new_birth)
    death = minute_seconds/12
    print("Olenlerin sayi: ", death)
    new_immiqrant = minute_seconds/29
    print("Yeni immiqrantlarin sayi: ", new_immiqrant)
    increase = new_immiqrant + new_birth - death
    print("Daxil etdiyiniz ile gore artim: ",increase)
print(population()) 