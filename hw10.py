def input_scores() :
    print('[점수 입력]')
    num = 1
    i = 1
    list_ = []
    while True :
        num =int(input(f'#{i}? '))
        if num < 0 :
            break
        
        list_.append(num)
        i += 1
        
    return list_

def get_average(list_) :
    a = 0
    for i in range(len(list_)) :
        a += list_[i]
        
    return a / len(list_)

def show_scores(list_) :
    for i in range(len(list_)) :
            print(list_[i], end = ' ')
    
import pickle
import os

filepath = 'score.bin'

def save(list_) :
    with open(filepath, 'wb') as file :
        for it in list_ :
            pickle.dump(it, file)
        pickle.dump('avg', file)
        pickle.dump(get_average(list_), file)

def load() :
    lst = []
    i = 0
    with open(filepath, 'rb') as file :
        while True :
            lo = pickle.load(file)
            if lo == 'avg' :
                break
            else :
                lst.append(lo)
        lo = pickle.load(file)
        lst.append(lo)
    return lst

if not(os.path.exists(filepath)) :
    lst = input_scores()
    print()

    print('[점수 출력]')
    print('개인점수:', end = ' ')
    show_scores(lst)
    
    print()
    print(f'평균: {get_average(lst):.1f}')

    save(lst)
    i = len(lst)
else :
    print('[파일 읽기]')
    print()

    print('[점수 출력]')
    print('개인점수:', end = ' ')
    list_ = load()
    
    for i in range(len(list_)) :
        if list_[i] != list_[-1] :
            print(list_[i], end = ' ')
        else :
            print()
            print(f'평균: {list_[-1]:.1f}')
    
