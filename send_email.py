import smtplib
from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header

#收件人邮箱地址
mailto_list=["xx@xx.xx"]
#####################
#设置发送邮箱的服务器，用户名、口令以及邮箱的后缀
mail_host="smtp.xx.com"
mail_user="xx@xx.com"     #用户名
mail_pass="****"    #密码
mail_postfix="xx.com"
######################
def send_mail(to_list,sub,content):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@163.com","sub","content")
    '''
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
 
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e :
        print(str(e))
        return False
 
if __name__ == '__main__':
    if send_mail(mailto_list,"发送的主题~","发送的内容"):
        print ("发送成功")
    else:
        print ("发送失败")
