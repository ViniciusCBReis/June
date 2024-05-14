import time
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix

# Passo 1: Carregar os dados
data = pd.read_csv('D:/Atividades Faculdade/APS/dados/PlanilhaTreinoInicial.csv', encoding="utf8")

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
adaboost_classifier = AdaBoostClassifier()
models = []
models.append(('Model utilizando AdaBoost', adaboost_classifier))

#testes 
def mostrar_desempneho(X_train, y_train_encoded, X_test, y_test_encoded, model, name):
    inicio = time.time()
    model.fit(X_train, y_train_encoded)
    fim = time.time()
    tempo_treinamento = (fim - inicio)*1000
    #prevendo dados
    inicio = time.time()
    y_pred_prob = model.predict(X_test)
    fim = time.time()
    tempo_previsao = (fim - inicio)*1000
    print('Relatório Utilizando Algoritmo', name)
    print('\nMostrando Matriz de Confusão:')
    #matrix confusão
    conf_matrix = confusion_matrix(y_test_encoded, y_pred_prob)
    print(conf_matrix)
    print('\nMostrando Relatório de Classificação: ')
    print(metrics.classification_report(y_test_encoded, y_pred_prob))
    accuracy = accuracy_score(y_test_encoded, y_pred_prob)
    print('Accuracy: ', accuracy)
    relatorio = metrics.classification_report(y_test_encoded, y_pred_prob, output_dict=True)
    print('Precision', relatorio['macro avg']['precision'])
    print('Tempo de treinamento (ms): ', tempo_treinamento)
    print('Tempo de previsão (ms): ', tempo_previsao)
    return accuracy, tempo_treinamento, tempo_previsao

#bora
for name, model in models:
    print("Model:", name)
    accuracy, tempo_treinamento, tempo_previsao = mostrar_desempneho(X_train, y_train_encoded, X_test, y_test_encoded, model, name)
    print("Accuracy:", accuracy)
    print("Tempo de treinamento (ms):", tempo_treinamento)
    print("Tempo de previsão (ms):", tempo_previsao)
    print("\n")

model.save('treinocomadabost.h5')