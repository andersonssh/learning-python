def solve(eq: str):
    eq = eq.replace(' ', '').replace('+x', 'x')

    sinal_de_x = '-' if '-x' in eq else ''

    esquerda_do_igual, numeros_do_lado_direito = eq.split('=')

    if 'x' in numeros_do_lado_direito:
        esquerda_do_igual, numeros_do_lado_direito = numeros_do_lado_direito, esquerda_do_igual

    numeros_lado_esquerdo = esquerda_do_igual.replace(f'{sinal_de_x}x', '') or '0'

    resultado_esquerdo = eval(numeros_lado_esquerdo)
    resultado_direito = eval(numeros_do_lado_direito)
    resultado_final = (resultado_esquerdo * -1) + resultado_direito

    if sinal_de_x == '-':
        resultado_final = resultado_final * -1

    return resultado_final


print(solve('- 10 = x'))
