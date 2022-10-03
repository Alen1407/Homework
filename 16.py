def phone_number_ends_8(ls):
    ls_res = []
    for x in ls:
        if x['phone'][-1] == '8':
            ls_res.append(x)
    return ls_res

def dont_have_email(ls):
    ls_res = []
    for x in ls:
        if x['email'] == '':
            ls_res.append(x)
    return ls_res





di = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'}, 
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'}, {'name':'Princess', 'phone':'555-3141', 'email':''}, 
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

print(phone_number_ends_8(di))
print(dont_have_email(di))
