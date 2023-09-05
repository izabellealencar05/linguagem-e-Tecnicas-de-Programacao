dic = {
    1: 'arroz',
    2: 'feijao',
    3: 'tomate',
    4: 'cebola'
}
print(dic)
l = list(dic)
print(l)
l1 = list(dic.values())
print(l1)
dic1 = {'5':'banana'}
dic.update(dic1)
dic['5'] = 'abacaxi'
print('--------novo--------')
print(dic)
