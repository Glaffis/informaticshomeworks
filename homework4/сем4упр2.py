size = [10, 100, 1000, 10000]

plt.figure(figsize=(8, 6))

for i in range(len(size)):
    x = np.random.normal(0, 1, size[i])
    plt.subplot(2, 2, i+1)
    plt.hist(x, bins=20)
    plt.title("n = " + str(size[i]))

plt.tight_layout()
plt.show()