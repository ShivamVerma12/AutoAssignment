import allure
import pytest

from helper.helper import browser


@pytest.fixture()
def log_on_failure(browser, request):
    yield
    item = request.node
    if hasattr(item, 'rep_call') and item.rep_call.failed:
        ss = browser.get_screenshot_as_file("screenshot.png")
        allure.attach.file(ss, name="screenshot", attachment_type=allure.attachment_type.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
