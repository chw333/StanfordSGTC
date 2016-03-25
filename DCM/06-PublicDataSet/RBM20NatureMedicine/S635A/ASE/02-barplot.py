import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

CP1_S = 81434777
CP2_S = 84150701
S635A_S = 70504289

cp1_s635a = float(CP1_S)/S635A_S
cp2_s635a = float(CP2_S)/S635A_S

df = pd.read_table('ASE.num',  header=0)
### normlization
df.ix['CP1'][0]=int(df.ix['CP1'][0]/cp1_s635a)
df.ix['CP2'][0]=int(df.ix['CP2'][0]/cp2_s635a)

fig = plt.figure()
ax = fig.add_subplot(111)
df.plot(kind='bar', stacked=True, rot=1, ax = ax)
ax.set_ylabel('Number of reads covering the mutation (Normalized)')
ax.set_title('RBM20')
plt.savefig('ASE.pdf')

