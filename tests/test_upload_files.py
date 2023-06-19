from pytest_bdd import when, then, parsers
from modules.dataset.dataset import *


@when(parsers.parse('User uploads 2 files "{file1}" and "{file2}" in dataset "{dataset_name}"'))
def step_def(cnvrg, dataset_name, file1, file2):
    upload_files(cnvrg, dataset_name, file1, file2)


@then(parsers.parse('User verifies by file count in dataset "{dataset_name}"'))
def step_def(cnvrg, dataset_name):
    assert count_file(cnvrg, dataset_name) == 2
