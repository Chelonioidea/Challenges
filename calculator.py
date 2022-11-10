

def get_number():
    while True:
        q_num = input("Enter a number: ")
        try:
            q_num = float(q_num)
            return q_num
        except:
            q_num = input("Invalid Input. Enter a valid number or type 'end' to quit: ")
        #if q_num.lower == "end":
        #    print("Ending...")
        #    return False 


def get_opporator():
    while True:
        user_input = input("Enter a valid opporator (+, -, *, /) or type 'end' to quit: ")
        #if user_input == "end":
        #    print("Ending...")
        #    return break
        if user_input == "+" or user_input == "-" or user_input == "*" or user_input == "/" or user_input == "=":
            print("User entered: " + user_input)
            return user_input
        else:
            print("Invalid Input. Enter a valid opporator or type 'end' to quit: ")



def add_all(log, last_num):
    last_opp = "alpha"
    subtotal = 0
    for num, opp in log:
        if last_opp == "+":
            subtotal += num
            last_opp = opp
            print(f"Subtotal = {subtotal}")
        elif last_opp == "-":
            subtotal -= num
            last_opp = opp
            print(f"Subtotal = {subtotal}")
        elif last_opp == "alpha":
            subtotal = num
            last_opp = opp
            print("Alpha")
            print(f"Subtotal = {subtotal}")
    if last_opp == "+":
        subtotal += last_num
        print(f"Total = {subtotal}")
        return subtotal
    else:
        subtotal -= last_num
        last_opp = opp
        print(f"Total = {subtotal}")
        return subtotal
    


def domath():
    log = []
    num = get_number()
    while True:
        opp = get_opporator()
        if opp == "*":  
            num_2 = get_number()
            subtotal = num * num_2
            print(f"{num} * {num_2} = {subtotal}")
            num = subtotal
        elif opp == "/":
            num_2 = get_number()
            subtotal = num / num_2
            print(f"{num} / {num_2} = {subtotal}")
            num = subtotal
            
        elif opp == "+":
            log.append([num, opp])
            num = get_number()
            print(log)
        elif opp == "-":
            log.append([num, opp])
            num = get_number()
            print(log)
        else:
            return add_all(log, num)


answer = domath()
print(f"The final total is {answer}")