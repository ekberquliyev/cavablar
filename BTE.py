x1 = open("best_things_ever.txt")

best_things_ever_list = []

for line in x1:
    setr_listi = line.strip().split(", ")
    best_things_ever_list.append(setr_listi)   
#print(best_things_ever_list)
for i in best_things_ever_list[0]:
    print(i)
