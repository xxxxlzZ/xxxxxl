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
# sns.pairplot(data)
# 标准化处理
data['CRIM'] = (data['CRIM'] - np.mean(data['CRIM'])) / np.std(data['CRIM'])
data['ZN'] = (data['ZN'] - np.mean(data['ZN'])) / np.std(data['ZN'])
data['INDUS'] = (data['INDUS'] - np.mean(data['INDUS'])) / np.std(data['INDUS'])
data['CHAS'] = (data['CHAS'] - np.mean(data['CHAS'])) / np.std(data['CHAS'])
data['NOX'] = (data['NOX'] - np.mean(data['NOX'])) / np.std(data['NOX'])
data['RM'] = (data['RM'] - np.mean(data['RM'])) / np.std(data['RM'])
data['AGE'] = (data['AGE'] - np.mean(data['AGE'])) / np.std(data['AGE'])
data['DIS'] = (data['DIS'] - np.mean(data['DIS'])) / np.std(data['DIS'])
data['RAD'] = (data['RAD'] - np.mean(data['RAD'])) / np.std(data['RAD'])
data['TAX'] = (data['TAX'] - np.mean(data['TAX'])) / np.std(data['TAX'])
data['PTRATIO'] = (data['PTRATIO'] - np.mean(data['PTRATIO'])) / np.std(data['PTRATIO'])
data['B'] = (data['B'] - np.mean(data['B'])) / np.std(data['B'])
data['LSTAT'] = (data['LSTAT'] - np.mean(data['LSTAT'])) / np.std(data['LSTAT'])
data['target'] = (data['target'] - np.mean(data['target'])) / np.std(data['target'])

# 计算相关系数
corr = data.corr()
corr = corr[['target']]
corr = corr.drop('target')

# 取绝对值排序
corr = corr.apply(lambda x: abs(x))
corr = corr.sort_values('target', ascending=False)

# 输出结果
print('采用的特征提取法：相关系数法\n')
print('房价最相关的几个特征:\n', corr.head())

# 绘制特征关系图
sns.heatmap(data.corr(), cmap='coolwarm', annot=True, fmt='.2f', xticklabels=1, yticklabels=1, linewidths=0.5)
plt.xticks(rotation=90, fontsize=12)
plt.yticks(rotation=0, fontsize=12)
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.show()


def load_data():
    # 将数据集导入
    datafile = './波士顿房价数据集.csv'

    data = pd.read_csv(datafile)
    data = data.to_numpy()

    feature_num = 14

    maximums, minimums, avgs = \
        data.max(axis=0), \
            data.min(axis=0), \
            data.sum(axis=0) / data.shape[0]
    # 数据集的划分
    ratio = 0.8
    offset = int(data.shape[0] * ratio)
    training_data = data[:offset]
    test_data = data[offset:]
    # 对数据进行归一化处理（最值归一化）
    for i in range(feature_num):
        training_data[:, i] = (training_data[:, i] - avgs[i]) / (maximums[i] - minimums[i])
    for i in range(feature_num):
        test_data[:, i] = (test_data[:, i] - avgs[i]) / (maximums[i] - minimums[i])
    return training_data, test_data


# 定义神经网络
class Network(object):
    def __init__(self, num_of_weights):  # 初始化权重值
        # 随机产生w的初始值，为了保持程序每次运行结果的一致性，设置固定的随机数种子
        np.random.seed(0)
        self.w = np.random.randn(num_of_weights, 1)  # 初始参数一般符合标准正态分布
        self.b = 0.

    def forward(self, x):
        z = np.dot(x, self.w) + self.b
        return z

    def loss(self, z, y):
        error = z - y
        cost = error * error
        cost = np.mean(cost)
        return cost

    def gradient(self, x, y, z):
        gradient_w = (z - y) * x
        gradient_w = np.mean(gradient_w, axis=0)
        gradient_w = gradient_w[:, np.newaxis]
        gradient_b = (z - y)
        gradient_b = np.mean(gradient_b)
        return gradient_w, gradient_b

    def update(self, gradient_w, gradient_b, eta=0.01):
        self.w = self.w - eta * gradient_w
        self.b = self.b - eta * gradient_b

    def train(self, training_data, epoch_num=100, batch_size=10, eta=0.01):
        n = len(training_data)
        losses = []
        for epoch in range(epoch_num):
            # 打乱数据集并分批
            np.random.shuffle(training_data)
            for k in range(0, n, batch_size):
                mini_batches = [training_data[k:k + batch_size]]
                for iter_id, mini_batch in enumerate(mini_batches):
                    x = mini_batch[:, :-1]
                    y = mini_batch[:, -1:]
                    z = self.forward(x)
                    L = self.loss(z, y)
                    gradient_w, gradient_b = self.gradient(x, y, z)
                    self.update(gradient_w, gradient_b, eta)
                    losses.append(L)
        return losses


training_data, test_data = load_data()
x = training_data[:, :-1]
y = training_data[:, -1:]
# 创建网络
net = Network(13)
# 启动训练
losses = net.train(training_data, epoch_num=200, batch_size=30, eta=0.1)
# 画出损失函数的变化趋势
plot_x = np.arange(len(losses))
plot_y = np.array(losses)
plt.plot(plot_x, plot_y)
plt.xlabel('Iteration order')
plt.ylabel('loss')
plt.show
# 可视化测试的结果

training_data, test_data = load_data()
x = test_data[:, :-1]
y = test_data[:, -1:]
y_predict = net.forward(x)
plot_x = np.arange(len(y_predict))
plot_y = np.array(y_predict)
fig1 = plt.figure()
plt.plot(plot_x, plot_y)
plot_y1 = np.array(y)
plt.plot(plot_x, plot_y1)
plt.legend(['predict', 'true'], loc='upper left')
plt.ylim([-0.7, 0.5])
# plt.show()
fig2 = plt.figure()
plot_y2 = np.array(y - y_predict)
plt.plot(plot_x, plot_y2)
plt.ylabel('predict error')
plt.show()