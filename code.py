# -*- coding:utf-8 -*-
import numpy as np
from sklearn.decomposition import PCA
raw_input=np.loadtxt(r"C:\Users\JDB2015F-KM\Desktop\データ\memeサンプル.csv",delimiter=",",skiprows=1,dtype=str)
raw_input=np.delete(raw_input,1,1)
raw_input=np.delete(raw_input,0,1)
for i in range(raw_input.shape[0]):
    for j in range(raw_input.shape[1]):
        raw_input[i][j]=float(raw_input[i][j])
for i in range(int(raw_input.shape[0]/5)):
    for j in range(5):
        
moob=moob.T

pca = PCA(n_components=2)
pca.fit(moob)
print ("means")
print (pca.n_components_)
print("Proportion of Variance")
print(pca.explained_variance_ratio_)
print("Cumulative Proportion")
print(np.cumsum(pca.explained_variance_ratio_))
