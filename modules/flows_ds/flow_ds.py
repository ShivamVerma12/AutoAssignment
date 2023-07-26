import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException


def ds_task(browser):
    task = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='New Task']")))
    task.click()

    pyautogui.press('enter')

    ds = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='selector-input selector--input aut-dataset-bar']")))
    ds.click()
    pyautogui.press('down')
    pyautogui.press('enter')


def connect(browser):
    ds = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='operator dataload']")))
    time.sleep(2)
    action_chains = ActionChains(browser)
    action_chains.click_and_hold(ds).move_by_offset(0, 150).release().perform()

    source = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@ class='connector-point'])[4]")))

    source.click()
    time.sleep(2)
    task = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class ='operator preprocessing']")))
    action_chains.move_to_element(task).perform()
    time.sleep(2)

    destination = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@ class='connector-point'])[1]")))
    time.sleep(2)
    action_chains.drag_and_drop(source, destination).perform()
    destination.click()

