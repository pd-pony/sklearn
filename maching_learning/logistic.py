#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : logistic.py
# @Software: PyCharm
"""
逻辑回归，自动建模
"""
import pandas as pd

#参数初始化
filename='E:/chapter5/demo/data/bankloan.xls'
data=pd.read_excel(filename)
x=data.iloc[:,:8].as_matrix()
y=data.iloc[:,8].as_matrix()

from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
#建立随机逻辑回归模型，筛选变量
rlr=RLR()
#训练模型
rlr.fit(x,y)
#获取特征筛选结果，也可以通过.scores_方法获取各个特征的分类
rlr.get_support()
print(u'通过随机逻辑回归模型筛选特征结果')
print(u'有效特征为：%s' % ','.join(data.columns[rlr.get_support()]))
#筛选好特征
x=data[data.columns[rlr.get_support()]].as_matrix()

#建立逻辑货柜模型
lr=LR()
#用筛选后的特征数据来训练模型
lr.fit(x,y)
print(u'逻辑回归模型训练结束')
#给出模型的平均正确率
print(u'模型的平均正确率为：%s' % lr.score(x,y))
