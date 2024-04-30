import pandas as pd
from sklearn.calibration import LabelEncoder
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import nltk
nltk.download('punkt')

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
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_encoded.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')  # 'num_classes' é o número de classes no seu problema
])

# Passo 6: Compilar e Treinar o Modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train_encoded, y_train_encoded, epochs=10, batch_size=32, validation_data=(X_test_encoded, y_test_encoded))

# Passo 7: Avaliar o Modelo
test_loss, test_accuracy = model.evaluate(X_test_encoded, y_test_encoded)
print("Test Accuracy:", test_accuracy)