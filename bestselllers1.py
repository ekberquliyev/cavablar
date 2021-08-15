def open_file():
    x1 = open("bestsellers.txt")

    book_list = []

    for line in x1:
        setr_listi = line.strip().split("\t")
        book_list.append(setr_listi)
    return book_list

def first():
    
    b_year = int(input("Enter beginning year: "))
    e_year = int(input("Enter ending year: "))
    if b_year < e_year:
        for k in range(b_year,e_year + 1):
            
            m = str(k)
            j = open_file()
            print("ALL TITLES BETWEEN {} and {} :".format(b_year,e_year))
            for l in j:
                if m in l[3]:
                    print("-"*25)
                    print(l[0],l[1],l[2],l[3],l[4])
    else:
        raise("ERROR")
    return  


def third():
    author_s_name = input("Enter an author's name (or part of a name): ")
    c = open_file()
    print("SEARCH RESULT...")
    for w in c:
        if author_s_name in w[1]:
            print("-"*25)
            print(w[0],w[1],w[2],w[3],w[4])
        else:
            continue
    return ("Axtarisiniz netice vermedi...")




def fourth():
    title_name = input("Enter an title name: ")
    c = open_file()
    print("SEARCH RESULT...")
    for w in c:
        if title_name in w[0]:
            print("-"*25)
            print(w[0],w[1],w[2],w[3],w[4])
        else:
            continue
    return ("Axtarisiniz netice vermedi...")

def second():
    month = int(input("Enter month (as a number, 1-12): "))
    year = int(input("Enter year: "))
    c = open_file()

    month_str = str(month)
    year_str = str(year)
    for w in c:
        if month_str in w[3] and year_str in w[3]:
            print(w[0],w[1],w[2],w[3],w[4])
        else:
            continue
    return ("Axtarisiniz netice vermedi...")         


def interface():
    x = """(1)-Look up year range:
    (2)-Look up month/year:
    (3)-Search for author:
    (4)-Search for a title:
    (q or Q)-Quit
    """

    while(True):
        print(x)
        user_input = input("Please enter your choice: ")
        if user_input == "1":
            print("Look up year range")
            print (first())
        elif user_input == "2":
            print("Look up month/year")
            print(second())
        elif user_input == "3":
            print("Search for author")
            print(third())
        elif user_input == "4":
            print("Search for a title")
            print(fourth())
        elif user_input == "q" or user_input == "Q":
            print("Quit...")
            break
        else:
            print("ERROR")
    return user_input
interface()




