# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC3cfe13dc949e5ef6d98622af42230ce6'
auth_token = '8e87e368c4e96750057fbddbade24311'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='I gat You!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+256787250196'
                          )

print(message.sid)