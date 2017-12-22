# -*- coding: utf-8 -*-
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv(r"meme3.csv",header=0).values[57542:126978,2:5]
span = 1000
row_num =data.shape[0]
over_list = np.hstack([data[i:row_num-span+1+i] for i in range (span)])
print(over_list)
pca = PCA(n_components=5)
pca.fit(over_list)
transformed=pca.fit_transform(over_list)
print(pca.components_)
ev_ratio = pca.explained_variance_ratio_
ev_ratio = np.hstack([0,ev_ratio.cumsum()])
plt.plot(ev_ratio)
plt.show()

plt.scatter(transformed[53000:, 0], transformed[53000:, 1])
plt.scatter(transformed[:53000, 0], transformed[:53000, 1])
plt.title('principal component')
plt.xlabel('pc1')
plt.ylabel('pc2')
plt.show()
