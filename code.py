import random
chance = guessed = 0
random_numbers = [random.randint(0,9) for _ in range(4)]

#input and instrucion section
print('hello and welcom to the "COWS AND BULLS" lets predict!')
print('------------------------------------------------------')
print("guess a 4 digit number")
print("'COW' -> 'CORRECT'\t'BULL' -> 'WRONG'")
print('enter single digit to exit')
print('\nANS ANS ANS ANS \tmisplaced numbers(no. of repeatation)')



while guessed != 1:
    chance += 1
    cows = bulls = 0
    
    number_list = [int(i) for i in input()]
    
    if len(number_list) == 1:
        print(random_numbers)
        exit()
        
    guessed = 1
    correct = []
    
    for i in range(4):
        if random_numbers[i] == number_list[i]:
            print('cow',end=' ')
            
        else:
            print('bull',end=' ')
            guessed = 0
            if number_list[i] in random_numbers:
                correct.append(number_list[i])
                
    if len(correct):
        print('\t',end='')
        for i in correct:
            print(i,"(",random_numbers.count(i),")",sep='',end=' ')
            
    else:
        print('\t',end='none')
    print()
    print()
    
print('---CONGRATULATIONS!!!!---')
print('attempt made = ',chance)
