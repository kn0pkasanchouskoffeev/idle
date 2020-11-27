import random
a = (random.randint(1,100))
b = (random.randint(1,100))
a = str(a)
b = str(b)
print("a =" + a)
print("b =" + b)
c = a
a = b
b = c
print("а теперь a =" + a)
print("а b =" + b)
