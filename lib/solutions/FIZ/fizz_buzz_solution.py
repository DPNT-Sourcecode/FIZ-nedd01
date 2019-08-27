# noinspection PyUnusedLocal

def identical(num):
    l = len(num)
    f = num[0]
    c = 0
    while (c<=l-1):
        if (num[c] == f):
            if (c <= l - 1):
                return True
            c+=1

        else:
            return  False





def fizz_buzz(number):
    # if number %3 ==0 and number%5 ==0:
    #     return ('fizz buzz')
    if (number %3==0 or '3' in str(number)) and (number %5 ==0 or '5' in str (number)) and (number >10 and identfical(str(number))):
        return ('fizz buzz deluxe')
    elif  (number %3==0 or '3' in str(number)) and (number %5 ==0 or '5' in str (number))  :
        return ('fizz buzz')
    elif number %3==0 or '3' in str(number):
        return ('fizz')
    elif number %5 ==0 or '5' in str (number) :
        return ('buzz')
    elif (number >10 and identfical(str(number))):
        return ('deluxe')
    else:
        return number




