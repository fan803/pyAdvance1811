import smtplib
from email.mime.text import MIMEText
#建立连接
smtp = smtplib.SMTP("smtp.163.com")
#登录
smtp.login("614212406@qq.com","fan0803.long")
#发送邮件
sender = "453008210@qq.com"
recever = "2513762020@qq.com"
message =MIMEText("123")
message["from"] = sender
message["to"] = recever
message["subject"] = "好嗨哦"
smtp.sendmail(sender,recever,message.as_string())
# smtp.sendmail("发送者","接收者","发送内容")

#退出
smtp.quit()