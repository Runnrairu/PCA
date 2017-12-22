import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv(r"meme1.csv",header=0).values[:,2:7]
span = 5
row_num =data.shape[0]
over_list = np.hstack([data[i:row_num-span+1+i] for i in range (span)])
pca = PCA(n_components=10)
pca.fit(over_list)
print(pca.components_)
ev_ratio = pca.explained_variance_ratio_
ev_ratio = np.hstack([0,ev_ratio.cumsum()])
plt.plot(ev_ratio)
plt.show()

