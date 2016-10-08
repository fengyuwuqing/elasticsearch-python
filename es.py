#!/usr/bin/env python
# coding=utf-8
"""
@author:'guoji'
@Email:guojie@xinfushe.com
@company:北京用友薪福社云科技有限公司
@createtime:2016/10/8--13:59
"""
import os

from elasticsearch import Elasticsearch

es = Elasticsearch('http://127.0.0.1:9200')
total = 50000
# os.system("""curl -X PUT http://127.0.0.1:9200/es/_settings -d ‘{ "index" : { "max_result_window" : 100000000}}'""")
ret = es.search(index="es",size=10,from_ = 60000)
for hit in ret['hits']['hits']:
    print hit["_source"]