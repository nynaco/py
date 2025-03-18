def exchange(coin):
    fhun = coin // 500
    coin %= 500
    
    hun = coin // 100
    coin %= 100

    ften = coin // 50
    coin %= 50

    ten = coin // 10

    print('500원 동전의 개수:', fhun)
    print('100원 동전의 개수:', hun)
    print('50원 동전의 개수:', ften)
    print('10원 동전의 개수:', ten)

cash = int(input('동전으로 교환하고자 하는 금액은? '))

exchange(cash)
