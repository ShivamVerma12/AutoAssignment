from pytest_bdd import given, when, then, parsers
from modules.playwright_ticket.playwright_ticket import *


@when(parsers.parse('User select departure from as "{place}"'))
def step_def(browser_context, place):
    select_departure(browser_context, place)

@when(parsers.parse('User select going to "{place}"'))
def step_def(browser_context, place):
    select_arrival(browser_context, place)


@when('User select Departure date after 15 days')
def step_def(browser_context):
    select_date(browser_context)


@when('Click on search bus')
def step_def(browser_context):
    search(browser_context)


@when('User select first search result')
def step_def(browser_context):
    first_result(browser_context)


@when('User select 2 seats')
def step_def(browser_context):
    book_seat(browser_context)


@when('User select departure and arrival time and click on process to book')
def step_def(browser_context):
    step(browser_context)


@when('User login as guest user')
def step_def(browser_context):
    click_on_login(browser_context)


@when(parsers.parse('User login with credential "{email}" mobile number "{mobil}"'))
def step_def(browser_context, email, mobil):
    login(browser_context, email, mobil)


@when(parsers.parse('User personal details "{mobil}" "{place}" "{country}"'))
def step_def(browser_context, mobil, place, country):
    fill_details(browser_context, mobil, place, country)


@when('User click on checkbox, continue to book')
def step_def(browser_context):
    book(browser_context)


@then('Verify OTP sent')
def step_def(browser_context):
    verify(browser_context)