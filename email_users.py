import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from generator_config import config
from User import User, get_users
import socket

MY_ADDRESS = config['sender_mail']
PASSWORD = config['sender_pass']
INTIXEL_MAIL_SERVER = config['server']
INTIXEL_PORT = config['port']


def fill_mail_template(user: User):
    """
    Returns a the template for a mail after filling the data.
    """
    
    msg = 'Dear {0},\nThis is the new password \"{1}\" for the user \"{2}\". On the machine \"{3}\" with internal IP \"{4}\".\nNote the old password was \"{5}\".\nRegards,'\
        .format(user.name,user.new_pass,user.user_name,socket.gethostname(),socket.gethostbyname(socket.gethostname()),user.old_pass)

    return msg

def send(file: str):
    users = get_users(file) # read contacts

    # set up the SMTP server
    print(INTIXEL_MAIL_SERVER,INTIXEL_PORT)
    s = smtplib.SMTP(host=INTIXEL_MAIL_SERVER, port=INTIXEL_PORT)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for user in users:
        print(user)
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = fill_mail_template(user)

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=user.mail
        msg['Subject']="New password for your user name"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    import sys
    file = sys.argv[1]
    send(file)