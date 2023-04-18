import pdb

from utilities.commonSteps.webstepscommon import *
from behave import when, then
from utilities.commonFunctions import webcommon
from utilities.commonConfig import qaconfig
from google.cloud import storage


@when('user enters username "{useremail}"')
def enter_username(context, useremail):
    useremail = qaconfig.QADATA.get(useremail)
    username = webcommon.find_element(context, 'name', 'username')
    username.is_displayed()
    username.click()
    username.send_keys(useremail)
    webcommon.i_wait(context, 50)


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
    context.payload = {
        "username": "test@ggggg.com",
        "password": "password1234"
    }
    #login_response = requests.get('https://reqres.in/api/user/2')


@when('user request the post login API to "{baseuri}"')
def login_api_request(context, baseuri):
    context.api_response = webcommon.api_post_requests(context, baseuri=qaconfig.APIDATA.get(baseuri), uri='login.htm', param=context.payload)


@then('user should be able to login successfully with status code "{status_code}"')
def login_api_assert(context, status_code):
    assert context.api_response.status_code == 200


@given('user provides the "{bucket_name}" bucket name')
def step_impl(context, bucket_name):
    storage_client = storage.Client()
    context.bucket = storage_client.get_bucket(bucket_name)


@when('user provides the "{file_name}" file name')
def step_impl(context, file_name):
    context.blob = context.bucket.blob('Sample_csv.csv')
    context.blob = context.blob.download_as_string()
    context.blob = context.blob.decode('utf-8')


@then("file content should be printed to console")
def step_impl(context):
    print(context.blob)