from behave import given
from utilities.commonFunctions import webcommon
from utilities.commonConfig import qaconfig


@given(u'user is on "{url}"')
def go_to_url(context, url):
    url = qaconfig.QADATA.get(url)
    context.driver = webcommon.go_to(url, browser_type='chrome')


