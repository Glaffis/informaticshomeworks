import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("iris_data.csv")

plt.figure(figsize=(10, 10))

# 1. SepalLength от SepalWidth
plt.subplot(3, 2, 1)
plt.scatter(data["SepalLengthCm"], data["SepalWidthCm"])
plt.xlabel("SepalLengthCm")
plt.ylabel("SepalWidthCm")

# 2. SepalLength от PetalLength
plt.subplot(3, 2, 2)
plt.scatter(data["SepalLengthCm"], data["PetalLengthCm"])
plt.xlabel("SepalLengthCm")
plt.ylabel("PetalLengthCm")

# 3. SepalLength от PetalWidth
plt.subplot(3, 2, 3)
plt.scatter(data["SepalLengthCm"], data["PetalWidthCm"])
plt.xlabel("SepalLengthCm")
plt.ylabel("PetalWidthCm")

# 4. SepalWidth от PetalLength
plt.subplot(3, 2, 4)
plt.scatter(data["SepalWidthCm"], data["PetalLengthCm"])
plt.xlabel("SepalWidthCm")
plt.ylabel("PetalLengthCm")

# 5. SepalWidth от PetalWidth
plt.subplot(3, 2, 5)
plt.scatter(data["SepalWidthCm"], data["PetalWidthCm"])
plt.xlabel("SepalWidthCm")
plt.ylabel("PetalWidthCm")

# 6. PetalLength от PetalWidth + линия тренда
plt.subplot(3, 2, 6)
x = data["PetalLengthCm"]
y = data["PetalWidthCm"]
plt.scatter(x, y)
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")

k, b = np.polyfit(x, y, 1)
y_line = k * x + b
plt.plot(x, y_line, color="red")
plt.text(min(x)+0.1, max(y)-0.2, f"y = {k:.2f}x + {b:.2f}", color="red")

plt.tight_layout()
plt.show()