while (True):
    category_code = input("---Zehmet olmasa kateqoriya kodunu daxil edin--- \nEger cixmag isteyirsinizse 'q' duymesini basiniz: ")

    if not category_code:
        print("Bura Bos Qala Bilmez")
    
    elif category_code == "q" or category_code == "Q":
        print ("-"*20)
        print("Proqram qapadilir...")
        print ("-"*20)
        
    
    elif category_code == "r" or category_code == "R":
        print("Siz residential - ehali bolmesine aidsiz."
              "Qiymetler-$5 dollar və hər gallon üçün $0.0005 dollar")
        evvel = input("Zehmet olmasa suyu istifadə etməmişdən qabaq olan göstəricini daxil ediniz: ")
        sonra = input("Indi ise suyu istifadə etdikdən sonra olan göstəricini daxil ediniz: ") 
        if not evvel.isdigit() or not sonra.isdigit():
            print("Zehmet Olmasa Reqem Daxil Edin!!!")
        else:
            total = int(sonra) - int(evvel)
            gallon = total / 10
            print ("Toplam isletdiyiniz suyun miqdari - {} gallon.".format(gallon))

            borc = gallon * 5
            gallon1 = gallon * 0.0005
            print ("-"*20)
            print ("Ve her gallona gore olan borcunuz - {} $".format(gallon1))
            print ("-"*20)

            total_borc = borc + gallon1
            print ("-"*20)
            print ("Toplam borcunuz - {} $".format(total_borc))
            print ("-"*20)
        

    elif category_code == "c" or category_code == "C":
        print("Siz commercial bolmesine aidsiz."
              "Qiymetler-4 milyon gallona qədər $1000 dollar və hər əlavə gallon üçün $0.00025 dollar")
        evvel = input("Zehmet olmasa suyu istifadə etməmişdən qabaq olan göstəricini daxil ediniz: ")
        sonra = input("Indi ise suyu istifadə etdikdən sonra olan göstəricini daxil ediniz: ") 
        if not evvel.isdigit() or not sonra.isdigit():
            print("Zehmet Olmasa Reqem Daxil Edin!!!")
        else:
            total = int(sonra) - int(evvel)
            gallon = total / 10
            print ("Toplam isletdiyiniz suyun miqdari - {} gallon.".format(gallon))
            if int(gallon) < 40000:
                borc = gallon * 1000
                print ("-"*20)
                print ("Toplam borcunuz1 - {} $".format(borc))
                print ("-"*20)
            else:
                gallon1 = gallon * 0.0025
                print ("-"*20)
                print("Limiti kecdiyinize gore sizden artiq borc tutulur2")
                print ("-"*20)
                print("Her gallona gore olan borcunuz2- {} $".format(gallon1))
                print ("-"*20)
                borc = gallon * 1000
                print ("-"*20)
                print("Isletdiyiniz suya gore olan borcunuz2 - {} $".format(borc))
                print ("-"*20)
                total_borc = borc + gallon1
                print ("-"*20)
                print("Toplam borcunuz2 - {} $".format(total_borc))
                print ("-"*20)



    elif category_code == "i" or category_code == "I":
        print("Siz industrial - istehsalat bolmesine aidsiz.\nQiymetler-4 milyon gallon-a qədər $1000 dollar,\n4 milyon gallon-dan 10 milyon gallona qədər $2000 dollar,\nƏgər 10 milyon gallonu aşarsa onda hər gallon üçün $0.00025 dollar elave olunur")
        evvel = input("Zehmet olmasa suyu istifadə etməmişdən qabaq olan göstəricini daxil ediniz: ")
        sonra = input("Indi ise suyu istifadə etdikdən sonra olan göstəricini daxil ediniz: ") 
        if not evvel.isdigit() or not sonra.isdigit():
            print("Zehmet Olmasa Reqem Daxil Edin!!!")
        else:
            total = int(sonra) - int(evvel)
            gallon = total / 10
            print ("Toplam isletdiyiniz suyun miqdari - {} gallon.".format(gallon))
            if int(gallon) < 40000:
                borc = gallon * 1000
                print ("-"*20)
                print ("Toplam borcunuz3 - {} $".format(borc))
                print ("-"*20)
            elif 40000 <= int(gallon) < 100000:
                borc = gallon * 2000
                print ("-"*20)
                print ("Toplam borcunuz3 - {} $".format(borc))
                print ("-"*20)
            else:
                borc = gallon * 2000
                print ("isletdiyiniz suya gore borcunuz3 - {} $".format(borc))
                print ("-"*20)
                gallon1 = gallon * 0.0025
                print ("Limiti Kecdiyinize Gore Sizden Artiq Borc Tutulur")
                print ("-"*20)
                print ("Gallona Gore Olan Borcunuz- {} $".format(gallon1))
                total_borc = borc + gallon1
                print ("-"*20)
                print("Toplam Borcunuz - {} $".format(total_borc))
                print ("-"*20)









        


