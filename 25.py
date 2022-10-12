def verbose(num):
    res = ""
    dic = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
        '6': 'six', '7': 'seven', '9': 'nine', '10': 'ten', '11': 'eleven',
        '12': 'twelve', '13': 'thirteen', '14':'fourteen', '15': 'fifteen', '16': 'sixteen',
        '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty', 
        '30': 'thirty', '40': 'fourty', '50': 'fifty', '60': 'sixty', '70': 'seventy',
        '80': 'eighty', '90': 'ninety', '1000': 'one thousand'
    }
    
    if str(num) in dic.keys():
        res += dic[str(num)]
    elif num >= 20 and num < 100:
        res += verbose(int(str(num)[0]+'0')) + '-' + verbose(int(str(num)[1:]))
    elif num > 100 and num < 1000:
        res += verbose(int(str(num)[0])) + ' hundreed and ' + verbose(int(str(num)[1:]))
    elif num > 1000:
        res += verbose(int(str(num)[0])) + ' thousand ' + verbose(int(str(num)[1:]))
        
        
    return res
        
        
print(verbose(999))
