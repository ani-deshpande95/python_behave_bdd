import pdb

from utilities.commonSteps.webstepscommon import *
from behave import when, then
from utilities.commonFunctions import webcommon
from utilities.commonConfig import qaconfig
import requests
import json


@when('user enters username "{useremail}"')
def enter_username(context, useremail):
    useremail = qaconfig.QADATA.get(useremail)
    username = webcommon.find_element(context, 'name', 'username')
    username.is_displayed()
    username.click()
    username.send_keys(useremail)


@when('user enters password "{userpassword}"')
def enter_password(context, userpassword):
    userpassword = qaconfig.QADATA.get(userpassword)
    password = webcommon.find_element(context, 'name', 'password')
    password.is_displayed()
    password.click()
    password.send_keys(userpassword)


@when('user clicks on login button')
def click_login(context):
    login_button = webcommon.find_element(context, 'css selector', '[value="Log In"]')
    login_button.click()


@then('welcome text should be displayed')
def assert_login(context):
    welcome_text = webcommon.find_element(context, 'xpath', '//div[@id="leftPanel"]//b[text()="Welcome"]')
    welcome_text.is_displayed()


@given('user setup the login api data')
def login_api_setup(context):
    payload = {
        "username": "test@ggggg.com",
        "password": "password1234"
    }
    #login_response = requests.post('https://parabank.parasoft.com/parabank/login.htm', params=payload)
    login_response = requests.get('https://reqres.in/api/user/2')
    print(login_response.json())
