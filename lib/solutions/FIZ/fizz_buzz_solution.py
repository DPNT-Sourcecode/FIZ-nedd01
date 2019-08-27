# noinspection PyUnusedLocal







def fizz_buzz(number):
    # if number %3 ==0 and number%5 ==0:
    #     return ('fizz buzz')

    def identical(num):

        str1 = num
        str2 = num[::-1]
        if (int(num)<10):
            return False
        if (str1[0]== str1[1]):
            if (int (str1) - int(str2)==0) :
                return True
        else:
            return False



    if (number %3==0 or '3' in str(number)) and (number %5 ==0 or '5' in str (number)) and (number >10 and identical(str(number))):
         if (number%2==0):
            return ('fizz buzz deluxe')
         else:
             return ('fizz buzz fake deluxe')
    elif  (number %3==0 or '3' in str(number)) and (number %5 ==0 or '5' in str (number))  :
        return ('fizz buzz')
    elif (number %3==0 or '3' in str(number) )and (number >10 and identical(str(number))):
        if (number % 2 == 0):
            return ('fizz deluxe')
        else:
            return ('fizz fake deluxe')
    elif number %3==0 or '3' in str(number):
        return ('fizz')
    elif (number % 5 == 0 or '5' in str(number)) and (number >10 and identical(str(number))):
        if (number % 2 == 0):
            return ('buzz deluxe')
        else:
            return ('buzz fake deluxe')
    elif number %5 ==0 or '5' in str (number) :
        return ('buzz')
    elif (number >10 and identical(str(number))):
        if (number % 2 == 0):
            return ('deluxe')
        else:
            return ('fake deluxe')
    else:
        return number





