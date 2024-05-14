from os import name
import time
import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

# Passo 1: Carregar os dados
data = pd.read_csv('D:/Atividades Faculdade/APS/dados/planilhaTreino-3.csv', encoding="utf8")
data['Legenda'].fillna('', inplace=True)  # Preenche os valores nulos na coluna 'Legenda' com uma string vazia

# Passo 2: Dividir os dados em features (X) e rótulos (y)
X = data['Legenda']  # Features
y = data['Relevancia']  # Rótulos

# Passo 3: Tokenização dos dados usando CountVectorizer
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Passo 4: Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Convertendo os rótulos para valores numéricos
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

# Passo 5: Construir o Modelo de Árvore de Decisão
model = AdaBoostClassifier()

# Passo 6: Treinar o Modelo de Árvore de Decisão
inicio = time.time()
m = model.fit(X_train, y_train_encoded)
fim = time.time()
tempo_treinamento = (fim - inicio) * 1000

# Passo 7: Avaliar o Modelo de Árvore de Decisão
y_pred = model.predict(X_test)
test_accuracy = accuracy_score(y_test_encoded, y_pred)
print("Test Accuracy:", test_accuracy)
print('Tempo de treinamento (ms):', tempo_treinamento)

# Salvando o modelo treinado
model_filename = name.replace(" ", "_") + ".joblib"
joblib.dump(model, model_filename)
print(f"Modelo treinado salvo como {model_filename}")