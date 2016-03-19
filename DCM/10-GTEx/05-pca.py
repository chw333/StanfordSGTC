import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pylab as plt

df = pd.read_table('GTEx_Heart_S635A_TwoCtrl_exp-rlog_tail6.txt', header=0)
dc = list(df.columns)
dc[0]='GeneID'
dc[2] = 'GTEx Heart Left Ventricle 1'
dc[3] = 'GTEx Heart Left Ventricle 2'
dc[4] = 'GTEx Heart Left Ventricle 3'
df.columns = dc

X = df.ix[:,2:df.shape[1]].values.T
y = df.columns[2:df.shape[1]].values
X_std = StandardScaler().fit_transform(X)

#pca = PCA(n_components=2)
pca = PCA()
Y_sklearn = pca.fit_transform(X_std)


fig = plt.figure()
plt.style.use('ggplot')
#plt.style.use('seaborn-whitegrid')
ax = fig.add_subplot(111)
for lab, col in zip(y,('c','c','c','red', 'green', 'blue')):
    ax.scatter(Y_sklearn[y==lab, 0],Y_sklearn[y==lab, 1],label=lab,c=col, s=80)


ax.set_xlabel('Principal Component 1 : %.2f'%(pca.explained_variance_ratio_[0]*100) + '%')
ax.set_ylabel('Principal Component 2 : %.2f'%(pca.explained_variance_ratio_[1]*100) + '%')
ax.legend(loc='lower center')
plt.tight_layout()
plt.savefig('PCA_S635A_TwoCtrl_Tail6.pdf')
