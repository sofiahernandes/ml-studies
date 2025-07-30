import tkinter as tk # criar janelas gráficas simples
from tkinter import filedialog # abrir a janela de seleção de arquivos
import matplotlib.pyplot as plt # visualização de imagens
import matplotlib.image as mpimg # ler imagens no formato de arrays NumPy
import numpy as np # manipulação de arrays e operações matemáticas

def selecionar_imagem():
    tk.Tk().withdraw()  # Cria uma janela oculta apenas para usar o diálogo de arquivos
    return filedialog.askopenfilename(  # Abre a janela para o usuário escolher um arquivo de imagem
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp")]  # Filtros para tipos de arquivos de imagem
    )

def ler_imagem(path):
    img = mpimg.imread(path)  # Lê a imagem do caminho fornecido e retorna como array NumPy
    return img[:, :, :3] if img.shape[2] == 4 else img  # Remove o canal alpha se presente (RGBA → RGB)

def rgb_para_cinza(img):
    if img.max() <= 1.0:  # Se os valores dos pixels estiverem entre 0 e 1 (normalizados)
        img = (img * 255).astype(np.uint8)  # Converte para 0–255 e para tipo inteiro
    # Converte a imagem RGB para níveis de cinza usando pesos perceptuais (luminosidade)
    return np.dot(img[...,:3], [0.299, 0.587, 0.114]).astype(np.uint8)

def binarizar(img):
    limiar = np.mean(img).astype(np.uint8)  # Calcula o valor médio da imagem em tons de cinza como limiar
    print(f"[INFO] Limiar binarização: {limiar}")  # Exibe o limiar no terminal
    # Cria imagem binária: pixels acima ou iguais ao limiar viram 255 (branco), o resto vira 0 (preto)
    return np.where(img >= limiar, 255, 0).astype(np.uint8)

def mostrar_resultados(orig, cinza, binaria):
    # Cria uma grade de subplots 2x3 para exibir imagens e texto
    fig, axs = plt.subplots(2, 3, figsize=(18, 9))

    # Define os títulos e as imagens correspondentes
    titulos = ["Figura 1: Original", "Figura 2: Níveis de Cinza", "Figura 3: Preto e Branco"]
    imagens = [orig, cinza, binaria]
    mapas = [None, 'gray', 'gray']  # Define se a imagem será exibida com mapa de cor cinza

    # Exibe as 3 imagens nas primeiras 3 células da grade
    for i in range(3):
        axs[0][i].imshow(imagens[i], cmap=mapas[i])  # Exibe a imagem
        axs[0][i].set_title(titulos[i])  # Define o título
        axs[0][i].axis('off')  # Remove os eixos para deixar visual mais limpo

    # Texto descritivo sobre o processamento das imagens
    descricao = (
        "Descrição:\n"
        "A imagem original foi convertida para tons de cinza usando pesos perceptuais RGB, "
        "seguida de binarização com limiar baseado na média dos pixels."
    )
    # Insere o texto na célula inferior esquerda
    axs[1][0].text(0.5, 0.5, descricao, ha='center', va='center', fontsize=10, wrap=True)
    for ax in axs[1][1:]: ax.axis('off')  # Desativa os eixos das outras duas células inferiores

    # Define título geral e rodapé
    fig.suptitle("Projeto: Redução de Dimensionalidade em Imagens", fontsize=15)
    fig.text(0.5, 0.04, "Dio.me – Edson Gomes Chaves – 07-2025", ha='center', fontsize=9)

    # Ajusta o layout para evitar sobreposição de elementos
    plt.tight_layout(rect=[0, 0.08, 1, 0.94])
    plt.show()  # Exibe a janela com as imagens

    # Pergunta ao usuário se deseja salvar a imagem combinada
    if input("Salvar imagem combinada? (s/n): ").strip().lower() == 's':
        # Abre janela para o usuário escolher onde salvar a imagem
        caminho = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        if caminho:
            fig.savefig(caminho, dpi=100)  # Salva a figura inteira como imagem
            print(f"[SUCESSO] Imagem salva em: {caminho}")
        else:
            print("[INFO] Salvamento cancelado.")

def main():
    caminho = selecionar_imagem()  # Abre a janela para o usuário escolher a imagem
    if not caminho:
        print("[ERRO] Nenhuma imagem selecionada.")  # Se o usuário cancelar, exibe erro e sai
        return

    rgb = ler_imagem(caminho)  # Lê a imagem RGB
    cinza = rgb_para_cinza(rgb)  # Converte para escala de cinza
    binaria = binarizar(cinza)  # Converte para imagem binária
    mostrar_resultados(rgb, cinza, binaria)  # Mostra os resultados e oferece opção de salvar

# Ponto de entrada do programa
if __name__ == "__main__":
    main()  # Executa o processo principal
    input("Pressione ENTER para sair...")  # Espera o usuário para encerrar o terminal

## Observações:
# O uso de np.dot() é muito comum para converter RGB → cinza.
# np.where() é uma maneira bem rápida e eficiente de criar imagens binárias.
# tkinter é ótima para interfaces simples como seleção de arquivos, mas não ideal para aplicações maiores.