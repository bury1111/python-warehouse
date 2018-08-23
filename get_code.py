#爬取网页代码
import os
import urllib.request
import pickle  #使用pickle模块

url = 'http://www.baidu.com'
res = urllib.request.urlopen(url)
html = res.read().decode('utf-8')
#print(html)



#使用pickle的dump来保存数据至本地以二进制的形式
try:
    with open('code.pickle','wb') as mysavedata:  #wb w写入 b以二进制的形式
        pickle.dump(html,mysavedata)
except IOError as err:
    print(str(err))


#使用pickle的load来加载保存的数据
try:
    mydata=[]
    with open('code.pickle','rb') as my_data:
        mydata=pickle.load(my_data)
except IOError as err:
    print(str(err))
except pickle.PickleError as perr:
    print(str(perr))

print(mydata)
'''
#写入本地文本中
try:
    with open('get_code/code.txt','w',errors='ignore') as html_txt:
        print(html,file=html_txt)
        print("成功写入！")
except IOError as err:
    print('File error:'+str(err))
'''
