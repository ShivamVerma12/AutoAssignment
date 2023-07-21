import string
import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, timedelta
import time
import pyautogui


def click_on_elem(browser, by_locator: object, sec=10):
    element = WebDriverWait(browser, sec).until(EC.element_to_be_clickable(by_locator))
    element.click()
    return element


def open_url(browser):
    browser.get("https://www.irctc.co.in/")


def click_on_bus(browser):
    wait = WebDriverWait(browser, 20)
    bus = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".railDrishti.fa.fa-bus")))
    bus.click()


def select_departure(browser, place):
    main_window_handle = browser.current_window_handle  # Get the handle of the main window
    all_window_handles = browser.window_handles  # Get handles of all open windows

    # Find the handle of the new window by comparing handles
    new_window_handle = None
    for window_handle in all_window_handles:
        if window_handle != main_window_handle:
            new_window_handle = window_handle
            break

    # Switch to the new window
    browser.switch_to.window(new_window_handle)
    locator = By.XPATH, "//input[@id='departFrom']"
    # select = click_on_elem(browser, locator, 10)
    select = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(locator))
    select.click()
    time.sleep(1)
    select.send_keys(place)
    time.sleep(2)
    pyautogui.press('down')
    pyautogui.press('enter')



def select_arrival(browser, place):
    select = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#goingTo")))
    select.click()
    time.sleep(1)
    select.send_keys(place)
    time.sleep(2)
    pyautogui.press('down')
    time.sleep(2)
    pyautogui.press('enter')


def select_date(browser):
    today = date.today()
    future_date = today + timedelta(days=10)
    # Find all the clickable date elements inside the calendar
    date_elements = browser.find_elements(By.XPATH, ".//a[@class='ui-state-default']")

    # Iterate through each date element and check if it matches the desired date
    for date_element in date_elements:
        # Get the date text (e.g., '1', '2', ..., '31') from the date element
        date_text = date_element.text

        # If the date text matches the desired date, click on it to select the date
        if date_text == str(future_date.day):
            date_element.click()
            break  # Break the loop once the date is selected


def search(browser):
    search_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Search Bus']")))

    search_button.click()


def first_result(browser):
    first = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][normalize-space()='Select Seat'])[1]")))
    first.click()


def book_seat(browser):
    time.sleep(3)

    vacant_seats = browser.find_elements(By.XPATH,"//span[contains(@class, 'Seating') and not(contains(@class, 'occupied'))]")
    print(vacant_seats)
    print(len(vacant_seats))
    time.sleep(2)

    vacant_seats[0].click()
    vacant_seats[4].click()

    # else:
    #     print("No Vacant seat")


def step(browser):
    board = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH,"(//input[@name='bordTime'])[1]")))
    board.click()

    debard = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@name='debordTime'])[1]")))
    debard.click()

    proceed = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Proceed to Book']")))
    proceed.click()


def click_on_login(browser):
    guest = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//a[normalize-space()='Guest User Login'])[1]")))
    guest.click()


def login(browser, email, mobil):
    time.sleep(2)
    mail = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='emailLogin']")))
    mail.send_keys(email)

    mobile = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phoneLogin']")))
    mobile.send_keys(mobil)

    login_btn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//button[@type='submit'][normalize-space()='Login'])[2]")))
    login_btn.click()


def fill_details(browser, mobil, place, country):
    mobile = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Mobile Nunber']")))
    mobile.send_keys(mobil)

    address = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Address']")))
    address.send_keys(place)

    count = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@name='country']")))

    slect = Select(count)
    slect.select_by_value(country)

    state_sel = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@name='state']")))

    select = Select(state_sel)
    select.select_by_index(1)

    pin = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Pin Code']")))
    random_number = random.randint(100000, 999999)
    pin.send_keys(random_number)

    passenger1 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Traveller Name']")))
    res = str(''.join(random.choices(string.ascii_letters, k=6)))
    passenger1.send_keys(res)

    passenger2 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Traveller Name'])[2]")))
    passenger2.send_keys("random")

    gender1 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//select[@name='select'])[1]")))
    gender1_sel = Select(gender1)
    gender1_sel.select_by_index(2)

    age1 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Age'])[1]")))
    age1.send_keys("23")

    time.sleep(2)
    # passenger2 = WebDriverWait(browser, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-9']//div[1]//div[4]//input[1]")))
    # passenger2.send_keys(res)

    gender2 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//select[@name='select'])[2]")))
    gender2_sel = Select(gender2)
    gender2_sel.select_by_index(2)

    age2 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Age'])[2]")))
    age2.send_keys("24")


def book(browser):
    agree = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='agree']")))
    agree.click()

    cont = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Continue to Book']")))
    cont.click()


def verify(browser):
    info_success_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH,"//p[@class='info-success']")))
    if info_success_element:
        return True
    else:
        return False
