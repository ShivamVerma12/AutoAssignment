from pytest_bdd import when, then, parsers, given
from modules.flows.flows import *
from modules.experiment.experiment import *
from modules.dataset.dataset import login


@given(parsers.parse('User login with login credentials email "{email}" and password "{password}"'))
def step_def(browser, email, password):
    login(browser, email, password)


@when(parsers.parse('User creates a project "{project_name}"'))
def step_def(cnvrg, project_name):
    create_project(cnvrg, project_name)


@when(parsers.parse('User uploads a file "{file_name}" in project "{project_name}"'))
def step_def(cnvrg, file_name, project_name):
    upload_file(cnvrg, file_name, project_name)


@when('User clicks on flow')
def step_def(browser):
    flows(browser)


@when('User creates a new flow')
def step_def(browser):
    create_flow(browser)


@when('User clicks on new task and choose custom task')
def step_def(browser):
    create_task(browser)


@when(parsers.parse('User enters command "{cmd}"'))
def step_def(browser, cmd):
    new_task(browser, cmd)


@when('Users click on save changes')
def step_def(browser):
    save(browser)


@when('User click on run')
def step_def(browser):
    run(browser)


@then('User verify status')
def step_def(browser):
    verify(browser)
