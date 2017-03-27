#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : k-means.py
# @Software: PyCharm
"""
使用k-means算法聚类消费行为特征数据
"""
import pandas as pd

#读取数据
filename='E:/chapter5/demo/data/consumption_data.xls'
data=pd.read_excel(filename,index_col='Id')
#保存输出数据
outputfile='E:/chapter5/demo/data/consumption_result_data.xls'

#聚类模型参数选择
k=3
#聚类最大循环次数
iteration=500
#数据表转化
data_zs=1.0*(data-data.mean())/data.std()

from sklearn.cluster import KMeans
#构建模型，分为k类，并发数为4
model=KMeans(n_clusters=k,n_jobs=4,max_iter=iteration)
#开始聚类
model.fit(data_zs)

#简单打印结果
#统计各个类别的数目
r1=pd.Series(model.labels_).values_counts()
#标出聚类中心
r2=pd.DataFrame(model.cluster_centers_)
r=pd.concat([r2,r1],axis=1)
#重命名表头
r.columns=list(data.columns)+[u'类别数目']
print(r)

#详细输出原始数据及其类别
#详细输出每个样本对应的类别
r=pd.concat([data,pd.Series(model.labels_,index=data.index)],axis=1)
#重命名表头
r.columns=list(data.columns)+[u'聚类类别']
#输出保存结果
r.to_excel(outputfile)