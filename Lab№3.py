print ("Привет друг, придумать тебе пароль?")


a = "Если да, то нажми продолжить(ENTER)"; print (a)
input('Press ENTER to continue') 

  
    
import random

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('Количество паролей?'+ "\n")
length = input('Длина пароля, сколько букв/цифр?'+ "\n")
number = int(number)
length = int(length)
for n in range(number):
    password =''

    
    for i in range(length):
        password += random.choice(chars)
    print(password)

b = "Надеюсь тебе понравился пароль."; print (b)

c = "Для того чтобы выйти, нажмите - ENTER"; print (c)


input('Press ENTER to exit') 
