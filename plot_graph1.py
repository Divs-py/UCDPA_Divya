import matplotlib.pyplot as plt
import numpy as np

likes = np.array([655.7, 372, 441.5, 557.9, 405.2])
myLabels = ["A (07.11.2022)", "B (09.11.2022)", "C (11.11.2022)", "D (13.11.2022)","E (15.11.2022)"]

plt.pie(likes, labels = myLabels)
plt.title("Likes on Selected Tweets")
plt.show() 
