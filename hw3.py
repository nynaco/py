def get_fixed_price(per, sp):
    return int(sp / (1 - per))

per = int(input('할인율은? ')) / 100
a_sale_price = int(input('A 상품의 할인된 가격은? '))
b_sale_price = int(input('B 상품의 할인된 가격은? '))

a_price = get_fixed_price(per, a_sale_price)
b_price = get_fixed_price(per, b_sale_price)

print('A 상품의 정가는', a_price, '원')
print('B 상품의 정가는', b_price, '원')
