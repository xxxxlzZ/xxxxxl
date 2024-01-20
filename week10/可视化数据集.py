import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc', size=14)
# 读取数据
data = pd.read_csv('./波士顿房价数据集.csv')

data.hist(bins=15)
plt.show()
sns.boxplot(data=data[['INDUS', 'RM', 'RAD', 'LSTAT']])
plt.show()
sns.pairplot(data)
plt.show()