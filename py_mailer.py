import dns.resolver
import smtplib
from email.mime.text import MIMEText



def printMXserver(domain):
	answers = dns.resolver.query(domain, 'MX')
	for rdata in answers:
		print 'Host', rdata.exchange, 'has preference', rdata.preference

def getMXserver(domain):
	try:
		answers = dns.resolver.query(domain, 'MX')
		for rdata in answers:
			return str(rdata.exchange).rstrip('.')
	except:
		return None
		

def sendEmail(Sender, Recipient, subject, message, Server=None):
	msg = MIMEText(message)
	msg['Subject'] = subject
	msg['From'] = Sender
	msg['To'] = Recipient

	if Server is None:
		Server = getMXserver(Recipient.split("@")[1])
	if Server is None:
		print 'No MX record found to relay message'
		return False
	
	print "Server:", Server
	raw_input(">>")

	s = smtplib.SMTP(Server)
	s.sendmail(Sender, [Recipient], msg.as_string())
	s.quit()
	
	
