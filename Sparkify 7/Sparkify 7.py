#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import json
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("Sparkify-7").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    log = sc.textFile("s3a://snell2-spark/input")
    dat=log.collect()

for dic in dat:
    data=json.loads(dic)

#mapper code
s_lst=[]
a_lst=[]
for dic in dat:
    data=json.loads(dic)
    s=data['song']
    s_lst.append([s,1])

def reducer(lst):
    dict={}
    list=[]
    for l in lst:
        if l[0] not in dict:
            dict[l[0]]=1
        else: dict[l[0]]+=1
    for key,values in dict.items():
        if key == None:
            continue
        else:
            list.append([key,values])
    list = sorted (list, key=lambda x:x[1],reverse=True)
    return list

song=[]
song=reducer(s_lst)

sc.parallelize(song).saveAsTextFile("s3a://snell2-spark/output/s7")

