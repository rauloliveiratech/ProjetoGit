import tkinter as tk
import pyperclip
import string
import random


def gerar_senha():
    senha = ''
    senha += random.choice(
        string.ascii_uppercase.translate(str.maketrans('', '', 'OIl')))  # Adiciona uma letra maiúscula
    senha += random.choice(
        string.ascii_lowercase.translate(str.maketrans('', '', 'OIl')))  # Adiciona uma letra minúscula
    caracteres_especiais = list(
        "!@#$%".translate(str.maketrans('', '', 'OIl')))  # Cria uma lista com os caracteres especiais disponíveis
    senha += random.choice(caracteres_especiais)  # Adiciona um caractere especial
    caracteres_especiais.remove(
        senha[-1])  # Remove o caractere especial adicionado da lista de caracteres especiais disponíveis
    senha += random.choice(caracteres_especiais)  # Adiciona outro caractere especial que não esteja na senha atual

    # Adiciona os últimos quatro dígitos como números
    numeros_disponiveis = list(set(string.digits.translate(str.maketrans('', '', 'OIl'))) - set(senha))
    for i in range(4):
        senha += random.choice(numeros_disponiveis)  # Adiciona um número que não esteja na senha atual
        numeros_disponiveis.remove(senha[-1])  # Remove o último número adicionado da lista de números disponíveis

    return senha


def gerar_cinco_senhas():
    return [gerar_senha() for _ in range(5)]


def copiar_senha(senha):
    pyperclip.copy(senha)


def copiar_senhas(senhas):
    # Concatena as senhas numa única “string”, separando-as por quebras de linha
    texto = '\n'.join(senhas)
    # Copia o texto para a área de transferência
    pyperclip.copy(texto)


def exibir_senhas(senhas):
    root = tk.Tk()
    root.title("Gerador de Senhas - Acessos")
    root.resizable(False, False)
    largura_janela = 320
    altura_janela = 360
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    posicao_x = int(largura_tela - largura_janela)
    posicao_y = int((altura_tela / 2) - (altura_janela / 2))
    root.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

    frame1 = tk.Frame(root)
    frame1.pack(pady=10)
    labels = []
    for i, senha in enumerate(senhas):
        frame = tk.Frame(frame1, pady=5)
        frame.grid(row=i, column=0)

        label = tk.Label(frame, text=f"Senha {i + 1}: {senha}", bg="#DCDCDC", fg="#000000", width=20,
                         font=("Arial", 13))
        label.pack(side=tk.LEFT)
        labels.append(label)

        space_label = tk.Label(frame, width=0)
        space_label.pack(side=tk.LEFT)

        button = tk.Button(frame, text="Copiar", bg="#007bff", fg="white", padx=10,
                           command=lambda s=senha: copiar_senha(s), font=("Arial", 10), cursor="hand2")
        button.pack(side=tk.LEFT)

    frame2 = tk.Frame(root)
    frame2.pack(pady=10)

    def copiar_5_senhas():
        copiar_senhas(senhas)

    copiar_button = tk.Button(frame2, text="Copiar 5 senhas", bg="#007bff", fg="white", padx=10,
                              command=copiar_5_senhas, font=("Arial", 12), cursor="hand2")
    copiar_button.pack(side=tk.TOP)

    label2 = tk.Label(frame2, text="Operações - Multitech\nRaul Oliveira Mercadante", bg="#DCDCDC", fg="#000000", font=("Consolas", 10))
    label2.pack(side=tk.BOTTOM, pady=10)

    def reiniciar():
        root.destroy()
        gerar_senhas = gerar_cinco_senhas()
        exibir_senhas(gerar_senhas)

    gerar_button = tk.Button(frame1, text="Reiniciar", bg="#00BFFF", command=reiniciar, font=("Arial", 10),
                             cursor="hand2")
    gerar_button.grid(row=10, column=0, pady=10)

    root.mainloop()


gerar_senhas = gerar_cinco_senhas()
exibir_senhas(gerar_senhas)
