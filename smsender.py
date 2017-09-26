from twilio.rest import TwilioRestClient

acc_sid = 'AC42474977264072da7257d91e3b3f3ed6'
auth = '7516b1f35a73ce1df1ec7909e637063a'
client = TwilioRestClient(acc_sid,auth)

message = client.sms.message.create(body = 'Hello world!', 
	to = '+17025335332', from_= '+1702919576')
print message.sid