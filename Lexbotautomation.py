import boto3

client = boto3.client("lex-runtime");

try:
	client.post_text(botName="Employment_Details", botAlias="botAlias", userId = "12345", inputText="Hi")
	response = client.post_text(botName="Employment_Details", botAlias="botAlias", userId = "12345", inputText="123456");
	msg = response['message'];
       	if (msg == "Invalid Employment ID" or msg == "Valid Employment ID"):
        	print ("SUCCESS")
                print(msg)
		#return "true"
	else :
		print ("FAILURE")
		#return "false"

except:
	print ("Bot execution failed")
	print ("FAILURE")
	#return "false"

