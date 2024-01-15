import pandas as pd

# Lee el archivo CSV
data = pd.read_csv('datos/final_data.csv')

# Explora el DataFrame
print(data.head())

import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo de seaborn
sns.set(style="whitegrid")

# Gráfico de barras de puntos por juego
plt.figure(figsize=(12, 6))
sns.barplot(x='last', y='pts', data=data)
plt.title('Promedio de Puntos por Juego de Jugadores NBA All-Star')
plt.xlabel('Apellido del Jugador')
plt.ylabel('Puntos por Juego')
plt.show()

