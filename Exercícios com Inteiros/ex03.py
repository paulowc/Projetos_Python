#Dado um número inteiro positivo n, imprimir os n primeiros naturais ímpares.
#Exemplo: Para n=4 a saída deverá ser 1,3,5,7.

num = int(input('Digite um numero inteiro e positivo:'))
flag = True
contador = 0
while flag:
    if(num == 0):
        flag = False
    contador += 1
    if not(contador % 2 == 0):
        print(contador)
        num -= 1
    
    
    
