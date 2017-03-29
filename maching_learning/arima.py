#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : arima.py
# @Software: PyCharm
"""
arima时序模型
"""
import pandas as pd

#参数初始化
discfile = 'E:/chapter5/demo/data/arima_data.xls'
forecastum = 5

#读取数据，制定日期列为指标，pandas自动将“日期”列识别为Datatime格式
data=pd.read_excel(discfile,index_col=u'日期')

#时序图
import matplotlib.pyplot as plt
#正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
#正常显示负号
plt.rcParams['axes.unicode_minus']=False
#画图
data.plot()
plt.show()

#自相关图
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(data).show()

#平稳性检查
from statsmodels.tsa.stattools import adfuller as ADF
print(u'原始序列的ADF检验结果为：',ADF(data[u'销量']))
#返回值一次为adf、pvalue、usedlag、nobs、critical values、icbest、regresults、resstore

#差分后的结果
D_data = data.diff().dropna()
D_data.columns = [u'销量差分']
#时序图
D_data.plot()
plt.show()
#自相关图
plot_acf(D_data).show()

from statsmodels.graphics.tsaplots import plot_pacf
#偏自相关图
plot_pacf(D_data).show()
#平稳性检测
print(u'差分序列的ADF检验结果为：',ADF(D_data[u'销量差分']))

#白噪声检验
from statsmodels.stats.diagnostic import acorr_ljungbox
#返回统计量和p值
print(u'差分序列的白噪声检验结果为：',acorr_ljungbox(D_data,lags=1))


from statsmodels.tsa.arima_model import ARIMA
data[u'销量'] = data[u'销量'].astype(float)
#定阶
#一般结束不超过length/10
pmax = int(len(D_data)/10)
qmax = int(len(D_data)/10)
#bic矩阵
bic_matrix = []
for p in range(pmax+1):
    tmp=[]
    for q in range(qmax+1):
        #存在部分报错，所以用try来跳过报错
        try:
            tmp.append(ARIMA(data,(p,1,q)).fit().bic)
        except:
            tmp.append(None)
    bic_matrix.append(tmp)

#从中可以找出最小值
bic_matrix = pd.DataFrame(bic_matrix)
#先用stack展平，然后用idxmin()找出最小值位置
p,q = bic_matrix.stack().idxmin()
print(u'BIC最小的p值和q值为：%s、%s'%(p,q))
#建立ARIMA(0,1,1)模型
model=ARIMA(data,(p,1,q)).fit()
#给出一份模型报告
model.summary2()
#作为期5天的预测，返回预测结果、标准误差、置信区间
model.forecast(5)