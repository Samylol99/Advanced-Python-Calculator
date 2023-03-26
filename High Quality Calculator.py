# Introduction
print("Hello I can calculate (almost) EVERYTHING !!!")
is_repeat = True
# Defining Calculation Functions
def add (a1, a2) :
    return (a1 + a2)
def sub (s1 , s2) :
    return (s1 - s2)
def mult (m1, m2) :
    return (m1 * m2)
def dev (d1, d2):
    return (d1 / d2)
while is_repeat :
    # Asking of the user to input numbers and opperator
    try :
        n1 = float(input("Enter the first number => "))
        op = input("Enter the operator (+ - * /) => ")
        n2 = float(input("Enter the second number => "))
        # Preparing Answer Sentence
        def print_answer (after_calculation):
            print(str(n1) + " " + op + " " + str(n2) +" = " + str(after_calculation))
        # Answering accoding to the operator
        if op == "+" :
            print_answer(add(n1, n2))
        elif op == "-" :
            print_answer(sub(n1, n2))
        elif op == "*" :
            print_answer(mult(n1, n2))
        elif op == "/" :
            print_answer(dev(n1, n2))
        else :
            print("invalid opperator")
        # Reacting to user not entering number
    except ValueError :
        print("Invalid input")
        # Reacting to user trying to devide by 0
    except ZeroDivisionError :
        print("User trying to detroy the world by 0 Devision")
    # Conclusion
    print("I know I'm great.")
    # Making it repeat
    ans = input("Do you want to caculate something else ? (answer with \"yes\" if you want \nto continue, answer with anything else to end program)\n")
    if ans == "yes" :
        is_repeat = True
        print("Okay !")
    else :
        is_repeat = False
        print("Thanks for using this program :)")