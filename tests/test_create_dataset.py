from pytest_bdd import when, then, parsers, given
from modules.dataset.dataset import *


# @given(parsers.parse('User login with login credentials email "{email}" nad password "{password}"'))
# def step_def(browser, email, password):
#     login(browser, email, password)


@when(parsers.parse('User create dataset with name "{dataset_name}"'))
def step_def(dataset_name, cnvrg):
    create_dataset(cnvrg, dataset_name)


@then(parsers.parse('User verify title name of dataset "{title}"'))
def step_def(cnvrg, title):
    dataset = cnvrg.datasets.get(title)
    assert dataset.title == title
