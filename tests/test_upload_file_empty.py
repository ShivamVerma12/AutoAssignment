from pytest_bdd import when, then, parsers
from modules.dataset.dataset import *


@when(parsers.parse(
    'User uploads a file but enters empty strings instead of entering path of file in dataset "{dataset_name}"'))
def step_def(cnvrg, dataset_name):

    d = upload_file(cnvrg, dataset_name, "")
    import pdb
    pdb.set_trace()
    print(d)


@then('User verify the exception raised')
def step_def():
    pass
