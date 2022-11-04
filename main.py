from sys import argv
from time import sleep

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20100101&end=20201231'
LOAD_MORE = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/p[1]/button'
COOKIE_WINDOW = '/html/body/div[1]/div/div[3]/div/div[2]'


def initDriver():
    global driver
    options = Options()
    options.add_experimental_option('detach', True)  # Staying browser on after script exit.
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.get(URL)


def closeCookieWindow():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, COOKIE_WINDOW))).click()


def scrollDown():
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')


def loadMore():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, LOAD_MORE))).click()


def main():
    try:
        if argv[1] != '-t':
            print('No "-t" argument found.')
            return
        if isinstance(argv[2], int):
            print('Bad number entered.')

        initDriver()
        closeCookieWindow()

        if int(argv[2]) == 0:
            while True:
                scrollDown()
                loadMore()

        for i in range(int(argv[2])):
            scrollDown()
            loadMore()

    except IndexError:
        print('No "-t" argument found.')
        return
    except KeyboardInterrupt:
        print('Interrupt! Exiting...')
        exit(1)


if __name__ == '__main__':
    main()
