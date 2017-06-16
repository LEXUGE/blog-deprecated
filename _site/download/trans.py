#!/usr/bin/env python  
# -- coding: UTF-8 -- 
import codecs
import re  
import urllib2  
import re  
import json  
import sys
from urllib import quote

reload(sys)
sys.setdefaultencoding( "utf-8" )

class Youdao:  
    def __init__(self):  
        self.url = 'http://fanyi.youdao.com/openapi.do'  
        self.key = '54293807'   
        self.keyfrom = 'LEXUGE-trans'  
  
    def get_translation(self,words):  
        url = self.url + '?keyfrom=' + self.keyfrom + '&key='+self.key + '&type=data&doctype=json&version=1.1&q=' + quote(str(words))  
        result = urllib2.urlopen(url).read()   
        json_result = json.loads(result)  
        try : 
            json_result2 = json_result["basic"]
           
        except :
            pass    
        try :
            json_result3 = json_result2["uk-phonetic"]
       
        except :
            pass 
        try :
            json_result = json_result["translation"]
      
        except :
            pass
        for i in json_result:  
            print u'翻译:'+i  
        try :
            print u'英式发音:'+json_result3
        except :
            pass
        try : 
            print u'解释:'+json_result2["explains"][0]  
        except :
            pass
    
  
youdao = Youdao()  
while True:
    print '\n'
    try:
        msg=raw_input(u'输入你要翻译的单词,输入lexuge退出:').decode('utf-8')
    except:
        pass
    if msg == 'lexuge':  
        break  
    youdao.get_translation(msg)  
