import os

os.getcwd()

#os.chdir('C:\\Users\\bury\Desktop\\HeadFirstPython\\chapter3')

try:
                data = open('C:\\Users\\bury\Desktop\\HeadFirstPython\\chapter3\\sketch.txt')
                
                for each_line in data:
                        try:
                         (role,line_spoken) = each_line.split(':',1)
                         print(role,end=' ')
                         print(' said: ',end=' ')
                         print(line_spoken,end=' ')
                        except ValueError: #ValueError处理
                                pass

                data.close()
except IOError : #IOError处理
        print('The data file is missing~')
