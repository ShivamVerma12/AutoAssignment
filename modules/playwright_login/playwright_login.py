import time


def open_url(browser_context):
    browser_context.goto('https://www.irctc.co.in/')


def login(browser_context, user, passcode):
    xpath_locator = "//a[normalize-space()='LOGIN']"
    element = browser_context.locator(xpath_locator)
    element.click()

    username = browser_context.locator("//input[@placeholder='User Name']")
    username.fill(user)

    password = browser_context.locator("//input[@placeholder='Password']")
    password.fill(passcode)


def log(browser_context):
    logg = browser_context.locator("//label[normalize-space()='Login & Booking With OTP']")
    logg.click()


def confirm(browser_context):
    con = browser_context.locator("//button[normalize-space()='Proceed']")
    con.click()


def signin(browser_context):
    sign = browser_context.locator("//button[normalize-space()='SIGN IN']")
    sign.click()


def verify_log(browser_context):
    stat = browser_context.locator("//div[@class='loginError']")
    text = stat.text_content()
    assert "Bad" in text

