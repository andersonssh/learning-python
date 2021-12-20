# A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
#
# For example, take 153 (3 digits), which is narcisstic:
#
#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1652 (4 digits), which isn't:
#
#     1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
# The Challenge:
#
# Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10. This may be True and False in your language, e.g. PHP.
#
# Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

# teste de uso de conversao para str
def str1(v, dev):
    print('convertendo para str, solucao de :', dev)
    return str(v)

# minha solucao

def narcissistic(value):
    list_value = [int(i) for i in list(str1(value, 'minha solucao'))]
    return sum([x**len(list_value) for x in list_value]) == value

# melhor solucao da plataforma

def narcissistic2(value):
    return value == sum(int(x) ** len(str1(value, 'melhor da plataforma')) for x in str1(value, 'melhor da plataforma'))

# a minha solucao parece ser mais performatica!
narcissistic(37112342341423)
narcissistic2(37112342341423)



