import numpy as np
import random
import matplotlib.pyplot as plt
import cv2


def distance(a, b):
    # Euclidean distance
    return np.sum((a - b) ** 2, axis=1) ** 0.5


def Kmeans(k, X):
    # init random k as the init centroid
    idx = random.sample(list(range(len(X))), k)
    clusters = X[idx]   # (k, 2)
    
    # ith sample label, set the init cluster as 0 class
    labels = np.zeros((len(X),))
    
    while True:
        cnt = 0
        for i, d in enumerate(X):
            _distance = distance(d, clusters)
            min_idx = np.argmin(_distance)
            if labels[i] != min_idx:
                cnt += 1
                labels[i] = min_idx
        if cnt == 0:
            break
        
        for label in range(k):
            # update centroid
            centroid = np.mean(X[labels == label], axis=0)
            clusters[label] = centroid
    return labels


if __name__ == "__main__":

    X = np.vstack((
        np.random.randn(5, 2) - 5,
        np.random.randn(10, 2) + 5,
    ))
    
    labels = Kmeans(2, X)
    
    # visualization
    plt.scatter(X[:, 0], X[:, 1], c=labels)
    plt.show()
    