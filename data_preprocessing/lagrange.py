#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : lagrange.py
# @Software: PyCharm
"""
拉格朗日插值法
"""
from scipy.interpolate import  lagrange
import pandas as pd

#销量数据路径
inputfile="C:/Users/dong.pei/Desktop/Python practice of data analysis and data mining/chapter4/chapter4/demo/data/catering_sale.xls"
#输出数据路径
outputfile="C:/Users/dong.pei/Desktop/Python practice of data analysis and data mining/chapter4/chapter4/demo/data/sales.xls"

#读取数据
data=pd.read_excel(inputfile)
#过滤异常值
data[u'销量'][(data[u'销量']<400)|(data[u'销量']>50000)]=None

#自定义列向量插值函数
#s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
def polyinterp_column(s,n,k=5):
    y = s[list(range(n-k,n))+list(range(n+1,n+1+k))]
    #删除控制
    y=y[y.notnull()]
    #插值并返回插值结果
    return lagrange(y.index,list(y))(n)

#逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        #如果为空即插值
        if(data[i].isnull())[j]:
            data[i][j]=polyinterp_column(data[i],j)

#输出结果，写入文件
data.to_excel(outputfile)
