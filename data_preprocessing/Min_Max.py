#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : Min_Max.py
# @Software: PyCharm
"""
除了上述介绍的方法之外，另一种常用的方法是将属性缩放到一个指定的最大和最小值
（通常是1-0）之间，这可以通过preprocessing.MinMaxScaler类实现。使用这种方法的
目的包括：
1、对于方差非常小的属性可以增强其稳定性。
2、维持稀疏矩阵中为0的条目。
"""
from sklearn import preprocessing
import numpy as np
X_train=np.array([[1.,-1.,2],[2.,0.,0.],[0.,1.,-1.]])
min_max_scaler=preprocessing.MinMaxScaler()
X_train_minmax=min_max_scaler.fit_transform(X_train)
print(X_train_minmax)

#将相同的缩放应用到测试集数据中
X_test=np.array([[-3.,-1.,4]])
X_test_minmax=min_max_scaler.transform(X_test)
print(X_test_minmax)

#缩放因子等属性
print(min_max_scaler.scale_)
print(min_max_scaler.min_)