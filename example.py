import py_mailer



Sender='youremail@example.com' 
Recipient='recipient@example.com' 
subject='hi subj' 
message='Hi body'


py_mailer.sendEmail(Sender, Recipient, subject, message)
