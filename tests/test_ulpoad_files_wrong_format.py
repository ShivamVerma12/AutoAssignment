from pytest_bdd import when, then, parsers
from modules.dataset.dataset import *


@when(parsers.parse('User uploads 2 files "{file1}" and "{file2}" in dataset "{dataset_name}" n wrong format'))
def step_def(cnvrg, file1, file2, dataset_name):
    d = upload_files_wrong_format(cnvrg, file1, file2, dataset_name)
    import pdb
    pdb.set_trace()
    print(d)


@then('User verifies by the exception raised')
def step_def():
    # assert upload_files_wrong_format(cnvrg, file1, file2, dataset_name) ==
    pass