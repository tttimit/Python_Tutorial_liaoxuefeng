##from email import encoders
##from email.header import Header
##from email.mime import *
##from email.mime.text import MIMEText
##from email.utils import parseaddr, formataddr
from email import *
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def test():
    from_addr = 'timit_cloud@163.com'
    password = 'zly19911206+bjyz'
    to_addr = 'timit_cloud@qq.com'
    smtp_server = 'SMTP.163.com'
    # =============
    # 发送纯文本邮件
    # msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
    # ======
    
    # ============
    # 如果要发送HTML格式的邮件：
    # msg = MIMEText('<html><body><h1>Hello</h1>' + '<p>Send by Python...</p></body></html>', 'html', 'utf-8')
    # ======

    # ============
    # 如果要发送附件，附件可以看作一个包含多个部分的邮件，文本及各个附件本身
    # MIMEMultipart整个邮件 = MIMEText文本 + MIMEBase各个附件
    msg = MIMEMultipart()
    # 邮件正文
    msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

    #从本地打开一个图片添加到附件中
    with open('test.jpg', 'rb') as f:
        mime = MIMEBase('image', 'jpeg', filename='test.jpg')
        #  加上一些必要的头信息
        mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件内容读取进来
        mime.set_playload(f.read())
        # 使用base64编码
        encoders.encode_base64(mime)
        #　添加到MIMEMultipart
        msg.attach(mime)
    # ======

    # =========
    # 某些老的设备可能不支持HTML邮件，可以添加纯文本作为替代选项
    msg = MIMEMultipart('alternative')
    msg.attach(MIMEText('hello', 'plain', 'utf-8')
    msg.attach(MIMEText('<html><body><h1>可以显示HTML。。。</h1></body></html>', 'html', 'utf-8')
    # ======               
    
    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('炸裂者 <%s>' % to_addr)
    msg['Subject'] = Header('来自疾风的问候！。。', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)

    # =======
    # 普通的邮件再传输时使用的是明文，可能会被窃听
    # 更安全的方法是先创建SSL安全连接，再使用SMTP协议发送邮件
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    # ======
    
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


test()

