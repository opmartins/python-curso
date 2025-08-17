parede_largura = float(input('Largura da parede: '))
parede_altura = float(input('Altura da parede: '))

area = parede_largura * parede_altura
latas = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(parede_largura,parede_altura,area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(latas))
