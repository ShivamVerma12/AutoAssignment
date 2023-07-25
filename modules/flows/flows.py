import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui


def flows(browser):
    proj = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='project']")))
    proj.click()

    flow = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Flows']")))
    flow.click()


def create_flow(browser):
    create = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='New Flow']")))
    create.click()


def create_task(browser):
    task = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='New Task']")))
    task.click()

    pyautogui.press('down')
    pyautogui.press('enter')


def new_task(browser, cmd):
    task = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter a command or search…']")))
    task.click()

    pyautogui.typewrite(cmd)
    pyautogui.press('enter')


def save(browser):
    save_changes = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save Changes']")))
    save_changes.click()


def run(browser):
    run_task = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@class='action-button run-button']")))

    run_task.click()

    runtask = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Run']")))
    runtask.click()


def verify(browser):
    status = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//td[@data-column='state'][1]"))).text

    stat = False
    while True:
        if status.lower() == 'debug':
            stat = True
            break
        elif status.lower() == 'error':
            stat = False
            break

        # If the status is neither 'debug' nor 'error', continue waiting and update the status
        status = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[@data-column='state'][1]"))).text

    assert stat

