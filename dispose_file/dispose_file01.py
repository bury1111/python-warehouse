import os
###strip()函数只去除首尾两端的空白，想去除字符串全部空白使用replace(" ","")
#写一个函数 根据文件名来读取文件内容
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        return(data.replace(" ","").split(','))
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)

'''
with open('data1.txt') as d1:
    data= d1.readline()
data1=data.strip().split(',')
with open('data2.txt') as d2:
    data= d2.readline()
data2=data.strip().split(',')
with open('data3.txt') as d3:
    data= d3.readline()
data3=data.replace(" ","").split(',')
with open('data4.txt') as d4:
    data= d4.readline()
data4=data.strip().split(',')
'''
#现在调用读取文件函数即可
data1=get_coach_data('data1.txt')
data2=get_coach_data('data2.txt')
data3=get_coach_data('data3.txt')
data4=get_coach_data('data4.txt')

print('\n ---------------------读取原始数据')
print(sorted(data1))
print(sorted(data2))
print(sorted(data3))
print(sorted(data4))

#格式化数据使其统一 再进行排序
def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif '.' in time_string:
        splitter='.'
    else:
        return(time_string)
    (mins,secs)=time_string.split(splitter)
    return(mins+':'+secs)

#去除列表重复数据（迭代）
def distinct(list_data):
    distinct_data=[]
    for each_t in list_data:
        if each_t not in distinct_data:
            distinct_data.append(each_t)
    return distinct_data

print('\n ---------------------格式化数据后进行排序')
#完整写法
new_data1=[]
new_data2=[]
new_data3=[]
new_data4=[]

for each_t in data1:
    new_data1.append(sanitize(each_t))
for each_t in data2:
    new_data2.append(sanitize(each_t))
for each_t in data3:
    new_data3.append(sanitize(each_t))
for each_t in data4:
    new_data4.append(sanitize(each_t))
print(sorted(new_data1,reverse=True))#reverse=True 降序处理 默认升序为True
print(sorted(new_data2))
print(sorted(new_data3))
print(sorted(new_data4))
print('\n ---------------------格式化数据后进行排序(推导列表输出)')
#推导列表（减少代码量）
print(sorted([sanitize(t) for t in data1]))#列表[0:3]使用一个列表分片访问列表中从第0项到（但不包括）第3项的数据项
print(sorted([sanitize(t) for t in data2]))
print(sorted([sanitize(t) for t in data3]))
print(sorted([sanitize(t) for t in data4]))

print('\n ---------------------去重之后的数据(并只输出前三项)【reverse=True倒序排列的】')
#输出去重之后的数据
print(distinct(sorted([sanitize(t) for t in data1],reverse=True))[0:3])
print(distinct(sorted([sanitize(t) for t in data2],reverse=True))[0:3])
print(distinct(sorted([sanitize(t) for t in data3]))[0:3])
print(distinct(sorted([sanitize(t) for t in data4]))[0:3])

#若不想写函数来去重的话可以不使用列表 使用集合 集合的特性是无序的且不允许重复
#创建一个空集合 distances = set() 将数据放入集合中即可
print('\n ---------------------将数据放入集合中达到删除重复项的目的')
data_new=sorted(set([sanitize(t) for t in data1]),reverse=True)[0:3]
print(data_new)

print('\n ---------------------列表和集合的区别')
print(['d-a-t-a l-o-s-s'])
print(set('d-a-t-a l-o-s-s'))
                     
