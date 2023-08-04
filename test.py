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
from tests.test_flows import *
from tests.test_flow_ds import *
from tests.test_playwright_login import *
from tests.test_playwright_ticket import *

# scenarios('feature_file/datasets.feature')
# scenarios('feature_file/experiment.feature')
# scenarios('feature_file/workspace.feature')
# scenarios('feature_file/flows.feature')
# scenarios('feature_file/flows_ds.feature')
# scenarios('feature_file/playwright_login.feature')
scenarios('feature_file/playwright_ticket.feature')