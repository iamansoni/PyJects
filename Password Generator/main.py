import random

print('Welcome to your Password Generator!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGTHIJKLMOPQRSTUVWXYZ!@#$%^&*()_+.,0123456789'

number = int(input('Amount of passwords to generate: '))
length = int(input('Input your password length: '))

print('\nHere are your Passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)