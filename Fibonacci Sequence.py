while True:
    try:
        def greet():
            print("\nThat's it :)")
            userinput()
            dummy = input("\nPress Enter to exit ")


        def sequence(number):
            output = ""
            num1 = 0
            num2 = 1
            if number == -2:
                output += "\nOkay nothing to show here, hope you have a good day! "
            elif number == -1:
                output += "\n0 "
            elif number == 0:
                output += "\n0, 1 "
            else:
                for x in range(0, number+1):
                    num3 = num1 + num2
                    if x == 0:
                        output += "\n0, "
                        output += "1,"
                    else:
                        output += f" {num3},"
                        num1 = num2
                        num2 = num3
            print(output[:-1])
            greet()


        ifRun = False


        def userinput():
            global ifRun
            if ifRun:
                seqnumber = input("\nHow many numbers of the Fibonacci sequence do you need? You may just press Enter to exit now: ")
                if seqnumber == "":
                    exit()
            else:
                seqnumber = input("Hi there!, how many numbers of the Fibonacci sequence do you need? ")
                seqnumber = int(seqnumber)
                ifRun = True
            if int(seqnumber) > 1000:
                print("Sorry, max limit is 1000.")
                userinput()
            elif int(seqnumber) < 0:
                print("A postive integer was expected... Try again")
                userinput()
            else:
                sequence(int(seqnumber)-2)


        userinput()

    except ValueError:
        ifRun = True
        print("\nInteger value expected. Try again...\n")
