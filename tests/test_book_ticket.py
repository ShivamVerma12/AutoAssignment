import parse
from pytest_bdd import given, when, then, parsers
from modules.ticket.ticket import *


@given("User open IRCTC website")
def step_def(browser):
    open_url(browser)


@when("User clicks on buses")
def step_def(browser):
    click_on_bus(browser)


@when(parsers.parse('User select departure from as "{place}"'))
def step_def(browser, place):
    select_departure(browser, place)


@when(parsers.parse('User select going to "{place}"'))
def step_def(browser, place):
    select_arrival(browser, place)


@when('User select Departure date after 15 days')
def step_def(browser):
    select_date(browser)


@when('Click on search bus')
def step_def(browser):
    search(browser)


@when('User select first search result')
def step_def(browser):
    first_result(browser)


@when('User select 2 seats')
def step_def(browser):
    book_seat(browser)


@when('User select departure and arrival time and click on process to book')
def step_def(browser):
    step(browser)


@when('User login as guest user')
def step_def(browser):
    click_on_login(browser)


@when(parsers.parse('User login with credential "{email}" mobile number "{mobil}"'))
def step_def(browser, email, mobil):
    login(browser, email, mobil)


@when(parsers.parse('User personal details "{mobil}" "{place}" "{country}"'))
def step_def(browser, mobil, place, country):
    fill_details(browser, mobil, place, country)


@when('User click on checkbox, continue to book')
def step_def(browser):
    book(browser)


@then('Verify OTP sent')
def step_def(browser):
    assert verify(browser)
