#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : correlation_analysis.py
# @Software: PyCharm
"""
餐饮销量数据相关性分析
"""
import pandas as pd

#导入数据
catering_sale='E:\python\sklearn\data_preprocessing\data\catering_sale_all.xls'
#读取数据
data=pd.read_excel(catering_sale,index_col=u'日期')

#相关系数矩阵，即给出任意两款菜式之间的相关系数
print(data.corr())
#只显示“百合酱蒸凤爪“与其他菜式的相关系数
print(data.corr()[u'百合酱蒸凤爪'])
#计算“百合酱蒸凤爪”与“翡翠蒸香茜饺"的相关系数
print(data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺']))