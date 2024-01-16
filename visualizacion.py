import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lee el archivo CSV
data = pd.read_csv('datos/final_data.csv')

data['full_name'] = data['first'] + ' ' + data['last']

# Visualización 1:

top_teams = data['team'].value_counts().nlargest(5)
plt.figure(figsize=(10, 6))
top_teams.plot(kind='bar', color='skyblue')
plt.title('Equipos con Mayor Cantidad de Jugadores All Star')
plt.xlabel('Equipo')
plt.ylabel('Cantidad de Jugadores All Star')
plt.savefig('equipos.png')

# Visualización 2:

plt.figure(figsize=(12, 6))
sns.lineplot(x='year', y='fg_pct', data=data, label='Tiros de Campo')
sns.lineplot(x='year', y='fg3_pct', data=data, label='Tiros de 3 Puntos')
plt.title('Cambios en la Eficiencia en los Tiros de Campo a lo Largo del Tiempo')
plt.xlabel('Año')
plt.ylabel('Eficiencia en Tiros de Campo (%)')
plt.legend(title='Tipo de Tiro', loc='upper left')
plt.savefig('tiros.png')


# Visualización 3:

plt.figure(figsize=(12, 6))
sns.lineplot(x='year', y='reb', label='Rebotes', data=data)
sns.lineplot(x='year', y='stl', label='Robos', data=data)
plt.title('Tendencias en Estadísticas de Rebotes y Robos a lo Largo del Tiempo')
plt.xlabel('Año')
plt.ylabel('Promedio por Juego')
plt.legend()
plt.savefig('rebotes_robos.png')


# Visualización 4:

all_star_participations = data.groupby('full_name').size().sort_values(ascending=False).head(5)
plt.figure(figsize=(10, 6))
all_star_participations.plot(kind='bar', color='salmon')
plt.title('Jugadores con Más Participaciones en el All Star')
plt.xlabel('Jugador')
plt.ylabel('Total de Participaciones en el All Star')
plt.xticks(rotation=45, ha='right')
plt.savefig('jugadores_participaciones.png')

# Visualización 5:

# Contar la cantidad de equipos diferentes para cada jugador en el All-Star Game
teams_per_player = data.groupby(['first', 'last'])['team'].nunique()

# Obtener el top 10 de jugadores con más equipos diferentes en el All-Star Game
top_players = teams_per_player.sort_values(ascending=False).head(10)

# Crear el gráfico de barras para el top 10
plt.figure(figsize=(12, 6))
top_players.plot(kind='bar', color='skyblue')
plt.title('Top 10 de Jugadores con Más Equipos Diferentes en el All-Star Game')
plt.xlabel('Jugador')
plt.ylabel('Número de Equipos en el All-Star Game')
plt.xticks(rotation=45, ha='right')
plt.savefig('equipos diferentes.png')


# Visualización 6:

# Crear columnas adicionales para categorizar las asistencias por partido
data['asist_category'] = pd.cut(data['ast'], bins=[0, 2, 5, 9, float('inf')], labels=['0-2', '3-5', '6-9', '10+'])
data['points_category'] = pd.cut(data['pts'], bins=[0, 10, 20, 30, float('inf')], labels=['0-10', '11-20', '21-30', '31+'])
data['steals_category'] = pd.cut(data['stl'], bins=[0, 1, 3, float('inf')], labels=['0-1', '2-3', '4+'])
data['rebounds_category'] = pd.cut(data['reb'], bins=[0, 5, 10, 15, float('inf')], labels=['0-5', '6-10', '11-15', '16+'])

# Configuración de subgráficos
fig, axes = plt.subplots(2, 2, figsize=(14, 14))

# Gráfico circular para Puntos
axes[0, 0].pie(data['points_category'].value_counts(), labels=data['points_category'].value_counts().index, autopct='%1.1f%%', startangle=140)
axes[0, 0].set_title('Proporción de Jugadores por Rango de Puntos por Partido')

# Gráfico circular para Asistencias (ya creado)
axes[0, 1].pie(data['asist_category'].value_counts(), labels=data['asist_category'].value_counts().index, autopct='%1.1f%%', startangle=140)
axes[0, 1].set_title('Proporción de Jugadores por Rango de Asistencias por Partido')

# Gráfico circular para Robos
axes[1, 0].pie(data['steals_category'].value_counts(), labels=data['steals_category'].value_counts().index, autopct='%1.1f%%', startangle=140)
axes[1, 0].set_title('Proporción de Jugadores por Rango de Robos por Partido')

# Gráfico circular para Rebotes
axes[1, 1].pie(data['rebounds_category'].value_counts(), labels=data['rebounds_category'].value_counts().index, autopct='%1.1f%%', startangle=140)
axes[1, 1].set_title('Proporción de Jugadores por Rango de Rebotes por Partido')

# Ajustes adicionales para la presentación
plt.tight_layout()
plt.savefig('circulares.png')


# Visualización 7:

legendary_players = ['Michael Jordan', 'LeBron James', 'Kobe Bryant']
legendary_data = data[data['full_name'].isin(legendary_players)]

plt.figure(figsize=(12, 6))
sns.lineplot(x='year', y='pts', hue='full_name', data=legendary_data)
plt.title('Comparación de Puntos por Juego de Jugadores Legendarios')
plt.xlabel('Año')
plt.ylabel('Puntos por Juego')
plt.savefig('comparacion_legendarios.png')


plt.show()
