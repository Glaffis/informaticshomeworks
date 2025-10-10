import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

d = pd.read_csv("BTC_data.csv")
d["time"] = pd.to_datetime(d["time"])

plt.figure(figsize=(10, 5))
plt.plot(d["time"], d["close"])


ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))     
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))  

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()