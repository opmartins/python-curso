from math import sin, cos, tan, radians, degrees

a = float(input('Digite o ângulo: '))

a = radians(a)

s = degrees(sin(a))
c = degrees(cos(a))
t = degrees(tan(a))

a = degrees(a)

print('O ângulo digitado é {:.2f}. Seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(a, s, c, t))