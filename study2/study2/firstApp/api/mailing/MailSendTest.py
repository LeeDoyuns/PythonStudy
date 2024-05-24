import smtplib
from email.mime.text import MIMEText
from study2.config.utils import *
from django.http import HttpResponse,JsonResponse
from rest_framework import status
import os
import sys

#메일보내기

projectRoot = Path(__file__).resolve().parent.parent.parent.parent / 'study2'
# projectRoot = projectRoot / '\study2\study2\study2'
JSON_PATH = os.path.join(projectRoot, 'secret.json')
# paths = root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(JSON_PATH)
jsonData = read_json(JSON_PATH)
sendEmailAddr = jsonData["gmail_id"]
recvEmailAddr = jsonData["recv_mail"]
password = jsonData["gmail_pwd"]

def gmailSendTest(rea):
    smtpName = "smtp.gmail.com"
    smtpPort = 587
    text = "<h1>테스트</h1> </br></br> <p>testets</p>"
    msg = MIMEText(text, "html", "utf8")
    
    msg["Subject"] = "이거슨 메일제목"
    msg["From"] = sendEmailAddr
    msg["To"] = recvEmailAddr
    print(msg.as_string)
    
    
    smtp = smtplib.SMTP(smtpName, smtpPort)
    smtp.starttls()
    smtp.login(sendEmailAddr, password)
    smtp.sendmail(sendEmailAddr, recvEmailAddr, msg.as_string())    #메일전송, 문자열로 변환 필요
    smtp.close()
    
    return JsonResponse({"sendMailTest": "success"}, safe=False, json_dumps_params={'ensure_ascii':False}, status = status.HTTP_200_OK)