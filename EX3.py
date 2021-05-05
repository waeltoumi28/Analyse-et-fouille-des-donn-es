import pandas as pd
fromage = pd.read_table("fromage.txt" ,sep="\t",header=0,index_col=0)
print(fromage.shape)
print(fromage.describe())
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
fromage_cr=sc.fit_transform(fromage)
from scipy.cluster.hierarchy import dendrogram , linkage
import matplotlib.pyplot as plt
Z= linkage(fromage_cr,method='ward',metric='euclidean')
plt.title('C-A-H')
dendrogram(Z,labels=fromage.index,orientation='left' , color_threshold=0)
plt.show()
