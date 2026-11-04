import tkinter as tk

# ==========================================
# 1. FUNÇÕES OBRIGATÓRIAS DO PROJETO 5
# ==========================================

def somarmultiplosnumeros(numeros):
    soma = 0
    for num in numeros:
        soma += num
    return soma


def multiplicarmultiplosnumeros(numeros):
    produto = 1
    for num in numeros:
        produto *= num
    return produto


def ehinteiro(numero):
    if isinstance(numero, int):
        return True
    if isinstance(numero, float):
        return numero.is_integer()
    return False


def ehpar(numero):
    if ehinteiro(numero):
        return int(numero) % 2 == 0
    return False


# ==========================================
# 2. OPERAÇÕES EXTRAS (LÓGICA)
# ==========================================

def subtrairmultiplosnumeros(numeros):
    if not numeros:
        return 0
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado


def dividirmultiplosnumeros(numeros):
    if not numeros:
        return 0
    resultado = numeros[0]
    for num in numeros[1:]:
        if num == 0:
            return "Não é possível dividir por zero"
        resultado /= num
    return resultado


# ==========================================
# 3. LÓGICA DA INTERFACE TKINTER
# ==========================================

def clicar_botao(valor):
    visor.insert(tk.END, valor)


def limpar_visor():
    visor.delete(0, tk.END)


def calcular_expressao():
    try:
        expressao = visor.get()
        resultado = eval(expressao)
        limpar_visor()
        
        if ehinteiro(resultado):
            visor.insert(0, str(int(resultado)))
        else:
            visor.insert(0, str(resultado))
    except ZeroDivisionError:
        limpar_visor()
        visor.insert(0, "Não é possível dividir por zero")
    except Exception:
        limpar_visor()
        visor.insert(0, "Operador inválido")


def checar_par():
    try:
        num = float(visor.get())
        resultado = "É Par" if ehpar(num) else "Não é Par"
        limpar_visor()
        visor.insert(0, resultado)
    except Exception:
        limpar_visor()
        visor.insert(0, "Número inválido")


# ==========================================
# 4. CONSTRUÇÃO DA JANELA E DESIGN
# ==========================================

if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("Calculadora Aprimorada")
    janela.geometry("380x480")
    janela.resizable(False, False)
    janela.configure(bg="#121212")

    # Visor
    visor = tk.Entry(
        janela, 
        font=("Arial", 20, "bold"), 
        bg="#1e1e1e", 
        fg="#ff69b4", 
        bd=8, 
        relief="flat",
        justify="right"
    )
    visor.grid(row=0, column=0, columnspan=4, padx=12, pady=15, ipady=8)

    # Botão de funcionalidade especial (É Par?)
    btn_par = tk.Button(
        janela, 
        text="Verificar se é Par", 
        font=("Arial", 11, "bold"), 
        bg="#331122", 
        fg="#ff85c0", 
        command=checar_par
    )
    btn_par.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=4, pady=4)

    # Botões do Teclado
    botoes = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        'C', '0', '=', '+'
    ]

    linha = 2
    coluna = 0

    for texto in botoes:
        if texto == "C":
            cor_fundo = "#331122"
            cor_texto = "#ff4d8d"
            comando = limpar_visor
        elif texto == "=":
            cor_fundo = "#ff1493"
            cor_texto = "#ffffff"
            comando = calcular_expressao
        elif texto in "+-*/":
            cor_fundo = "#221122"
            cor_texto = "#ff85c0"
            comando = lambda t=texto: clicar_botao(t)
        else:
            cor_fundo = "#1a1a1a"
            cor_texto = "#ff69b4"
            comando = lambda t=texto: clicar_botao(t)

        btn = tk.Button(
            janela, 
            text=texto, 
            font=("Arial", 14, "bold"), 
            bg=cor_fundo, 
            fg=cor_texto,
            activebackground="#333333",
            activeforeground="#ff69b4",
            bd=0,
            command=comando
        )
        btn.grid(row=linha, column=coluna, padx=4, pady=4, sticky="nsew")
        
        coluna += 1
        if coluna > 3:
            coluna = 0
            linha += 1

    # Ajusta o tamanho automático das colunas
    for i in range(4):
        janela.grid_columnconfigure(i, weight=1)
    for i in range(1, 6):
        janela.grid_rowconfigure(i, weight=1)

    janela.mainloop()