import os
import imghdr
import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with open('./mail_template/index.html', 'r') as f:
    html = f.read()

msg = EmailMessage()
msg['Subject'] = 'Check out custom Mail'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'chris.kafrouni@gmail.com'
msg.set_content('This is a plain text body.')



#logo_shop    = make_msgid()
#Products     =
#one          =
#two          =
#three        =
#facebook2x   =
#twitter2x    =
#instagram2x  =
#linkedin2x   =

#html = html.format(
#    logo_shop,
#    Products,
#    one,
#    two,
#    three,
#    facebook2x,
#    twitter2x,
#    instagram2x,
#    linkedin2x
#)

msg.add_alternative(html, subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)