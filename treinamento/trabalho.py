import numpy as np
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.calibration import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import nltk
nltk.download('punkt')
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics
import time

# Passo 1: Carregar os dados

data = pd.read_csv('D:/Atividades Faculdade/APS/treinamento/treinamentoia2.csv', encoding="utf8")

# Passo 2: Dividir os dados em features (X) e rótulos (y)
X = data.drop(data.columns[4], axis=1)  # Features
y = data.iloc[:, 4]  # Rótulos

# Passo 3: Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Passo 4: Codificar as variáveis categóricas usando OneHotEncoder
encoder = OneHotEncoder(handle_unknown='ignore')
X_train_encoded = encoder.fit_transform(X_train)
X_test_encoded = encoder.transform(X_test)
print(y_train.unique())

# Codificar os rótulos usando LabelEncoder
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)  # Somente 'Positivo' é codificado
y_test_encoded = label_encoder.transform(y_test)

# Passo 5: Construir o Modelo
models = []

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_encoded.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')  # 'num_classes' é o número de classes no seu problema
])

#model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#models.append(('Model with Adam', model))
#mlp_classifier = MLPClassifier(hidden_layer_sizes=(64, 32), activation='relu', solver='adam', max_iter=1000, random_state=42)
#models.append(('Model com MLP', mlp_classifier))
#decision_tree_classifier = DecisionTreeClassifier(random_state=42)
#models.append(('Modelo com Arvore de decisões', decision_tree_classifier))
#random_forest_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
#models.append(('Model com RandomForest', random_forest_classifier))
#adaboost_classifier = AdaBoostClassifier(n_estimators=100, random_state=42)
#models.append(('Model utilizando AdaBoost', adaboost_classifier))
#knn_classifier = KNeighborsClassifier(n_neighbors=5)
#models.append(('Modelo utilizando KNN', knn_classifier))
#logistic_regression = LogisticRegression(random_state=42)
#models.append(('Model utilizando Regressão Logística', logistic_regression))
#svm_classifier = SVC(kernel='linear', random_state=42)
#models.append(('Modelo utilizando SVC', svm_classifier))
gaussian_nb = GaussianNB()
models.append(('Model utilizando Gaussian_nb', gaussian_nb))

#Prints do trabalho
print('\nMostrando os 5 primeiros regsitros:')
pd.options.display.max_columns = None
print(data.head(5))
print('\nMostrando as informações do DataFrame:')
data.info()
print('\nMostrando Labels: ')
print(data.iloc[:, 4] .value_counts())

#funç relatório
def mostrar_desempneho(X_train_encoded, y_train_encoded, X_test_encoded, y_test_encoded, model, name):
    inicio = time.time()
    model.fit(X_train_encoded, y_train_encoded)
    fim = time.time()
    tempo_treinamento = (fim - inicio)*1000
    #prevendo dados
    inicio = time.time()
    y_pred_prob = model.predict(X_test_encoded)
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
    
#modelos
# Iterar sobre os modelos, treinar e avaliar
for name, model in models:
    print("Model:", name)
    accuracy, tempo_treinamento, tempo_previsao = mostrar_desempneho(X_train_encoded, y_train_encoded, X_test_encoded, y_test_encoded, model, name)
    print("Accuracy:", accuracy)
    print("Tempo de treinamento (ms):", tempo_treinamento)
    print("Tempo de previsão (ms):", tempo_previsao)
    print("\n")