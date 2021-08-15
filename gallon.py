def gallon():
    gallon_number = int(input("enter a gallon number: "))
    gallon_litr = gallon_number*3.7854
    print(gallon_litr,"litr edir.")
    gallon_barel = gallon_number/19.5 
    print(gallon_barel, "barel edir.")
    gallon_co2 = gallon_number*20
    print("CO2-nin miqdari: ",gallon_co2)
    gallon_etanol = gallon_number*75.700
    print("enerji qarsiligi: ", gallon_etanol)
    gallon_dollar = gallon_number*4
    print("Dollar ile qiymeti: ", gallon_dollar)
print(gallon())