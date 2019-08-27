# noinspection PyUnusedLocal

def identical(num):
    l = len(num)
    c = 0
    while (c<=l-1):
        if (num[c] == num[c+1]):
            pass
        elif (c<=l-1 and num[c] == num[c+1]):
            return True
        else:
            return  False
        c+=1




def fizz_buzz(number):
    # if number %3 ==0 and number%5 ==0:
    #     return ('fizz buzz')
    if (number %3==0 or '3' in str(number)) and (number %5 ==0 or '5' in str (number)) and (number >10 and identfical(str(number))):
        return ('fizz buzz deluxe')
    elif  (number %3==0 or '3' in str(number)) and (number %5 ==0 or '5' in str (number))  :
        return ('fizz buzz')0
    elif number %3==0 or '3' in str(number):
        return ('fizz')
    elif number %5 ==0 or '5' in str (number) :
        return ('buzz')
    elif (number >10 and identfical(str(number))):
        return ('deluxe')
    else:
        return number



