# noinspection PyUnusedLocal
def fizz_buzz(number):
    if number %3 ==0 and number%5 ==0:
        return ('fizz buzz')
    elif number %3==0 or '3' in str(number):
        return ('fizz')
    elif number %5 ==0 or '5' in str (number) :
        return ('buzz')
    elif   ('5' in str(number) and '3' in str(number) ):
        return ('fizz buzz')
    else:
        return number


