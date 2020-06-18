import config   # You have to create your own config.py file where you store PASSWORD and EMAIL_ADDRESS
import smtplib
import requests
import time
from bs4 import BeautifulSoup

url = 'https://www.lappisgym.se/'

r = requests.get(url, timeout=5)

counter_value = '0'

time_counter = 0

while counter_value == '0':

    if r.status_code == 200:             # Status code 200 means "OK"

        soup = BeautifulSoup(r.text, 'html.parser')  # We use a html parser

        l = soup.findAll("p", {"class": "text-blue-darkest pt-2"})  # there are two lines to be found

        text = str(l[1])                                            # we only want the second one

        text_list = text.split()                                    # we split the list

        # print(text_list)

        counter_value = text_list[9]                                # This is where we want to monitor

        # print(counter_value)

    else:
        print("Error")

    time.sleep(30)                                                  # we monitor every 30 second
    time_counter += 1

    if time_counter % 60 == 0:

        print('programmet har varit igång i ' + str(time_counter/60) + ' timmar.')  # Every hour a message is printed


def notify_user():  # will send me an email if there is ever an available keycard at the gym

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(config.EMAIL_ADDRESS, config.PASSWORD)

        msg = 'Ledigt KEYCARD till lappis gym!!!'   # the message

        # logging.info('Sending Email...')
        smtp.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, msg)

# If the while loop breaks while the program is running, we send the email by running the function

# notify_user()





