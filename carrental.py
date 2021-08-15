while (True):

    category_code = input("---Zehmet olmasa kateqoriya kodunu daxil edin--- \n---Eger cixmag isteyirsinizse 'q' duymesini basiniz--- \n---Seciminiz: ")
    if not category_code:
        print("Bura Bos Qala Bilmez")

    elif category_code == "q" or category_code == "Q":
        print ("-"*20)
        print("Proqram qapadilir...")
        print ("-"*20)
        break
    elif category_code == "b" or category_code == "B":
        print("Siz BUDGET bolmesini secdiniz."
              "Qiymetler-Hər gün üçün $40 dollar, hər sürülən milə görə əlavə $0.25 dollar")

        evvel = input("Zehmet olmasa sayğacın ilkin göstəricisini qeyd et: ")
        sonra = input("Indi ise sayğacın son göstəricisini qeyd et: ") 
        gun = input("Ve indi günlərin sayını daxil et: ")
        if not evvel.isdigit() or not sonra.isdigit() or not gun.isdigit():
            print("Zehmet Olmasa Reqem Daxil Edin!!!")
        else:
            total1 = (int(sonra) - int(evvel))* 0.25
            print("Mile gore odeyeceyiniz mebleg: {} $".format(total1))
            total2 = int(gun)*40
            print("Gune gore odeyeceyiniz mebleg: {} $".format(total2))
            print("Yekun mebleg: {} $".format(total1 + total2))





    elif category_code == "d" or category_code == "D":
        print("Siz DAILY bolmrsini secdiniz."
              "Qiymetler-Hər gün üçün $60 dollar"
              "əgər gündəlik sürülən məsafə 100 mili keçməyibsə onda əlavə ödəniş tələb olunmur. Əks halda hər əlavə sürülən milə görə $0.25 dollar tutulur.")

        evvel = input("Zehmet olmasa sayğacın ilkin göstəricisini qeyd et: ")
        sonra = input("Indi ise sayğacın son göstəricisini qeyd et: ") 
        gun = input("Ve indi günlərin sayını daxil et: ")
        if not evvel.isdigit() or not sonra.isdigit() or not gun.isdigit():
            print("Zehmet Olmasa Reqem Daxil Edin!!!")
        else:
            total1 = int(sonra) - int(evvel)
            if total1 < 100:
                print("Mile gore hec bir odenis teleb olunmur.")
            else:
                total1*0.25
                print("Mile gore odeyeceyiniz mebleg: {} $".format(total1))
                total2 = int(gun)*40
                print("Gune gore odeyeceyiniz mebleg: {} $".format(total2))
                print("Yekun mebleg: {} $".format(total1 + total2))




    elif category_code == "w" or category_code == "W":
        print("Həftəlik $190 dollar tutulur. Əgər həftəlik sürülən məsafə 900 mili keçməyibsə onda əlavə ödəniş tələb olunmur."
              "Əgər həftəlik məsafə 900 mildən 1500 milə qədər olubsa onda həftəlik ödənişə $100 dollar əlavə olunur"
              "Əgər həftəlik sürüş 1500 mili keçmişdirsə onda həftəlik ödəniş $200 dollar və 1500 mildən artıq məsafənin hər milinə görə $0.25 dollar tutulmalıdır.")
        evvel = input("Zehmet olmasa sayğacın ilkin göstəricisini qeyd et: ")
        sonra = input("Indi ise sayğacın son göstəricisini qeyd et: ")
        hefte = input("Zehmet olmasa heftenin sayini daxil edin: ")
        if not evvel.isdigit() or not sonra.isdigit() or not hefte.isdigit():
            print("Zehmet Olmasa Reqem Daxil Edin!!!")
        else:
            total1 = int(sonra) - int(evvel)
            if total1 < 900:
                print("Mile gore hec bir odenis teleb olunmur.")
                h_mebleg = int(hefte)*190
                print("Yekun mebleg: {} $".format(h_mebleg))

            elif total1 < 1500:
                print("Mile gore heftelik $100 elave olunur.")
                h_mebleg = (int(hefte)*190)+100
                print("Yekun mebleg: {} $".format(h_mebleg))

            elif total1 > 1500:
                print("Heftelik odenis $200 ve her mile gore $0.25 tutulur.")
                total1 = int(sonra) - int(evvel)
                print("Mile gore odeyeceyiniz mebleg: {} $".format(total1))
                h_mebleg = int(hefte)*200
                print("Heftelik mebleg: {} $".format(h_mebleg))
                total = total1 + h_mebleg
                print("Yekun mebleg: {} $".format(total))
