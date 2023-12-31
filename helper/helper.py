import os

import pytest
from cnvrgv2 import Cnvrg
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os


@pytest.fixture()
def cnvrg():
    cnvrgvar = Cnvrg(domain=os.environ.get('URL'),
                     email="test@mailinator.com",
                     password="123456",
                     )
    yield cnvrgvar


@pytest.fixture()
def browser():
    chromedriver = "/usr/local/bin/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(chromedriver)
    driver = webdriver.Chrome(service=service, options=options)  # instance of Webdriver
    yield driver

