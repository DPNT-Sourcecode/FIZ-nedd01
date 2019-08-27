# noinspection PyUnusedLocal







def fizz_buzz(number):
    # if number %3 ==0 and number%5 ==0:
    #     return ('fizz buzz')

    def identical(num):

        str1 = num
        str2 = num[::-1]

        if (int (str1) - int(str2)==0):
            return True
        else:
            return False


        # l = len(num)
        # f = num[0]
        # c = 0
        # while (c <= l - 1):
        #     if (num[c+1] == f):
        #         if (c <= l - 1):
        #             return True
        #         c += 1
        #
        #     else:
        #         return False

    if (number %3==0 or '3' in str(number)) and (number %5 ==0 or '5' in str (number)) and (number >10 and identical(str(number))):
        return ('fizz buzz deluxe')
    elif  (number %3==0 or '3' in str(number)) and (number %5 ==0 or '5' in str (number))  :
        return ('fizz buzz')
    elif number %3==0 or '3' in str(number):
        return ('fizz')
    elif number %5 ==0 or '5' in str (number) :
        return ('buzz')
    elif (number >10 and identical(str(number))):
        return ('deluxe')
    else:
        return number



