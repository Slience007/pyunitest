'''
email模块负责构造邮件内容
smtplib模块负责发送邮件
'''
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.header import Header

class sendEmail():
    #定义全局变量邮件服务器地址，登录用户，授权码
    global MAILHOST,MAILUSER,MAILPWD
    MAILHOST = "smtp.126.com"
    MAILUSER = "wang_suqiang@126.com"
    MAILPWD = "wsq126"

    def __init__(self,subject,content,reveiver,attachPath=""):
        self.subject = subject
        self.content = content
        self.receiver = reveiver
        self.attachPath = attachPath
    #写邮件,返回msg.as_string()
    def writeEmail(self):
        msg = MIMEMultipart()
        #邮件正文
        msg.attach(MIMEText(self.content, 'plain', 'utf8'))
        receiverName = ",".join(self.receiver)
        msg['from'] = Header(MAILUSER,'utf-8')
        #msg['to'] =  Header(",".join(self.receiver)).encode()
        msg['to'] = Header(receiverName).encode()
        #邮件主题
        msg['Subject'] = Header(self.subject,'utf-8').encode()
        #print("msg is:",msg)
        #attachPath不为空则添加附件到邮件中
        if self.attachPath != "":
            with open(self.attachPath, 'rb') as f:
                attach1  = MIMEText(f.read(), 'base64', 'utf-8')
                attach1["Content-Type"] = 'application/octet-stream'
                #filename可以随便写
                attach1["Content-Disposition"] = 'attachment; filename="Result.html"'
                msg.attach(attach1)

        return msg.as_string()

    #发送邮件
    def sendEmail(self):
        receiver = ";".join(self.receiver)
        try:
            #连接邮件服务器
            server = smtplib.SMTP()
            server.connect(MAILHOST,25)
            #打开debug模式可以看到握手过程
            #server.set_debuglevel(1)
            #登录，MAILPWD为网易邮件的授权码
            server.login(MAILUSER,MAILPWD)
            #发送邮件
            server.sendmail(MAILUSER,receiver,self.writeEmail())
            server.quit()
            print("Email send sucess.")
        except Exception as  e:
            print("Email send fail.")
            print(e)







