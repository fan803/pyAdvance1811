import smtplib
from email.mime.text import MIMEText
#建立连接
smtp = smtplib.SMTP("smtp.qq.com")
#登录
smtp.login("453008210@qq.com","fan803.long")
#发送邮件
sender = "453008210@qq.com"
recever = "1539401976@qq.com"
message =MIMEText("12345上山打老虎,傻子，12345上山打老虎")
message["from"] = sender
message["to"] = recever
message["subject"] = "好嗨哦"
smtp.sendmail(sender,recever,message.as_string())
# smtp.sendmail("发送者","接收者","发送内容")

#退出
smtp.quit()


