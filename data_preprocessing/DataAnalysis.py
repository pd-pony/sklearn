#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : DataAnalysis.py
# @Software: PyCharm
"""
餐饮销量数据统计量分析
"""
import pandas as pd

#导入数据
catering_sale='E:\python\sklearn\data_preprocessing\data\catering_sale.xls'
#读取数据
data=pd.read_excel(catering_sale,index_col=u'日期')
#过滤异常数据
data=data[(data[u'销量'])>400&(data[u'销量']<5000)]
#保存基本统计量
statistics=data.describe()

#极差
statistics.loc['range']=statistics.loc['max']-statistics.loc['min']
#变异系数
statistics.loc['var']=statistics.loc['std']/statistics.loc['mean']
#四分位数间距
statistics.loc['dis']=statistics.loc['75%']-statistics.loc['25%']

print(statistics)