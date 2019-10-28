import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

browser = webdriver.Chrome()

path = os.getcwd()

print('Path: ' + path)


def create_project():
    repo_name = input('Repo Name: ')
    username = input('Enter your github email: ')
    password = getpass.getpass()

    browser.get('https://www.github.com/login')
    username_field = browser.find_elements_by_xpath('//*[@id="login_field"]')[0]
    password_field = browser.find_elements_by_xpath('//*[@id="password"]')[0]

    username_field.send_keys(username)
    password_field.send_keys(password)

    password_field.send_keys(Keys.ENTER)

    browser.find_element_by_xpath('/html/body/div[4]/div/div/div/main/div[1]/div/div/a[2]').click()

    repository_name = browser.find_elements_by_xpath('//*[@id="repository_name"]')[0]
    repository_name.send_keys(repo_name)



if __name__ == "__main__":
    create_project()
