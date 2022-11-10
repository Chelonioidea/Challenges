import math
#M	1000
#CM	900
#D	500
#CD	400
#C	100
#XC	90
#L	50
#XL	40
#X	10
#IX	9
#V	5
#IV	4
#I	1

def roman_num(num):
    M = math.floor(num / 1000)
    num -= M * 1000
    CM = math.floor(num / 900)
    num -= CM * 900
    D = math.floor(num / 500)
    num -= D * 500
    CD = math.floor(num / 400)
    num -= CD * 400
    C = math.floor(num / 100)
    num -= C * 100
    XC = math.floor(num / 90)
    num -= XC * 90
    L = math.floor(num / 50)
    num -= L * 50
    XL = math.floor(num / 40)
    num -= XL * 40
    X = math.floor(num / 10)
    num -= X * 10
    IX = math.floor(num / 9)
    num -= IX * 9
    V = math.floor(num / 5)
    num -= V * 5
    IV = math.floor(num / 4)
    num -= IV * 4
    I = math.floor(num / 1)
    num -= I * 1
    roman = "M" * M + "CM" * CM + "D" * D + "CD" * CD + "C" * C + "XC" * XC + "L" * L + "XL" * XL + "X" * X + "IX" * IX + "V" * V + "IV" * IV + "I" * I

    return roman

print(roman_num(10002))
tests = [3999, 2014, 1023, 1006, 1004, 891, 400, 83, 45, 29, 12]
new_tests = []
for test in tests:
    new_tests.append(test) 
    print(roman_num(test))

for test in new_tests:
    pass


    


