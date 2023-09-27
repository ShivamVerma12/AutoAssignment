from pytest_bdd import scenarios
from tests.test_create_dataset import *
from helper.helper import *
from tests.test_file_dataset import *
from tests.test_upload_file_wrong import *
from tests.test_upload_files import *
from tests.test_remove_file import *
from tests.test_ulpoad_files_wrong_format import *
from tests.test_experiment import *
from tests.test_workspace import *

# scenarios('feature_file/datasets.feature')
# scenarios('feature_file/experiment.feature')
scenarios('feature_file/workspace.feature')


