import os
###strip()函数只去除首尾两端的空白，想去除字符串全部空白使用replace(" ","")
#写一个函数 根据文件名来读取文件内容
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)

def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif '.' in time_string:
        splitter='.'
    else:
        return(time_string)
    (mins,secs)=time_string.split(splitter)
    return(mins+':'+secs)

sarah= get_coach_data('data1.txt')
#print(sarah)
#print(sarah.pop(0))#pop从列表中剔除一个元素并返回这个值   ##del和pop用法一致，但是他不返回任何值
#print(sarah)
(sarah_name,sarah_dob)=sarah.pop(0),sarah.pop(0)
print(sarah_name+"'s fastest time are:"+str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

###使用字典关联数据
sarah=get_coach_data('data1.txt')
sarah_data={}
sarah_data['name']=sarah.pop(0)
sarah_data['dob']=sarah.pop(0)
sarah_data['times']=sarah
print(sarah_data)
print(sarah_data['name']+"'s fastest times are:"+str(sorted(set([sanitize(t) for t in sarah_data[   'times']]))[0:3]))

###改进代码，一次性在函数读取数据中完成字典创建返回一个字典而不再是列表
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
            tmpdata=data.strip().split(',')
            return({
                    'name':tmpdata.pop(0),
                    'dob':tmpdata.pop(0),
                    'times':str(sorted(set([sanitize(t) for t in tmpdata]))[0:3])
                })
    except IOError  as ioerr:
        print('File error:'+str(ioerr))
        return(None)

sarah=get_coach_data('data1.txt')
print(sarah)
print(sarah['name']+"'s fastest times are:"+sarah['times'])





















