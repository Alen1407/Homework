def check_phone_number(str):
    ls = []
    for i in range(len(str)):
        if(str[i]!='-'):
            ls.append(str[i])
    if ((str[3]=='-' and str[7]=='-') or (str[0]=='1' and str[1]=='-' and str[5]=='-' and str[9]=='-')) and (''.join(ls).isnumeric()):
        return 1
    else:
        return 0

number = input("Enter a phone number: ")
if(check_phone_number(number)):
    print("Valid")
else:
    print("Invalid")
