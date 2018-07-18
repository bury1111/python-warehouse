import os

os.getcwd()

os.chdir('C:\\Users\\bury\\python-warehouse\\HeadFirstPython\\chapter3')

data = open('sketch.txt')

for each_line in data:
	try:
		(role,line_spoken) = each_line.split(':',1)
		print(role,end=' ')
		print(' said: ',end=' ')
		print(line_spoken,end=' ')
	except:
		pass

data.close()