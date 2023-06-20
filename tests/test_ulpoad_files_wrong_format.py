from pytest_bdd import when, then, parsers
from modules.dataset.dataset import *

err = None


@when(parsers.parse('User uploads 2 files "{file1}" and "{file2}" in dataset "{dataset_name}" n wrong format'))
def step_def(cnvrg, file1, file2, dataset_name):
    global err
    err = upload_files_wrong_format(cnvrg, file1, file2, dataset_name)


@then(parsers.parse('User verifies by the exception raised "{error}"'))
def step_def(error):
    assert str(err) in error
