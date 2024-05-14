import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import tensorflow as tf
from sklearn.model_selection import train_test_split
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

# Passo 1: Carregar os dados
data = pd.read_csv('D:/Atividades Faculdade/APS/dados/PlanilhaTreinoInicial.csv', encoding="utf8")

# Passo 2: Dividir os dados em features (X) e rótulos (y)
X = data.drop(data.columns[1], axis=1)  # Features
y = data.iloc[:, 1]  # Rótulos

# Passo 3: Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Passo 4: Codificar os rótulos usando LabelEncoder
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

# Passo 5: Pré-processamento adicional, se necessário (ex: tokenização)
# Exemplo de tokenização usando NLTK
X_train_tokenized = X_train.apply(lambda row: word_tokenize(row.values[0]), axis=1)
X_test_tokenized = X_test.apply(lambda row: word_tokenize(row.values[0]), axis=1)

# Passo 6: Construir o Modelo
max_length = max(len(tokens) for tokens in X_train_tokenized)
vocab_size = len(set(word for tokens in X_train_tokenized for word in tokens))

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=64, input_length=max_length),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Passo 7: Compilar e Treinar o Modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(
    tf.keras.preprocessing.sequence.pad_sequences(X_train_tokenized, maxlen=max_length),
    y_train_encoded,
    epochs=10,
    batch_size=32,
    validation_data=(tf.keras.preprocessing.sequence.pad_sequences(X_test_tokenized, maxlen=max_length), y_test_encoded)
)

# Passo 8: Avaliar o Modelo
test_loss, test_accuracy = model.evaluate(tf.keras.preprocessing.sequence.pad_sequences(X_test_tokenized, maxlen=max_length), y_test_encoded)
print("Acurácia no Teste:", test_accuracy)
