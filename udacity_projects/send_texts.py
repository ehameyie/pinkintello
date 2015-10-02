from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "some combination"
auth_token  = "some combination"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="AHAHAH Salut! Message a partir de python :B",
    to="+some number",    # Replace with your phone number
    from_="+some number") # Replace with your Twilio number
print message.sid
