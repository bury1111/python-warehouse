man = []
other = []
import os
#os.chdir('C:\\Users\\bury\Desktop\\HeadFirstPython\\chapter3')
try:
    data = open('C:\\Users\\bury\Desktop\\HeadFirstPython\\chapter3\\sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing~')

#print(man)
#print(other)
#写入文件并保存至磁盘
try:
    man_file = open('man_file.txt','w')#打开文件并以w模式打开 write 默认为r模式 read
    other_file = open('other_file.txt','w')

    print(man,file = man_file) #写入文件为print 由file 文件对象名来控制
    print(other,file = other_file)
    print("已保存至文件~")
    
    man_file.close() #记得关闭文件!
    other_file.close()
except IOError :
    print('File error')
    
