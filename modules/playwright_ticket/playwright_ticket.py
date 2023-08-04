import time
from datetime import date, timedelta
import random
import string


def select_departure(browser_context, place):
    input_elem = browser_context.locator('//input[@id="departFrom"]')
    input_elem.click()
    input_elem.type(place)
    time.sleep(2)
    browser_context.keyboard.press("ArrowDown")
    browser_context.keyboard.press("Enter")


def select_arrival(browser_context, place):
    select = browser_context.locator("#goingTo")
    select.click()
    select.type(place)
    time.sleep(2)
    browser_context.keyboard.press("ArrowDown")
    browser_context.keyboard.press("Enter")


def select_date(browser_context):
    date_elements = browser_context.locator("(//a[@class='ui-state-default'])[15]")
    date_elements.click()


def search(browser_context):
    search_button = browser_context.locator("//button[normalize-space()='Search Bus']")
    search_button.click()


def first_result(browser_context):
    first = browser_context.locator("(//button[@type='button'][normalize-space()='Select Seat'])[1]")
    first.click()


def book_seat(browser_context):
    time.sleep(2)
    vacant_seat = browser_context.locator("(//span[contains(@class, 'Seating') and not(contains(@class, 'occupied'))])[1]")
    vacant_seat.click()
    vacant_seat = browser_context.locator("(//span[contains(@class, 'Seating') and not(contains(@class, 'occupied'))])[2]")
    vacant_seat.click()


def step(browser_context):
    board = browser_context.locator("(//input[@name='bordTime'])[1]")
    board.click()

    debard = browser_context.locator("(//input[@name='debordTime'])[1]")
    debard.click()

    proceed = browser_context.locator("//button[normalize-space()='Proceed to Book']")
    proceed.click()


def click_on_login(browser_context):
    guest = browser_context.locator("(//a[normalize-space()='Guest User Login'])[1]")
    guest.click()


def login(browser_context, email, mobil):
    time.sleep(1)
    mail = browser_context.locator("//input[@id='emailLogin']")
    mail.type(email)

    mobile = browser_context.locator("//input[@id='phoneLogin']")
    mobile.type(mobil)

    login_btn = browser_context.locator("(//button[@type='submit'][normalize-space()='Login'])[2]")
    login_btn.click()


def fill_details(browser_context, mobil, place, country):
    time.sleep(1)
    mobile = browser_context.locator("//input[@placeholder='Mobile Nunber']")
    mobile.type(mobil)

    address = browser_context.locator("//input[@placeholder='Address']")
    address.type(place)

    count = browser_context.wait_for_selector("//select[@name='country']")
    count.select_option(value=country)

    state_sel = browser_context.wait_for_selector('select[name="state"]')

    # Use the select_option() method to select an option by index
    state_sel.select_option(index=1)

    pin = browser_context.locator("//input[@placeholder='Pin Code']")
    random_number = random.randint(100000, 999999)
    pin.type(str(random_number))

    passenger1 = browser_context.locator("(//input[@placeholder='Traveller Name'])[1]")
    res = str(''.join(random.choices(string.ascii_letters, k=6)))
    passenger1.type(res)

    passenger2 = browser_context.locator("(//input[@placeholder='Traveller Name'])[2]")
    passenger2.type("random")

    gender1 = browser_context.wait_for_selector("(//select[@name='select'])[1]")
    gender1.select_option(index=2)

    age1 = browser_context.locator("(//input[@placeholder='Age'])[1]")
    age1.type("23")

    gender2 = browser_context.wait_for_selector("(//select[@name='select'])[2]")
    gender2.select_option(index=1)

    age2 = browser_context.locator("(//input[@placeholder='Age'])[2]")
    age2.type("24")


def book(browser_context):
    agree = browser_context.locator("//input[@id='agree']")
    agree.click()

    cont = browser_context.locator("//button[normalize-space()='Continue to Book']")
    cont.click()


def verify(browser_context):
    info_success_element = browser_context.locator("//p[@class='info-success']")
    assert info_success_element

