# -*- coding: utf-8 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

import smtplib


def instantiating_mail(smtp_server, port, sender, password):
    """This function instantiates the email session.

    Parameters
    ----------
    smtp_server : str
        smtp_server DNS address.
    port : int
        smtp_server port.
    sender : str
        The sender mail address.
    token : str
        Account´s token.

    Returns
    -------

    """
    session = smtplib.SMTP(smtp_server, port)
    session.ehlo()
    session.starttls()
    session.login(sender, password)


def mail(sender, to, subject, content=None, attachment=None, port=25,
         token='', smtp_server='smtp.gmail.com'):
    """This function send emails.

    Parameters
    ----------
    sender : str
        The sender mail address.
    to : str
        Recipient list.
    subject : str
        Message subject.
    content : str, optional
        Content subject.
    attachment : str, optional
        Attachment path.
    port : int
        smtp_server port.
    token : str, optional
        Account´s token.
    smtp_server : str, optional
        smtp_server DNS address.

    Returns
    -------

    """
    instantiating_mail(smtp_server, port, sender, token)

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = to

    message.attach(MIMEText(content))
    if attachment:
        part = MIMEBase('application', "octet-stream")
        if isinstance(attachment, str):
            with open(attachment, 'r') as f:
                part.set_payload(f.read())

            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename="{}"'.format(
                                attachment.split('\\')[-1]
                            ))
        message.attach(part)

    with smtplib.SMTP_SSL(smtp_server, 465) as server:
        server.login(sender, token)
        server.sendmail(sender, message['To'].split(','), message.as_string())
