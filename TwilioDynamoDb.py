import boto3
import datetime
from twilio.rest import Client

# Dynamodb table details
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('twilio_stop_number')

# Account Sid and Auth Token from twilio.com/user/account
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
client = Client(account_sid, auth_token)

sms = client.messages("xxxxxxxxxxxxxxxxxxxxxxx").fetch()
print("SMS was sent from %s" % sms.from_)
print("SMS Body %s" % sms.body.encode('utf-8'))
print("Twilio sent the above SMS %s" % sms.to)
print("Date sent %s" % sms.date_sent)
print("Status of the message: %s" % sms.status)

# Inserting the Phone number,Date,Time and Body of the SMS.
from_phone=long(sms.from_)
sms_body=sms.body
#write=table.put_item(Item={'phone_number':from_phone,'sms_body':sms_body})

if (sms_body == "start"):
	try:
		table.delete_item(Key={'phone_number':from_phone});
	except:
		print ("Not able to delete with the Number: "+str(from_phone))
		
else:
	if (sms_body == "Stop"):
		table.put_item(Item={'phone_number':from_phone,'sms_body':sms_body, 'Date':datetime.datetime.now().strftime("%c")})
