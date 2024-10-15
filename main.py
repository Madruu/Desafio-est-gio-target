
def fibonacci_sequence(limit):
    sequence = [0, 1]
    while sequence[-1] < limit:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

def is_in_fibonacci(number):
    sequence = fibonacci_sequence(number)
    return number in sequence

# Solicita ao usuário um número
num = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if is_in_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")