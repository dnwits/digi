#Aquest programa llegeix dades de consum energètic d'una fàbrica a partir d'un fitxer CSV i calcula el consum total 
# per dia i per mes. A més, determina quin dia ha tingut el consum energètic més alt. Això ajuda a monitoritzar 
# l'eficiència energètica d'una fàbrica.

#No fet, la veritat...
import pandas as pd


df = pd.read_csv('consum_energetic.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['dia'] = df['timestamp'].dt.date


consum_diari = df.groupby('dia')['kwh'].sum()
consum_total = consum_diari.sum()


print(f"Consum energètic total del mes: {consum_total} kWh")
print(f"Dia amb més consum: {consum_diari.idxmax()} amb {consum_diari.max()} kWh")
