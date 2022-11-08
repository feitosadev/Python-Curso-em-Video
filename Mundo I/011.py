largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura

print('Sua parede tem a dimensão de {} x {} e sua área é de {}'.format(largura, altura, area))

tinta = area / 2

print('para pint aessa parede você precisará de {}L de tinta.'.format(tinta))