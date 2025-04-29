shopping_bag = {}
while True:
    item = input('상품명? ')
    if item == '':
        print()
        break
    
    num = int(input('수량은? '))
    if (num <= 0):
        print()
        break
    
    shopping_bag[item] = num
    print(f'장바구니에 {item} {num}개가 담겼습니다.')
    print()
    
print('장바구니 보기:', shopping_bag)
print()

print('[검색]')
key = input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{key}은(는) {shopping_bag[key]}개 담겨 있습니다.')
