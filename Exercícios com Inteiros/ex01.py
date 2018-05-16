#1.  Dada uma seqüência de números inteiros não-nulos, seguida por 0, imprimir seus quadrados. 

flag = True

while flag:
    num = int(input('Digite um número: '))
    if(num == 0):
        flag = False
    print('Quadrado:{}'.format(num*num))
