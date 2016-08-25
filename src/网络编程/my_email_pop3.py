# 发送邮件使用的是SMTP协议
# 获取邮件使用的是POP3，注意获取下来是编码后的纯文本，需要解析一下
# Python内置的 poplib 用来下载邮件到本地，email提供的一些类来解析内容

import poplib
from email.parser import Parser

# 输入邮件地址，口令，服务器地址
email = 'timit_cloud@163.com'
password = 'zly19911206+bjyz'
pop3_server = 'POP3.163.com'

# 连接到服务器
server = poplib.POP3(pop3_server)

# 打开调试信息
server.set_debuglevel(1)

#可选：打印服务器的欢迎信息
print(server.getwelcome().decode('utf-8'))

# 身份认证
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间
print('Message: %s.Size: %s' % server.stat())

# list()返回所有邮件的编号
resp, mails, octets = server.list()

# 可以查看返回列表
print(mails)

# 获取最新的一封邮件，索引从１开始，因此长度标识最新的
index = len(mails)
resp, lines, octets = server.retr(index)

# lines 存储了邮件的原始文本的每一行，可以这样获取整个邮件的原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')

# 解析出邮件
msg = Parser().parsestr(msg_content)
print(type(msg))
with open('msg.txt', 'wb') as f:
    f.write(bytes(str(msg), 'utf-8'))
    
    
# print('msg:', msg)

#可以根据邮件索引号直接从服务器删除邮件：
# server.dele(index)

server.quit()
