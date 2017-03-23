#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : ExceptionHandling.py
# @Software: PyCharm
"""
本例用来展示数据的异常值处理
"""
import pandas as pd
#导入数据
catering_sale='E:\python\sklearn\data_preprocessing\data\catering_sale.xls'
#读取数据，制定“日期”列为索引列
data=pd.read_excel(catering_sale,index_col=u'日期')

#导入画图工具
import matplotlib.pyplot as plt
#正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
#正常显示负号
plt.rcParams['axes.unicode_minus']=False

#建立图像
plt.figure()
#画箱形图，直接使用DataFrame的方法
p=data.boxplot(return_type='dict')
#获取异常值标签
x=p['fliers'][0].get_xdata()
y=p['fliers'][0].get_ydata()
#排序
y.sort()


#用annotate加注释
#其中有些相近的点，注解会出现重叠，难以看清，需要一些技巧来控制
#经过调试之后有
for i in range(len(x)):
    if i>0:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] +0.08, y[i]))

plt.legend()
plt.show()