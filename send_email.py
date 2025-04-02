import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "rojko.alina@gmail.com"
password = "flaj cves tvjs pggt"

receiver = "ipr.1776@gmail.com"
context = ssl.create_default_context()

message = """
Hi!
How are you ?
Buy!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, )