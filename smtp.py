import smtplib

gmail_user = raw_input('EMAIL: ')
gmail_password = raw_input('PASSWORD: ')

sent_from = gmail_user
to = raw_input('Recipient(s): ').split();
subject = raw_input('Subject: ');
body = raw_input('Body: ');s

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    print 'Compile: CHECK'
    server.ehlo()
    print 'Extended HELO: CHECK'
    server.login(gmail_user, gmail_password)
    print 'Login: CHECK'
    server.sendmail(sent_from, to, email_text)
    print 'Transefer: CHECK'
    server.close()
    print 'SENDING...'
    print 'Email sent!'
except:
    print 'Something went wrong...'
