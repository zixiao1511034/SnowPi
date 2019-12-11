import sendgrid
from sendgrid.helpers import mail

# api key
api = sendgrid.SendGridAPIClient('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')

recipient = mail.Email('yz2455@cornell.edu')
sender = mail.Email('yueyuecornell1997@gmail.com')
subject = 'Sending with SendGrid is fun'
body = mail.Content('text/plain', 'and easy to do anywhere, even with Python')

email = mail.Mail(sender, subject, recipient, body)
response = api.client.mail.send.post(request_body=email.get())

print(response.status_code)
print(response.body)
print(response.headers)
