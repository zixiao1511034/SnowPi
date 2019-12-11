import sendgrid
# import thing
import os


def send():
    # api key

    print("start sending email")
    client = sendgrid.SendGridClient(<KEY>)

    message = sendgrid.Mail()
    message.add_to(<EMAIL>)
    message.set_from(<EMAIL>)
    message.set_subject("Deep Snow Alert!")
    message.set_html("Snow is deep, be careful!!")
    client.send(message)
    print("has sent email")


with open('/home/pi/Documents/rpiWebServer/test_fifo') as f:
    for line in f:
        print(line, type(line))
        if line == 'sendEmail\n':
            print("enter")
            send()
            print('finish')
            break
# while True:
#     import thing
#     if thing.signal == 1:
#         print("get signal from thing!")
#         #print "come into"
#         send()

# while True:
#     signal = thing.get_name()
#     if thing.signal == 1:
#         print("get signal from thing!")
#         # print "come into"
#         send()
#         break
