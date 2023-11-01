# Importa o módulo os para realizar operações com arquivos e diretórios
# Importa a função askdirectory do módulo tkinter.filedialog para exibir uma janela de seleção de pasta
import os
from tkinter.filedialog import askdirectory

# Abre uma janela de seleção de pasta e armazena o caminho escolhido pelo usuário em 'caminho'
caminho = askdirectory(title="Selecione uma Pasta")

# Lista todos os arquivos e diretórios dentro da pasta selecionada e armazena em 'lista_arquivos'
lista_arquivos = os.listdir(caminho)

# Define um dicionário 'locais' que mapeia tipos de arquivos para as extensões correspondentes
locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"]
}

# Itera sobre cada arquivo na pasta selecionada
for arquivo in lista_arquivos:
    # Obtém o nome do arquivo e sua extensão
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    
    # Itera sobre as categorias definidas no dicionário 'locais'
    for pasta in locais:
        # Verifica se a extensão do arquivo está na lista de extensões para a categoria atual
        if extensao in locais[pasta]:
            # Verifica se a pasta de destino para a categoria já existe, caso contrário, cria a pasta
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            # Move o arquivo para a pasta de destino
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
