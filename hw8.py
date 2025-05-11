def buy(dic):
    print('[구입]')
    item = input('상품명? ')

    if item == '':
        print()
        return False

    num = int(input('수량은? '))
    dic[item] = num    
    print(f'장바구니에 {item} {num}개가 담겼습니다.')
    print()
    return True

def show(dic):
    print('>>> 장바구니 보기:', shopping_bag)
    print()

def find(dic):
    print('[검색]')
    key = input('장바구니에서 확인하고자 하는 상품은? ')
    if key not in dic:
        print(f'장바구니에 {key}은 (는) 없습니다.')
    else:
        print(f'{key}은(는) {shopping_bag[key]}개 담겨 있습니다.')

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
    
show(shopping_bag)
find(shopping_bag)




