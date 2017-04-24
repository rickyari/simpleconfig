#!/usr/bin/env python

import smtplib

FROM = "gagsingh@expedia.com"
TO = ["gagsingh@expedia.com"]
SUBJECT = "Hello!"
TEXT = "This message was sent with Python's smtplib."

message = """\
From: %s
To: %s
Subject: %s

%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

server = smtplib.SMTP('chsmtp.idx.expedmz.com', 25)

server.sendmail(FROM, TO, message)

server.quit()
