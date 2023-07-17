from pytest_bdd import given, when, then, parsers
from modules.dataset.dataset import login
from modules.experiment.experiment import *


@given(parsers.parse('User login with login credentials email "{email}" and password "{password}"'))
def step_def(browser, email, password):
    login(browser, email, password)


@when(parsers.parse('User creates a project "{project_name}"'))
def step_def(cnvrg, project_name):
    create_project(cnvrg, project_name)


@when(parsers.parse('User uploads a file "{file_name}" in project "{project_name}"'))
def step_def(cnvrg, file_name, project_name):
    upload_file(cnvrg, file_name, project_name)


@when(parsers.parse('User create an experiment "{experiment_name}" in project "{project_name}"'))
def step_def(cnvrg, project_name, experiment_name):
    create_experiment(cnvrg, project_name, experiment_name)


@then(parsers.parse('User verifies status code of experiment in project "{project_name}"'))
def step_def(cnvrg, project_name):
    assert verify_status(cnvrg, project_name)
