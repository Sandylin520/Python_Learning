def ask_for_input():
    while True:
        try:
            result = int(input("Please provide number:"))
        except:
            print("Whoops!that's not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("I'm going to ask you again")

ask_for_input()