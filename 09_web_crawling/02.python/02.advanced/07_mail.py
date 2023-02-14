"""
SMTP =>
Simple Mail Transfer Protocol
메일을 서버로 보낼 때 쓰는 규칙

POP =>
Post Office Protocol
메일을 서버로부터 받을 때 쓰는 규칙

"""

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

SMTP_SERVER = "smtp.gmail.com"  # 메일 서비스마다 다름
SMTP_PORT = "465"  # 메일 서비스마다 다름
SMTP_USER = "bizyoung93@gmail.com"  # 보낼 사람의 이메일 주소
SMTP_PASSWORD = "hykimbephvqxsanl"


"""
1) 기본 내용 및 구조
"""

msg = MIMEMultipart("alternative")  # 기본값이 alternative, 첨부파일 있을 때는 mixed

msg["From"] = "SMTP_USER"
msg["To"] = "bluefri0329@gmail.com"
msg["Subject"] = "제목"

# text = MIMEText("내용 메시지", _charset="utf-8")
text = MIMEText("내용 메시지", _charset="utf-8")
msg.attach(text)


"""
2) 실제 메일 보내는 코드
"""

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login(SMTP_USER, SMTP_PASSWORD)  # 로그인
# smtp.sendmail(SMTP_USER, "실제 보내는 대상 메일 주소", msg.as_string)
smtp.sendmail(SMTP_USER, "bluefri0329@gmail.com", msg.as_string)
smtp.close()
