import matplotlib.pyplot as plt

# Replace these values with comparison counts collected from Q1.
# Example data for successful searches on sorted arrays.
n = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

binary = [6, 8, 10, 12, 14, 16, 18, 20, 24, 26]
ternary = [7, 9, 12, 14, 16, 19, 21, 23, 26, 29]

plt.figure(figsize=(9, 5.5))
plt.plot(n, binary, marker="o", label="Binary Search")
plt.plot(n, ternary, marker="s", label="Ternary Search")

plt.xlabel("Number of elements (n)")
plt.ylabel("Number of comparisons")
plt.title("Binary Search vs Ternary Search")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig("binary_vs_ternary_search.png", dpi=200)
plt.show()
