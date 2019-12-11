import sendgrid
import time
import os
from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail


# api key

print("start sending email")
# # client = sendgrid.SendGridAPIClient(
# #     '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')
client = sendgrid.SendGridClient(
    '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')

message = sendgrid.Mail()
message.add_to("yz2455@cornell.edu")
message.set_from("zixiao1511034@outlook.com")
message.set_subject("Deep Snow Alert!")
message.set_html("Snow is deep, be careful!!")
client.send(message)
print("has sent email")
# message = Mail(
#     from_email='yz2455@cornell.edu',
#     to_emails='zw579@cornell.edu',
#     subject='Deep Snow Alert!',
#     html_content='<strong>Snow is deep, be careful!</strong>')
# try:
#     sendgrid_client = SendGridAPIClient(os.environ.get('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'))
#     response = sendgrid_client.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)



