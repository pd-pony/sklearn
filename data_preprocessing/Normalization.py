#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : Normalization.py
# @Software: PyCharm
#正则化（Normalization）
"""
正则化的过程是将每个样本缩放到单位范数（每个样本的范数为1），如果后面要使用如二次型（点积）或者
其它核方法计算两个样本之间的相似性这个方法会很有用。
Normalization主要思想是对每个样本计算其p-范数，然后对该样本中每个元素除以该范数，这样处理的结果
是使得每个处理后样本的p-范数（l1-norm,l2-norm）等于1。
             p-范数的计算公式：||X||p=(|x1|^p+|x2|^p+...+|xn|^p)^1/p
该方法主要应用于文本分类和聚类中。例如，对于两个TF-IDF向量的l2-norm进行点积，就可以得到这两个向
量的余弦相似性。
"""
from sklearn import preprocessing
import numpy as np
#可以使用preprocessing.normalize()函数对指定数据进行转换：
X_train=np.array([[1.,-1.,2],[2.,0.,0.],[0.,1.,-1.]])
X_normalized=preprocessing.normalize(X,norm='12')
print(X_normalized)

#可以使用processing.Normalizer()类实现对训练集和测试集的拟合和转换：
normalizer=preprocessing.Normalizer().fit(X)
print(normalizer)
normalizer.transform(X)
print(normalizer.transform([[-1.,1.,0.]]))