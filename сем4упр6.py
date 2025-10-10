import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

d = pd.read_csv("BTC_data.csv")
d["time"] = pd.to_datetime(d["time"])

x = np.arange(len(d))
y = d["close"].values

deg = 20

z = np.polyfit(x, y, deg)
p = np.poly1d(z)

plt.figure(figsize=(10,5))
plt.plot(d["time"], y, label="реальная цена")
plt.plot(d["time"], p(x), color="red", label=f"полином {deg}-й степени")
plt.xticks(rotation=45)
plt.legend()
plt.show()
print(p)