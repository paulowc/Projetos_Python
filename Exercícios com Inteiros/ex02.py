#2.  Dado um número inteiro positivo n, calcular a soma dos n primeiros números inteiros positivos.

flag = True
while (flag):
    i = int(input('Digite um numero inteiro positivo: '))
    soma= 0;
    if(i == 0):
        flag = False
    while(0<=i):
        soma += i
        i -= 1
    print('A soma dos n primeiros números inteiros positivos é {}'.format(soma))
        
