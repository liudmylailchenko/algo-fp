import random
import matplotlib.pyplot as plt
import numpy as np

num_simulations = 1_000_000

sum_counts = {i: 0 for i in range(2, 13)}

for _ in range(num_simulations):
    dice_sum = random.randint(1, 6) + random.randint(1, 6)
    sum_counts[dice_sum] += 1

simulated_probabilities = {
    key: (value / num_simulations) * 100 for key, value in sum_counts.items()
}

analytical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}

sums = list(simulated_probabilities.keys())
simulated_vals = list(simulated_probabilities.values())
analytical_vals = [analytical_probabilities[i] for i in sums]

x = np.arange(len(sums))
width = 0.4

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, simulated_vals, width, label="Simulated")
rects2 = ax.bar(x + width / 2, analytical_vals, width, label="Analytical")

ax.set_xlabel("Sum")
ax.set_ylabel("Probability (%)")
ax.set_title("Dice Roll Simulation")
ax.set_xticks(x)
ax.set_xticklabels(sums)
ax.legend()

plt.show()
