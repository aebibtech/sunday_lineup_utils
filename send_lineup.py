import sys
import os
from getpass import getpass
import json
import fbchat
import re
from fbchat import Client
from fbchat.models import *
from open_lineup import open_file

fbchat._state.FB_DTSG_REGEX = re.compile(r'"DTSGInitialData",\[\],{"token":"(.*?)"')

def get_config():
    fb_cred = None
    email = ''
    pswd = ''
    tid = ''
    try:
        fhand = open(os.path.expanduser("~/.fbconfig"))
        fb_cred = fhand.readlines()
        email = fb_cred[0].replace('\n', '')
        pswd = fb_cred[1].replace('\n', '')
        tid = fb_cred[2]
        fhand.close()
    except:
        print("No fb credentials found")
        email = input("FB email|phone|username: ")
        pswd = getpass()
        print('Thread ID of Group Chat')
        tid = input('(The number after t/): ')
        fb_cred_file = open(os.path.expanduser("~/.fbconfig"), "w")
        fb_cred_file.write(email + "\n")
        fb_cred_file.write(pswd + "\n")
        fb_cred_file.write(tid)
        fb_cred_file.close()

    return [email, pswd, tid]


config = get_config()
email = config[0]
pswd = config[1]
tid = config[2]

sess_file = '~/fbsession.json'

try:
    lineup_date = sys.argv[1]
except:
    lineup_date = input('Line-up date (yyyy-mm-dd): ')


print("Line-up date: ", lineup_date, "\n")

greeting = "Hi Team! This is our line up for this Sunday:\n\n\n"

lineup_msg = greeting + open_file(lineup_date).read()

print(lineup_msg)

cookies = {}
try:
    # Load the session cookies
    with open(os.path.expanduser(sess_file), 'r') as f:
        cookies = json.load(f)
except:
    # If it fails, never mind, we'll just login again
    pass

# Attempt a login with the session, and if it fails, just use the email & password
client = Client(email, pswd, max_tries=2, session_cookies=cookies)

# ... If logged in, send Line up message to GC.
sent = False
if client.isLoggedIn():
    print("\n\nFacebook login success!\n")
    print("Sending Line-up {}...\n\n".format(lineup_date))
    sent = client.send(Message(text=lineup_msg), thread_id=tid, thread_type=ThreadType.GROUP)

if sent:
    print("Line-up {} was sent successfully!\n\n\n".format(lineup_date))
else:
    print("Line-up {} not sent.".format(lineup_date))

# Save the session again
with open(os.path.expanduser(sess_file), 'w') as f:
    json.dump(client.getSession(), f)