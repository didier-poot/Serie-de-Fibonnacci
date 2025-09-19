def fibonacci(n):
    serie = []
    a = 0
    b = 1
    c = 0
    for numero in range(n):
        serie.append(a)
        c= a + b
        a = b
        b = c
    return serie

cantidad = 8
print(f"Serie de Fibonacci con {cantidad} iteraciones:")
print(fibonacci(cantidad))