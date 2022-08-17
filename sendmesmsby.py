from twilio.rest import Client





def sendmessage(theimported):
	account_sid =''
	account_token='add it your self'
	number='+add it your self'
	client = Client(account_sid,account_token)
	message = client.messages.create(
		body=theimported,
		from_=number,
		to='+251920304374')

while True:
	theinput = input('please inter your message please: ')
	sendmessage(theinput)
	sendmessage(theinput)