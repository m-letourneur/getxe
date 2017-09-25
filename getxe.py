import os
from bs4 import BeautifulSoup
from urllib import urlopen
from selenium import webdriver

import schedule
import time

import smtplib
from config import EMAIL, PASSWORD


def send_mail(close_rate, comment):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    # Next, log in to the server
    server.login(EMAIL, PASSWORD)

    # Send the mail
    msg = ("Hello!\n\n" +
           'Look at that SGD-EUR rate: ' + str(close_rate) + '! ' + comment
           + '\n\nBest regards,'
           + '\nMarc'
           + '\n\n\n\n\n\n\n\nDisclaimer - email automatically generated if the SGD-EUR rate is above 0.64')
    msg = "\r\n".join([
        "From: " + EMAIL,
        "To: " + 'marcletourneur@hotmail.fr',
        "Subject: tedlt",
        "",
        msg
    ])

    server.sendmail(EMAIL, 'marcletourneur@hotmail.fr', msg)
    server.sendmail(EMAIL, 'auguste.byiringiro@laposte.net', msg)
    server.quit()


def routine():
    url = 'https://www.xe.com/currencycharts/?from=SGD&to=EUR&view=1Y'
    driver = webdriver.Chrome('/Users/Caco/bin/chromedriver')
    driver.get(url)
    html_source = driver.page_source
    driver.quit()

    sp = BeautifulSoup(html_source, "html.parser")
    # print sp
    items = sp.find_all(attrs={"id": "rates_detail_desc"})
    close_rate = items[0].contents[2]
    close_rate = float(str(close_rate)[8:13])
    print close_rate

    if close_rate > 0.64:
        send_mail(close_rate, "Go for it.")
        print "Bingo"
    else:
        # send_mail(close_rate, "Wait a bit...")
        print "Wait a bit..."

schedule.every().day.at("8:30").do(routine)
schedule.every().day.at("17:30").do(routine)
# schedule.every().day.at("20:17").do(routine)

while True:
    schedule.run_pending()
    time.sleep(1)

# if __name__ == '__main__':
#     send_mail(close_rate=0.5, comment='Ah')
