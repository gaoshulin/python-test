import os
import yaml
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

with open('../env/env.yaml', 'r') as file:
    config = yaml.safe_load(file)

# global config
mail_conf = config.get('mail', {})
if not mail_conf:
    # 退出程序
    exit()


def send_main_message(email, subject, content, file_path=''):
    """
    发送邮件服务
    :param email: 收件人邮箱
    :param subject: 邮件主题
    :param content: 邮件正文内容
    :param file_path: 附件文件路径
    """
    # 获取邮件配置
    # 邮箱SMTP服务器地址
    smtp_server = mail_conf.get('mail_host', '')
    # 邮箱SMTP服务端口号（SSL加密）
    smtp_port = mail_conf.get('mail_port', '')
    # 发件人邮箱地址
    sender_email = mail_conf.get('mail_username', '')
    # 发件人邮箱授权码
    sender_password = mail_conf.get('mail_password', '')
    # 发件人来源名称
    sender_name = mail_conf.get('mail_from_name', '')

    # 创建邮件对象
    msg = MIMEMultipart()

    # 确保 From 头格式正确
    msg['From'] = f'{sender_name} <{sender_email}>'
    msg['To'] = email
    msg['Subject'] = subject
    # 邮件正文内容 - 文本
    msg.attach(MIMEText(content, 'plain', 'utf-8'))

    # 接受 html 内容
    # htmlContent = "<html><body><h1>Hello</h1></body></html>"
    # msg.attach(MIMEText(htmlContent, 'html', 'utf-8'))

    try:
        # 如果有附件，添加附件到邮件中
        if file_path and os.path.exists(file_path):
            with open(file_path, 'r') as f:
                # 创建附件对象
                attachment = MIMEApplication(f.read())
                # 设置附件的文件名
                attachment.add_header('Content-Disposition', 'attachment', filename=file_path.split('/')[-1])
                # 将附件添加到邮件中
                msg.attach(attachment)

        # 创建SMTP对象，使用SSL加密
        smtp_obj = smtplib.SMTP_SSL(smtp_server, smtp_port)
        # 登录邮箱
        smtp_obj.login(sender_email, sender_password)
        # 发送邮件
        smtp_obj.sendmail(sender_email, email, msg.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("邮件发送失败:", e)
    except FileNotFoundError:
        print(f"附件文件 {file_path} 未找到。")
    finally:
        # 确保 smtp_obj 已定义并成功创建
        if 'smtp_obj' in locals():
            smtp_obj.quit()


# 示例调用
email_mail = '1453811292@qq.com'
email_subject = '邮件测试主题'
email_content = '这是一封使用 Python 发送的邮件。'
attachment_file = './basic.py'
send_main_message(email_mail, email_subject, email_content, attachment_file)
