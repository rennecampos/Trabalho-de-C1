import math

def diferenca_finitas(f, x, h=1e-5, metodo='central'):
    if metodo == 'progressiva':
        return (f(x + h) - f(x)) / h
    elif metodo == 'regressiva':
        return (f(x) - f(x - h)) / h
    elif metodo == 'central':
        return (f(x + h) - f(x - h)) / (2 * h)
    else:
        raise ValueError("Método inválido. Use 'progressiva', 'regressiva' ou 'central'.")

if __name__ == "__main__":
    print("Digite a expressão da função em Python (ex.: math.sin(x), x**2, math.exp(x))")
    expr = input("f(x) = ")
    
    # Define f(x) usando eval
    def f(x):
        return eval(expr)
    
    x = float(input("Ponto x onde calcular a derivada: "))
    h = float(input("Valor de h (ex.: 1e-5): "))
    metodo = input("Método ('progressiva', 'regressiva' ou 'central'): ").strip()
    
    derivada = diferenca_finitas(f, x, h=h, metodo=metodo)
    print(f"Derivada aproximada de f em x={x}: {derivada}")
