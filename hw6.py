switch = 0
j = 1

while j :
    if switch == 0:
        for i in range(1,5):
            print(f'{i+1} x {j} = {(i+1)*j:2d}',end = '   ') 
    else:
        for q in range(6,10):
            print(f'{q} x {j} = {q*j:2d}',end = '   ')
    j += 1
    print()
    
    if j == 10 and switch == 0:
        j = 1
        switch = 1
        print()
    elif j == 10 and switch == 1:
        break
