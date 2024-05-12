import os
import re

def remover_emojis(texto):
    # Expressão regular para encontrar emojis
    padrao = re.compile("["
                        u"\U0001F600-\U0001F64F"  # emoticons
                        u"\U0001F300-\U0001F5FF"  # símbolos e pictogramas diversos
                        u"\U0001F680-\U0001F6FF"  # transporte e símbolos de mapa
                        u"\U0001F1E0-\U0001F1FF"  # bandeiras (iOS)
                        u"\U00002500-\U00002BEF"  # caracteres chineses comuns
                        u"\U00002702-\U000027B0"
                        u"\U00002702-\U000027B0"
                        u"\U000024C2-\U0001F251"
                        u"\U0001f926-\U0001f937"
                        u"\U00010000-\U0010ffff"
                        u"\u2640-\u2642"
                        u"\u2600-\u2B55"
                        u"\u200d"
                        u"\u23cf"
                        u"\u23e9"
                        u"\u231a"
                        u"\ufe0f"  # variante seletora de modificador
                        u"\u3030"
                        "]+", flags=re.UNICODE)
    return padrao.sub(r'', texto)

def formatar_arquivo_entrada(entrada, saida):
    with open(entrada, 'r', encoding='utf-8') as arquivo_entrada:
        texto = arquivo_entrada.read()
        texto_formatado = remover_emojis(texto).replace(',', '')
        with open(saida, 'w', encoding='utf-8') as arquivo_saida:
            arquivo_saida.write(texto_formatado)

# Diretório com os arquivos de entrada
diretorio_entrada = 'D:/Atividades Faculdade/APS/dados/txtsdetreino'
# Diretório para os arquivos de saída
diretorio_saida = 'D:/Atividades Faculdade/APS/dados/lgndform'

# Iterar sobre os arquivos na pasta de entrada
for arquivo in os.listdir(diretorio_entrada):
    if arquivo.endswith('.txt'):
        # Caminho completo do arquivo de entrada
        caminho_arquivo_entrada = os.path.join(diretorio_entrada, arquivo)
        # Nome do arquivo de saída (adicionando _formatado antes da extensão)
        nome_arquivo_saida = arquivo.split('.')[0] + '_formatado.txt'
        # Caminho completo do arquivo de saída
        caminho_arquivo_saida = os.path.join(diretorio_saida, nome_arquivo_saida)
        # Formatar o arquivo de entrada e salvar o arquivo de saída
        formatar_arquivo_entrada(caminho_arquivo_entrada, caminho_arquivo_saida)

print("Processamento concluído.")