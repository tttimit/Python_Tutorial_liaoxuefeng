from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

msg_content = b''

with open('msg.txt', 'rb') as f:
    while True:
        buffer = f.read(1024)
        if buffer:
            msg_content += buffer
        else:
            break

# print("msg:", type(msg))
print('msg:', msg_content)

msg = Parser().parsestr(str(msg_content))


# 邮件对象有可能是一个 MIMEMultipard 对象，因此我们可以递归地打印出Message的层次结构

def print_info(message, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = message.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if message.is_multipart():
        parts = message.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s----------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = message.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = message.get_payload(decode=True)
            charset = guess_charset(message)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, str(content) + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(message):
    charset = message.get_charset()
    if charset is None:
        content_type = message.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8].strip()
    return charset


print_info(msg)
