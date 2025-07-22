import random
import os
os.system('cls' if os.name == 'nt' else 'clear')
simvols_1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
simvols_2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
simvols_3 = ["!", "@", "#", "$", "%", "^", "&", "*", "_"]
simvols_4 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
while True:
    #os.system('cls' if os.name == 'nt' else 'clear')
    passwd = [] 
    length = int(input("Введите длину пароля(не менее 12): \n"))
    if 12 <= length <= 18: 
        for _ in range(length):
            b = random.choice(simvols_2)
            a = random.choice(simvols_1)
            c = random.choice(simvols_2 + simvols_1 + simvols_3 + simvols_4)
            passwd.append(c)
        os.system('cls' if os.name == 'nt' else 'clear')
    else: 
        print("Не верная длина пароля!")
    print(''.join(passwd))
    
