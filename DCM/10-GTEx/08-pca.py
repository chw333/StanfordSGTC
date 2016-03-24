import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pylab as plt
import seaborn as sns

df = pd.read_table('GTEx_Heart_S635A_TwoCtrl_exp-rlog_SelectedControl.txt', header=0)
dc = list(df.columns)
dc[0]='GeneID'
dc[2] = 'GTEx Atrial Appendage Actual Death 1'
dc[3] = 'GTEx Atrial Appendage Actual Death 2'
dc[4] = 'GTEx Atrial Appendage Actual Death 3'
dc[5] = 'GTEx Left Ventricle Actual Death 1'
dc[6] = 'GTEx Left Ventricle Actual Death 2'
dc[7] = 'GTEx Left Ventricle Actual Death 3'
dc[8] = 'GTEx Atrial Appendage Presumed Death 1'
dc[9] = 'GTEx Atrial Appendage Presumed Death 2'
dc[10] = 'GTEx Atrial Appendage Presumed Death 3'
dc[11] = 'GTEx Left Ventricle Presumed Death 1'
dc[12] = 'GTEx Left Ventricle Presumed Death 2'
dc[13] = 'GTEx Left Ventricle Presumed Death 3'
dc[14] = 'S635A'
dc[15] = 'CP1'
dc[16] = 'CP2'
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
#plt.style.use('seaborn-white')
c1 = sns.color_palette("Set2", 4)[0]
c2 = sns.color_palette("Set2", 4)[1]
c3 = sns.color_palette("Set2", 4)[2]
c4 = sns.color_palette("Set2", 4)[3]


ax = fig.add_subplot(111)
for lab, col in zip(y,(c1, c1, c1, c2, c2, c2, c3, c3, c3, c4, c4, c4,'red', 'green', 'blue')):
    ax.scatter(Y_sklearn[y==lab, 0],Y_sklearn[y==lab, 1],label=lab,c=col, s=80)


ax.set_xlabel('Principal Component 1 : %.2f'%(pca.explained_variance_ratio_[0]*100) + '%')
ax.set_ylabel('Principal Component 2 : %.2f'%(pca.explained_variance_ratio_[1]*100) + '%')
ax.legend(loc='lower right', prop={'size':6})
plt.tight_layout()
plt.savefig('PCA_S635A_TwoCtrl_GTExSelectedCtrl.pdf')
