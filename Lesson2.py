import random

pas="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lenth=int(input("Укажите длину пароля "))
x=''

for i in range(lenth):
    x+=random.choice(pas)
print("Ваш пароль ",x)