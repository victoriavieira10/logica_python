def operadores():
  print("Escolha um operador: ")
  print("1 - + ")
  print("2 - - ")
  print("3 - * ")
  print("4 - /")


def somar():
  print(f"Resultado:{numero1 + numero2}" )
  

def subtrair():
  print(f"Resultado:{numero1 - numero2}")

def multiplicacao():
    print(f"Resultado:{numero1 * numero2}")

def divisao():
  if(numero2 == 0):
      print("Não é possível dividir por zero")
  else:
   print(f"Resultado:{numero1 / numero2}")
  
  opcao = ""
while opcao != "5":

 numero1= float(input("Digite um número: "))
 numero2= float(input("Digite o segundo numero: "))

 operadores()
 opcao = input ("Escolha uma opção:")

 if opcao =="1":
  somar()
 elif opcao == "2":
  subtrair()
 elif opcao == "3":
  multiplicacao()
 elif opcao == "4":
  divisao()
 else:
  print("Operador inválido")

