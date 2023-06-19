from pytest_bdd import when, then, parsers
from modules.dataset.dataset import *


@when(parsers.parse('User upload file "{file_name}" in dataset "{dataset_name}"'))
def step_def(cnvrg, dataset_name, file_name):
    upload_file(cnvrg, dataset_name, file_name)


@then(parsers.parse('User verify file name uploaded in dataset "{file_name}"'))
def step_def(cnvrg, file_name):
    assert verify_file_name(cnvrg, file_name)
