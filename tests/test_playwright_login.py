from pytest_bdd import given, when, then, parsers
from modules.playwright_login.playwright_login import *


@given('User open IRCTC url in browser')
def step_def(browser_context):
    open_url(browser_context)


@when(parsers.parse('User click on Login, enter credentials username "{user}" password "{passcode}"'))
def step_def(browser_context, user, passcode):
    login(browser_context, user, passcode)


@when('User click on login & booking with otp')
def step_def(browser_context):
    log(browser_context)


@when('User confirms to book ticket')
def step_def(browser_context):
    confirm(browser_context)


@when('User click on Signin')
def step_def(browser_context):
    signin(browser_context)


@then('User verify')
def step_def(browser_context):
    verify_log(browser_context)
