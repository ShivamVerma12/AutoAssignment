from pytest_bdd import when, then, parsers
from modules.dataset.dataset import *


@when(parsers.parse('User removes a file "{file_name}" from dataset "{dataset_name}"'))
def step_def(cnvrg, file_name, dataset_name):
    remove_file(cnvrg, file_name, dataset_name)


@then(parsers.parse('User Verifies by file name "{file_name}" is present or not'))
def step_def(cnvrg, file_name):
    assert verify_file_name(cnvrg, file_name) == False
