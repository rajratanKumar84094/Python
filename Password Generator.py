#A RANDOM PASSWORD GENERATOR

import string

import random

len=int(input("Enter the Length of the Password:"))

lower=string.ascii_lowercase

upper=string.ascii_uppercase

digit=string.digits

symbols=string.punctuation

str=lower+upper+digit+symbols

str=string.printable

pswd=random.sample(str,len)

password="".join(pswd)

print(password)
