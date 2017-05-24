from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC9f20aa02b0e5da64e3f8ce0f1c0a7305"
# Your Auth Token from twilio.com/console
auth_token  = "178267b9ad9f9879146b2032aeca6743"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+919654175851", #your own phone number registered with twilio
    from_="+18703904066",  #your twilio number
    body="Hey I think you are Piyush Goel, right!! Dont worry its me")

print(message.sid)
