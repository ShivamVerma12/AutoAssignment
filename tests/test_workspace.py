import pytest
from pytest_bdd import given, when, then, parsers
from modules.dataset.dataset import login
from modules.workspaces.workspaces import *
from modules.experiment.experiment import *


@pytest.mark.usefixtures("log_on_failure")
@given(parsers.parse('User login with login credentials email "{email}" and password "{password}"'))
def step_def(browser, email, password, log_on_failure):
    login(browser, email, password)


@when(parsers.parse('User creates a project "{project_name}"'))
def step_def(cnvrg, project_name, log_on_failure):
    create_project(cnvrg, project_name)


@when(parsers.parse('User create an workspace "{workspace_name}" in project "{project_name}"'))
def step_def(cnvrg, workspace_name, project_name, log_on_failure):
    create_workspace(cnvrg, workspace_name, project_name)


@then(parsers.parse('User verifies workspace "{workspace_name}" created or not in project "{project_name}"'))
def step_def(cnvrg, workspace_name, project_name, log_on_failure):
    assert verify_workspace(cnvrg, workspace_name, project_name)
