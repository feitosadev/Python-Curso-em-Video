preço = float(input('Qual é o preço do produto? '))
novo = preço - (preço * 5/100)
print('O produto que custava R$ {}, na promoção com desconto de 5% o produto vai ficar R$ '.format(preço, novo))