def soma(numero1, numero2):
    return numero1 + numero2

def cria_potencia(base):
    def potencia(expoente):
        return base ** expoente
    return potencia

potencia_2 = cria_potencia(2)

print(potencia_2(2))
print(cria_potencia(2)(2))
