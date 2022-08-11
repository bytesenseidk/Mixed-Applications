import os
import sys
import pickle
import imaplib
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
from mimetypes import guess_type as guess_mime_type
from base64 import urlsafe_b64encode, urlsafe_b64decode


class Login(object):
    mail_servers = {
        "gmail": [["smtp.gmail.com", 587], ["imap.gmail.com", 993]],
        "aol": [["smtp.aol.com", 587], ["imap.aol.com", 993]],
        "outlook": [["smtp-mail.outlook.com", 587], ["imap-mail.outlook.com", 993]],
        "bt-connect": [["smtp.btconnect.com", 25], ["imap4.btconnect.com", 143]],
        "office365": [["smtp.office365.com", 587], ["outlook.office365.com", 993]],
        "yahoo": [["smtp.mail.yahoo.com", 465], ["imap.mail.yahoo.com", 993]],
        "yahoo-plus": [["plus.smtp.mail.yahoo.com", 465], ["plus.imap.mail.yahoo.com", 993]],
        "yahoo-uk": [["smtp.mail.yahoo.co.uk", 465], ["imap.mail.yahoo.co.uk", 993]],
        "yahoo-europe": [["smtp.mail.yahoo.com", 465], ["imap.mail.yahoo.com", 993]],
        "t-online": [["securesmtp.t-online.de", 587], ["secureimap.t-online.de", 993]],
        "verizon": [["outgoing.verizon.net", 587], ["incoming.verizon.net", 143]]
        # Find additional mail servers at https://www.systoolsgroup.com/imap/
    }
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        if email != "debug" and password != "debug":
            try:
                self.smtp_server, self.smtp_port = Login.mail_servers[email.split("@")[1].split(".")[0]][0]
                self.imap_server, self.imap_port = Login.mail_servers[email.split("@")[1].split(".")[0]][1]
            except KeyError:
                sys.exit("Invalid email address")
            
    def __str__(self):
        if hasattr(self, "smtp_port"):
            data = "\n"
            for key, value in self.__dict__.items():
                data += f"{key}: \t{value}\n"
            return data
        return "Invalid email address"
    
    @staticmethod
    def gmail_validation():
        # Gmail user access and refresh tokens
        scope = ["https://mail.google.com/"]
        creds = None
        if os.path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("Client_Credentials.json", scope)
                creds = flow.run_local_server(port=0)
            with open("token.pickle", "wb") as token:
                pickle.dump(creds, token)
        return build("gmail", "v1", credentials=creds)
    
    def login(self):
        if self.email == "debug" and self.password == "debug":
            return True
        try:
            imap = imaplib.IMAP4_SSL(self.imap_server)
            imap.login(self.email, self.password)
            return True
        except imaplib.IMAP4.error:
            return False
    
    def logout(self):
        pass
    
    def send_email(self):
        pass
    
    def read_email(self):
        pass
    
    def delete_email(self):
        pass
    
    
if __name__ == "__main__":
    with open("LoginCreds.txt", "r") as f:
        email = f.readline().strip()
        password = f.readline().strip()
        api_key = f.readline().strip()
    user = Login(email, password)
    print(user)
    user.login()
    
