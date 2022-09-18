

def t_movie():
    
    print()
    print("which movie do you want to watch?")
    print()
    print("1. RRR")
    print("2. KRK")
    print("3. VTK")
    print("4. Back")
    print()

    movie=int(input("choose your movie: "))
    print()
    
    if movie==1:
        theater()
    
    elif movie==2:
        theater()

    elif movie==3:
        theater()
    
    elif movie==4:
        center()
        theater()
        return 0


def theater():
    
    print()
    print("which screen do you want: ")
    print()
    print("1. screen 1")
    print("2. screen 2")
    print("3. screen 3")
    print()

    a=int(input("choose your screen: "))
    print()
    ticket=int(input("number of ticket: "))
    print()
    timing(a)

def timing(a):
    
    time1={
        "1": "10.00 - 01.00",
        "2": "01.10 - 04.10",
        "3": "04.20 - 07.20",
        "4": "07.30 - 10.30"             
    }
    
    time2={
        "1": "10.15 - 01.15",
        "2": "01.25 - 04.25",
        "3": "04.35 - 07.35",
        "4": "07.45 - 10.45"             
    }
    
    time3={
        "1": "10.30 - 01.30",
        "2": "01.40 - 04.40",
        "3": "04.50 - 07.50",
        "4": "08.00 - 10.45"             
    }

    if a==1:

        print()
        print("choose time: ")
        print(time1)
        print()
        t=input("select your time: ")
        x=time1[t]
        print()
        print("successfully booked!enjoy the movie!")
        print()
    
    elif a==2:

        print("choose time: ")
        print(time2)
        print()
        t=input("select your time: ")
        x=time2[t]
        print()
        print("successfully booked!enjoy the movie!")
        print()
    
    elif a==3:

        print("choose time: ")
        print(time3)
        print()
        t=input("select your time: ")
        x=time3[t]
        print()
        print("successfully booked!enjoy the movie!")
        print()

    return 0

def movie(theater):

    if theater==1:
        t_movie()

    elif theater==2:
        t_movie()

    elif theater==3:
        t_movie()

    elif theater==4:
        city()

    else:
        print("wrong choice")

def center():
    
    print()
    print("which theater do you watch movie: ")
    print()
    print("1. INOX")
    print("2. ICON")
    print("3. ARRS")
    print("4. Back")
    print()

    a=int(input("choose your theater to watch a movie: "))
    print()
    movie(a)
    return 0

def city():

    print("Hi welcome to movie ticket booking: ")
    print()
    print("where you want to watch movie?: ")
    print()
    print("1. city 1")
    print("2. city 2")
    print("3. city 3")
    print("4. exit")    

    place=int(input("enter your choice: "))
    print()
    if place==1:
        center()
    
    elif place==2:
        center()

    elif place==3:
        center()

    elif place==4:
        quit()

    else:
        print("wrong choice")  
    
city()