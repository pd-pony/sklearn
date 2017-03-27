#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : pca.py
# @Software: PyCharm
"""
本例是使用PCA进行降维的示例
"""
import pandas as pd

#参数初始化
inputfile='C:/Users/dong.pei/Desktop/Python practice of data analysis and data mining/chapter4/chapter4/demo/data/principal_component.xls'
outputfile='C:/Users/dong.pei/Desktop/Python practice of data analysis and data mining/chapter4/chapter4/demo/data/result.xls'

#读取数据
data=pd.read_excel(inputfile,header=None)

from sklearn.decomposition import PCA
pca=PCA()
pca.fit(data)
#返回模型的各个特征向量
print(pca.components_)
#返回各个成分各自的方差百分比
print(pca.explained_variance_ratio_)

#当选取前4个主成分时，累计贡献率已经到达97.37%，因此选取前3个主成分进行计算就已经相当不错了，
pca=PCA(3)
pca.fit(data)
#降维
low_d=pca.transform(data)
#保存结果到输出文件中
pd.DataFrame(low_d).to_excel(outputfile)
#必要时可以恢复元数据
pca.inverse_transform(low_d)