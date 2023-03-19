from behave import given
from utilities.commonFunctions import webcommon


@given(u'user is on "{url}"')
def go_to_url(context, url):
    context.driver = webcommon.go_to(url, browser_type='chrome')


