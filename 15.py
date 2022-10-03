def has_key(dic, key):
    ls = dic.keys()
    if key in ls:
        return 1
    return 0

dic = {}
product = ''
while(1):
    product = input("Enter product name: ")
    if(product == "exit"):
        break
    price = int(input("Product price: "))
    dic[product] = price

print(dic)

while(1):
    get_name = input("Enter the product name: ")
    if get_name == "exit":
        break
    if not(has_key(dic, get_name)):
        print(get_name + " doesn`t exist in the list!")
        continue
    print(dic[get_name])


