# -*- coding: utf-8 -*-
"""
Task 2: 
    How to insert a translation part in Python (Youdao Dict)?
Created on Mon Jan  2 10:50:57 2017
@author: liuxinyu
"""

import urllib.request
import urllib.parse
import json

content=input('请输入需要翻译的内容：')

url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index'
data={}
data['type']='AUTO'
data['i']=content
data['doctype']='json'
data['xmlVersion']=1.8
data['keyfrom']='fanyi.web'
data['ue']='UTF-8'
data['typoResult']='true'
data=urllib.parse.urlencode(data).encode('utf-8')

response=urllib.request.urlopen(url,data)
html=response.read().decode('utf-8')

target=json.loads(html)
target=target['translateResult'][0][0]['tgt']

print('翻译结果:%s' % (target))


