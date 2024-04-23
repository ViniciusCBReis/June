import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Passo 1: Carregar os dados
data = pd.read_csv('Treinamentoia.csv')

# Passo 2: Pré-Processamento dos Dados
# Exemplo: Normalização dos dados
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data.drop(['Tipo', 'Assunto', 'Positivo'], axis=1))  # Ajuste e transformação

# Passo 3: Divisão dos Dados
X_train, X_test, y_train, y_test = train_test_split(data_scaled, data[['Tipo', 'Assunto', 'Positivo']], test_size=0.4, random_state=42)

# Passo 4: Construir o Modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(3)  # 2 saídas para 2 colunas alvo
])

# Passo 5: Compilar e Treinar o Modelo
model.compile(optimizer='adam', loss='mse')  # Mean Squared Error para regressão
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Passo 6: Avaliar o Modelo
test_loss = model.evaluate(X_test, y_test)
print("Test Loss:", test_loss)
