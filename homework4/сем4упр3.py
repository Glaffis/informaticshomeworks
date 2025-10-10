import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("iris_data.csv")

species_counts = data["Species"].value_counts()

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%')
plt.title("Доли разных видов")

more_12 = len(data[data["PetalLengthCm"] > 1.2])
between_12_15 = len(data[(data["PetalLengthCm"] > 1.2) & (data["PetalLengthCm"] < 1.5)])
more_15 = len(data[data["PetalLengthCm"] > 1.5])

petal_groups = [more_12, between_12_15, more_15]
labels = ["> 1.2 см", "1.2–1.5 см", "> 1.5 см"]

plt.subplot(1, 2, 2)
plt.pie(petal_groups, labels=labels, autopct='%1.1f%%')
plt.title("Длины лепестков")

plt.tight_layout()
plt.show()
