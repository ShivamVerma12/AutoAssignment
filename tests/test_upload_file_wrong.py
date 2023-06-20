from pytest_bdd import when, then, parsers
from modules.dataset.dataset import *

err = None


@when(parsers.parse(
    'User uploads a file "{file_name}" which is not present in system in dataset "{dataset_name}"'))
def step_def(cnvrg, dataset_name, file_name):
    global err
    err = upload_file(cnvrg, dataset_name, file_name)


@then(parsers.parse('User verify the exception raised "{error}"'))
def step_def(error):
    assert str(err) in error
