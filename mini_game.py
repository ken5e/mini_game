from sys import exit

def dse():
    num = input("Input your HKDSE score in best 5 (0 - 35): ")

    try:
        global dse_score
        dse_score = int(num)
    except ValueError:
        print("Man, learn to type an integer.")
        dse()

    if dse_score in range(0, 36):
        print(f"Your HKDSE score in best 5 is {dse_score}.")
    else:
        print("Enter a number range in 0 - 35.")
        dse()

    if dse_score >= 20:
        print("Congratulation! You can go to a university.")
        university()
    else:
        print("Unfortunately, you can't enter any university.")
        non_university()

def non_university():
    print("""
Although you can't enter any university,
you still can to get
\t1. an associate degree
\t2. a higher diploma
\t3. a yin-jin diploma
\t4. a job.
""")

    way_out = input("Input a number (1-4): ")

    if way_out == "1":
        asso()
    elif way_out == "2":
        hd()
    elif way_out == "3":
        yin_jin()
    elif way_out == "4":
        job()
    else:
        print("I can't understand your input.")
        non_university()

def asso():
    global degree
    degree = "associate"
    print("Now you are in an associate degree program.")
    hard = input("Do you want to 1. work hard or 2. play hard? (1-2): ")

    if hard == "1":
        print("Your hard work has paid off.")
        print("You can link up to a university.")
        university()
    elif hard == "2":
        print("Although you did not work hard, You can still graduate.")
        job()
    else:
        print("I can't understand your input.")
        asso()

def hd():
    global degree
    degree = "Higer diploma"
    print("Now you are in a higher diploma program.")
    hard = input("Do you want to 1. work hard or 2. play hard? (1-2): ")

    if hard == "1":
        print("Your hard work has paid off.")
        university()
    elif hard == "2":
        print("Although you did not work hard, you can still graduate.")
        job()
    else:
        print("I can't understand your input.")
        hd()

def yin_jin():
    global degree
    degree = "Higer diploma"
    print("Anyone can graduate from this program.")
    job()


def university():
    print("Now, you need to choose your major.")
    print("You can choose \n\t1. medical\n\t2. science\n\t3. a professional major\n\t4. a non-professional major.")
    choice = input("Input your major (1-4): ")

    global degree

    if choice == "1" and dse_score >= 32:
        print("You chose a medical degree.")
        print("You are a Doctor now.")
        print("Congratulation! You are a life winner!")
        input("Press enter to exit.")
        exit(0)

    elif (choice == "1" and dse_score < 32):
        print(f"Please know your place. you dse score is {dse_score} only.")
        university()

    elif choice == "2":
        print("The developer suggest you to choose anything but science.")
        decision = True

        while (decision):
            no_sci = input("Do you insist (y/n): ")

            if no_sci == "y":
                print("Another idiot. ")
                print("You chose a science degree.")
                degree = "science"
                decision = False
                job()

            elif no_sci == "n":
                decision = False
                university()

            else:
                print("I can't understand your input.")


    elif choice == "3":
        print("You chose a professional degree.")
        print("Nice choice!")
        degree = "professional"
        job()

    elif choice == "4":
        print("You chose a non professional degree.")
        print("Ok, I respect your choice.")
        degree = "non professional"
        job()

    else:
        print("I can't understand your input.")
        university()

def job():
    print("Now you need to find a job.")
    print("First thing first, do you want to be a police officer?")
    popo = input("Input (y/n): ")

    if popo == "y":
        print("You son of a bitch! Only dogs choose to be police officers.")
        input("Press enter to exit")
        exit(0)
    elif popo == "n":
        print("At least you have conscience.")
        print(f"You hold a {degree} degree.")
    else:
        print("I can't understand your input.")
        job()

        if degree == ("non professional" or "science"):
            print("You can't find a job. You are a beggar now.")
            print(f"You should regret that you chose a {degree} degree.")
            input("Press enter to exit")
            exit(0)

        else:
            print("You found a job. You can survive in Hong Kong.")
            input("Press enter to exit")
            exit(0)

dse()
