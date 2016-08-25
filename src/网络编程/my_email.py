from email.mime.text import MIMEText
# 组装信息，第一个参数就是正文，第二个是MIME类型的subtype，第三个参数是编码
msg = MIMEText('hello, send by Python...\r\n 测试一下，给点面子啊！', 'plain', 'utf-8')

# 准备登陆发送邮箱的口令
##from_addr = input('From:')
##password = input('Password:')
from_addr = 'timit_cloud@163.com'
password = 'zly19911206+bjyz'


#目的地地址
##to_addr = input('To:')
to_addr = 'timit_cloud@qq.com'

# 发送邮箱的SMTP服务器地址
##smtp_server = input('SMTP server:')
smtp_server = 'SMTP.163.com'

import smtplib
server = smtplib.SMTP(smtp_server, 25)
# 可以打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
# 登陆服务器
server.login(from_addr, password)
# 可以发送给多个地址，因此第二个参数是个list
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
