import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pylab as plt

df = pd.read_csv(
    filepath_or_buffer='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
    header=None,
    sep=',')

df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
X = df.ix[:,0:4].values
y = df.ix[:,4].values
X_std = StandardScaler().fit_transform(X)

#pca = PCA(n_components=2)
pca = PCA()
Y_sklearn = pca.fit_transform(X_std)


fig = plt.figure()
plt.style.use('ggplot')
#plt.style.use('seaborn-whitegrid')
ax = fig.add_subplot(111)
for lab, col in zip(('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'),('blue', 'red', 'green')):
    ax.scatter(Y_sklearn[y==lab, 0],Y_sklearn[y==lab, 1],label=lab,c=col, s=40)

ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.legend(loc='lower center')
plt.tight_layout()
plt.savefig('test.pdf')
