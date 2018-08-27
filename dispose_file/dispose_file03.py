import os

class A:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name=a_name
        self.dob=a_dob
        self.times=a_times
    
    def sanitize(time_string):
        if '-' in time_string:
            splitter='-'
        elif '.' in time_string:
            splitter='.'
        else:
            return(time_string)
        (mins,secs)=time_string.split(splitter)
        return(mins+':'+secs)
        
    def top3(self):
        return (sorted(set([A.sanitize(t) for t in self.times]))[0:3])

    def get_coach_data(filename):
        try:
            with open(filename) as f:
                data=f.readline()
                tmpdata=data.strip().split(',')
                return(A(tmpdata.pop(0),tmpdata.pop(0),tmpdata))
        except IOError  as ioerr:
            print('File error:'+str(ioerr))
            return(None)
        
class AList(list):
    
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__ ([])
        self.name=a_name
        self.dob=a_dob
        self.extend(a_times)
        
    def top3(self):
        return(sorted(set([AList.sanitize(t) for t in self]))[0:3])

    def sanitize(time_string):
            if '-' in time_string:
                splitter='-'
            elif '.' in time_string:
                splitter='.'
            else:
                return(time_string)
            (mins,secs)=time_string.split(splitter)
            return(mins+':'+secs)

    def get_coach_data(filename):
        try:
            with open(filename) as f:
                data=f.readline()
                tmpdata=data.strip().split(',')
                return(AList(tmpdata.pop(0),tmpdata.pop(0),tmpdata))
        except IOError  as ioerr:
            print('File error:'+str(ioerr))
            return(None)
    
sarah=A.get_coach_data('data1.txt')
print(sarah.name+"'s fastest times: "+str(sarah.top3()))

#bury= A('bury')
#bury.add_time('2.01')
#print(bury.top3())
#bury.add_times(['2.12','2.22','1-22','3.23'])
#print(bury.top3())


bury = AList('bury asheng')

bury.append('1.32')
print(bury)
bury.extend(['2.22','1-21','2:22'])
print(bury.top3())
print(bury.name+"'s 最快的时间为"+str(bury.top3()))



















