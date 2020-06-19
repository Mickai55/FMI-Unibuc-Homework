import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix
import numpy as np

mat = [[380, 92],
        [115, 413]]

fig, ax = plt.subplots()

plt.imshow(mat)

# We want to show all ticks...
ax.set_xticks(np.arange(2))
ax.set_yticks(np.arange(2))
# ... and label them with the respective list entries
ax.set_xticklabels([0, 1])
ax.set_yticklabels([0, 1])

plt.xlabel("Predicted label", color="black")
plt.ylabel("True label", color="black")

# Loop over data dimensions and create text annotations.
for i in [0, 1]:
    for j in [0, 1]:
        text = ax.text(j, i, mat[i][j], ha="center", va="center", color="w")

ax.set_title("Confusion Matrix")

plt.colorbar(cmap='gray')
plt.show()