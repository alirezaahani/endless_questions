import random
def select_operations():
    ret = random.randint(1,2)
    if ret == 1:
        return "+"
    else:
        return "*"
number1 = number2 = number3 = answer = 1
total_ques = total_correct = total_worng = hint_counter = 0
operation1 = operation2 = ""
print("Welcome to endless question game !.\nIf you want to exit or hint, type something else.")
while 1:
    operation1 = select_operations()
    operation2 = select_operations()
    number1 = random.randint(1,10)
    number2 = random.randint(1,10)
    number3 = random.randint(1,10)
    try:
        answer = int(input("{0}{1}{2}{3}{4} ? ".format(number1,operation1,number2,operation2,number3)))
        if answer == eval("{0}{1}{2}{3}{4}".format(number1,operation1,number2,operation2,number3)):
            print("Your answer is correct")
            total_correct += 1
            total_ques += 1
        else:
            print("Your answer is worng")
            total_worng += 1
            total_ques += 1
    except:
        print("Error")
        user_quit = input("Do want to exit ?(y/n)")
        if user_quit == "y":
            print("You have answered {0} questions.".format(total_ques))
            print("You have answered {0} questions correct.".format(total_correct))
            print("You have answered {0} questions worng.".format(total_worng))
            print("You used {0} hints.".format(hint_counter))
            exit()
        else:
            hint = input("Do want a know the answer ?(y/n)")
            if hint == "y":
                print("{0}+{1}*{2}={3}".format(number1,number2,number3,number1+number2*number3))
                print("But is's too late :(")
                hint_counter += 1
