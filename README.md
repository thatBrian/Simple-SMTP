# Simple SMTP
### This project allows the user to send email through terminal using python.


## How does it work?
This program will ask the user for their user name and password for G Mail, then recipients(s), subject and body. The program will then try to establish a connection to 'smtp.gmail.com' on port 465, log the user in, transfer the user's message then close the connection.



## Example
python smtp.py

  *EMAIL: HCLinton@gmail.com
  PASSWORD: p@55w0rd
  Recipient(s): kimJongUn@gmail.com TrumpMyBaby@gmail.com
  Subject: test
  Body: body test test test
  Compile: CHECK
  Extended HELO: CHECK
  Login: CHECK
  Transefer: CHECK
  SENDING...
  Email sent!*
