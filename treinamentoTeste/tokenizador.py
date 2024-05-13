import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Baixe as stopwords se ainda não tiver feito isso
nltk.download('stopwords')

# Defina as stopwords para o idioma desejado
stop_words = set(stopwords.words('portuguese'))  # Altere para o idioma desejado
stop_words.remove('não')

# Função para tokenizar e remover stopwords de uma string usando NLTK
def tokenize_and_remove_stopwords(text):
    tokens = word_tokenize(text)
    tokens_without_stopwords = [word for word in tokens if word.lower() not in stop_words]
    return tokens_without_stopwords

# Nome do arquivo CSV de entrada
input_file = 'D:/Atividades Faculdade/APS/treinamento/Validaçãoia.csv'

# Nome do arquivo CSV de saída (apenas para demonstração)
output_file = 'Validçãoia2.csv'

# Lista para armazenar linhas tokenizadas sem stopwords
tokenized_lines = []

# Abrir o arquivo CSV de entrada
with open(input_file, 'r', encoding='utf-8') as csv_file:
    # Criar um objeto leitor CSV
    csv_reader = csv.reader(csv_file)
    
    # Iterar sobre as linhas do arquivo CSV
    for row in csv_reader:
        # Tokenizar cada célula da linha e remover stopwords
        tokenized_row = [tokenize_and_remove_stopwords(cell) for cell in row]
        
        # Adicionar linha tokenizada sem stopwords à lista
        tokenized_lines.append(tokenized_row)

# Escrever as linhas tokenizadas sem stopwords em um novo arquivo CSV
with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
    # Criar um objeto escritor CSV
    csv_writer = csv.writer(csv_file)
    
    # Escrever linhas tokenizadas sem stopwords no arquivo CSV de saída
    csv_writer.writerows(tokenized_lines)

with open(output_file, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in range(5):  # Imprimir as primeiras 5 linhas para verificar os resultados
        print(next(csv_reader))

print("Arquivo tokenizado e stopwords removidas criado com sucesso!")