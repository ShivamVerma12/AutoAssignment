from pytest_bdd import parsers,when
from modules.flows_ds.flow_ds import *
from modules.dataset.dataset import create_dataset


@when(parsers.parse('User creates a empty Dataset "{ds}"'))
def step_def(cnvrg, ds):
    create_dataset(cnvrg, ds)


@when('User clicks on new task and choose data task')
def step_def(browser):
    ds_task(browser)


@when('User link Dataset task output with task input')
def step_def(browser):
    connect(browser)