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
    import pdb
    pdb.set_trace()
    try:
        # Wait for the source and destination SVG elements to be clickable
        source = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class ='connector-wrapper output'])[2]")))

        destination = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class ='connector-wrapper input'])[1]")))

        # Perform the click action on the source SVG element
        source.click()

        # Create an ActionChains object to perform mouse actions
        action_chains = ActionChains(browser)

        try:
            # Drag and drop the source SVG element to the destination SVG element
            action_chains.drag_and_drop(source, destination).perform()
        except ElementNotInteractableException:
            destination.click()

    except TimeoutException as e:
        print("Timeout Exception: ", e)

    except Exception as e:
        print("Error: ", e)

    # ( //div[@ class ='connector-point'])[1]
    # ( // div[@ class ='connector-point'])[1]