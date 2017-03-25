#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : ParetoChart.py
# @Software: PyCharm
"""
菜品盈利数据 帕累托图
"""
import pandas as pd

#初始化参数
dish_profit='E:\python\sklearn\data_preprocessing\data\catering_dish_profit.xls'
data=pd.read_excel(dish_profit,index_col=u'菜品名')
data=data[u'盈利'].copy()
data.sort(ascending = False)

#导入图像库
import matplotlib.pyplot as plt
#正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
#正常显示负号
plt.rcParams['axes.unicode_minus']=False

# plt.figure()
# data.plot(kind='bar')
# plt.ylabel(u'盈利（元）')
# p = 1.0*data.cumsum()/data.sum()
# p.plot(color = 'r', secondary_y = True, style = '-o',linewidth = 2)
# plt.annotate(format(p[6], '.4%'), xy = (6, p[6]), xytext=(6*0.9, p[6]*0.9), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")) #添加注释，即85%处的标记。这里包括了指定箭头样式。
# plt.ylabel(u'盈利（比例）')
# plt.show()

plt.figure()
data.plot(kind='bar')
plt.ylabel(u'盈利（元）')
p=1.0*data.cumsum()/data.sum()
p.plot(color='r',secondary_y=True,style='-o',linewidth=2)
#添加注释，即85%处的注释
# plt.annotate(format(p[6], '.4%'), xy = (6, p[6]), xytext=(6*0.9, p[6]*0.9), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(format(p[6],'.4%'),xy=(6,p[6]),xytext=(6*0.9,p[6]*0.9),arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))

plt.ylabel(u'盈利（比例）')
plt.show()