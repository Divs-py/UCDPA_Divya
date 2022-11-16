import matplotlib.pyplot as plt
import numpy as np

likes = np.array([87.7, 107.8, 34.8, 51.3, 27.9])
myLabels = ["A (07.11.2022)", "B (09.11.2022)", "C (11.11.2022)", "D (13.11.2022)","E (15.11.2022)"]

plt.pie(likes, labels = myLabels)
plt.title("User Interactions on Selected Tweets")
plt.show() 
