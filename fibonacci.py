'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1
e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número,
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se
o número informado pertence ou não a sequência.
'''

def fibonacci ():
    a= 0;
    b = 1;
    fib = [0]
    while True:
        f = a + b
        if f > 1000:  # Condição de parada para evitar que a sequência se torne infinita
            break
        fib.append(f)
        a = b;
        b = f;
    return fib

num = int(input('Digite um numero inteiro menor que 1000: '))
fib = fibonacci()
print('Sequência de Fibonacci: ', fib)
if num in fib:
    print('%d pertence a sequência' %(num))
else:
    print('%d não pertence a sequência' %(num))