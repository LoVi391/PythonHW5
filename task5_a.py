

import random
k = 2018
while k != 0:
    a = int(input("1 игрок: "))
    k -= a
    if k < 1:
        print('выиграл 1 игрок')
        

    b = random.randint(1, 28)
    print(f"робот сходил: {b}")
    k -= b
    if k < 1:
        print('выиграл робот')
       

flag = True
i = 0
while flag:
    if i == 1000:
        flag = False 
    i +=1
print('END!')


