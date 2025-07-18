import math

def soma_riemann(f, a, b, n=1000, metodo='medio'):
    delta_x = (b - a) / n
    soma = 0.0
    for i in range(n):
        if metodo == 'esquerda':
            x_i = a + i * delta_x
        elif metodo == 'direita':
            x_i = a + (i + 1) * delta_x
        elif metodo == 'medio':
            x_i = a + (i + 0.5) * delta_x
        else:
            raise ValueError("Método inválido.")
        soma += f(x_i)
    return soma * delta_x

if __name__ == "__main__":
    print("Digite a expressão da função em Python (ex.: math.sin(x), x**2, math.exp(x))")
    expr = input("f(x) = ")
    
    def f(x):
        return eval(expr)
    
    a = float(input("Limite inferior a: "))
    b = float(input("Limite superior b: "))
    n = int(input("Número de subintervalos n: "))
    metodo = input("Método ('esquerda', 'direita' ou 'medio'): ").strip()
    
    integral = soma_riemann(f, a, b, n=n, metodo=metodo)
    print(f"Aproximação da integral de f(x) de {a} a {b}: {integral}")
