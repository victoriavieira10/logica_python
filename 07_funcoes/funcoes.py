#função sem retorno e sem parametros 
def sobre():
    print("Desenvolvido por: Victoria Vieira")

#Função sem retorno e com parâmetros
def turma(turma):
    print(f"Turma:{turma}")

# Função com retorno e com parametros
def somar(numero1, numero2):
    return numero1 + numero2

sobre()
turma("AD-05")


numero1 = float(input("Digite o primeiro Numero:"))
numero2 = float(input("Digite o segundo Numero:"))


resultado = somar(numero1, numero2)
print(f"A soma de {numero1} + {numero2} = {resultado}")