import re


phone_numbers = ["7027777272", "(702) 774 7777", "777.777.9999", "222-222-3434", "33#3333333", "444444444", 
                "17079999999", "1 (222) 222.2222", "1(777)9999999", "+1.333.333.3333", "1777.7777", "9999999"]

ck_phone = re.compile(r'''(
((\+1\s?)?(\d{3}|\(\d{3}\))) #area code (maybe country code)
(\s|\.|-)?                   #seperator
(\d{3})                      #first three
(\s|\.|-)?                   #seperator
(\d{4})                      #last four
)''', re.VERBOSE)

new_list = []
for phone in phone_numbers:
    new_list.append(ck_phone.findall(phone))
    default = ck_phone.findall(phone)
    print(default)
    
print(new_list)