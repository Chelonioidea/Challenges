import re


def panindrome(string):
    neg_i = -1
    for i in string:
        print(i)
        print(string[neg_i])
        print(i == string[neg_i])
        
        if i == string[neg_i]:
            neg_i -= 1
            continue
        elif i != string[neg_i]:
            return "Not a palindrome"
    return "Palindrome!"


menu = "Enter your string: " #PH

#while (user_input := input(menu)) != "0":

alpha = re.compile("[a-zA-Z0-9]")
input = "A man, a plan, a canal. Panama"
msg = alpha.findall(input.lower())
print(msg)
print(panindrome(msg))
