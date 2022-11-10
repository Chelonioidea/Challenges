cipher = {"A": "N", "B": "O", "C": "P", "D": "Q", "E": "R", "F": "S", "G": "T", "H": "U", "I": "V", "J": "W", "K": "X", "L": "Y", "M": "Z", 
"N": "A", "O": "B", "P": "C", "Q": "D", "R": "E", "S": "F", "T": "G", "U": "H", "V": "I", "W": "J", "X": "K", "Y": "L", "Z": "M"}

cipher2 = {65:78,66:79,67:80,68:81,69:82,70:83,71:84,72:85,73:86,74:87,75:88,76:89,77:90,78:65,79:66,80:67,81:68,82:69,83:70,84:71,85:72,86:73,87:74,88:75,89:76,90:77}

txt = "SERR PBQR PNZC"
output = txt.translate(cipher2)
print(output)

def cipher_loop(txt):
    code_list = []
    new_string = ""
    for letter in txt:
        if letter in cipher:
            code_list.append(cipher[letter])
        else:
            code_list.append(letter)

    for letter in code_list:
        new_string += letter

    print(new_string)
cipher_loop(txt)





