# 2. Programa para verificar se um número pertence à sequência de Fibonacci
def fibonacci_sequence(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

num = int(input("Informe um número: "))

if fibonacci_sequence(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
    


