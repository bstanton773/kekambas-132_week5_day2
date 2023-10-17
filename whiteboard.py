# Complete the solution so that the function will break up camel casing, using a space between words. 
# The function should return a new string.

# "camelCasing" = >  "camel Casing"
# "uncamelThisCamel" = >  "uncamel This Camel"
# "helloWorld" = >  "hello World"
# "thisIsAnotherCamelCasing" = >  "this Is Another Camel Casing"


# def solution(camel):
#     output = ''
#     for letter in camel:
#         if letter.isupper():
#             output += ' '
#         output += letter
#     return output

# import re
# def solution(camel):
#     output = ''
#     upper = re.compile('[A-Z]')
#     for letter in camel:
#         if upper.match(letter):
#             output += ' ' 
#         output += letter
#     return output

# def solution(camel):
#     return re.sub('[A-Z]',lambda x: ' ' + x.group(), camel)
import re
def solution(string):
    x = re.findall('[a-zA-z][a-z]+', string)
    return ' '.join(x)