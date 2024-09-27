# def get_multiplied_digits(number):
#    str_number = str(input('Введите число 40203: '))
#    first = str_number[1:]
#    number = first * get_multiplied_digits(int(str_number[1:]))
#
def get_multiplied_digits(number):
   str_number = str(number)
   first = str_number[1:]
   return first * get_multiplied_digits(int(str_number[1:]))

get_multiplied_digits(234324)