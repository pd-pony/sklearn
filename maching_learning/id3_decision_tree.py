#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : id3_decision_tree.py
# @Software: PyCharm
"""
使用ID3决策树算法预测销量高低
"""
import pandas as pd

#导入文件
filename='E:/chapter5/demo/data/sales_data.xls'
#读取数据
data=pd.read_excel(filename,index_col=u'序号')

#数据是类别数据，需要将其转换为数值数据
#用1表示“好”，“是”，“高”这三个属性，用-1表示“坏”，“否”，“低”
data[data==u'好']=1
data[data==u'是']=1
data[data==u'高']=1
data[data!=1]=-1
#转换为矩阵类型
x=data.iloc[:,:3].as_matrix().astype(int)
y=data.iloc[:,3].as_matrix().astype(int)

from sklearn.tree import DecisionTreeClassifier as DTC
#建立模型，基于信息熵
dtc=DTC(criterion='entropy')
#训练模型
dtc.fit(x,y)

#导入相关函数，可视化决策树
#到处的结果是一个dot文件，需要安装Graphviz才能将它转换为pdf或png格式
from sklearn.tree import export_graphviz
x=pd.DataFrame(x)
from sklearn.externals.six import StringIO
with open("tree.dot",'w') as f:
    f=export_graphviz(dtc,feature_names=x.columns,out_file=f)
