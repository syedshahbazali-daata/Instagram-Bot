import pickle
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By

username = ""
password = ""


#############################################

driver = uc.Chrome()
driver.get("https://www.instagram.com/accounts/login/?hl=en")


def find_element_click(location_of_the_element):
    """
    :param location_of_the_element: XPATH of te any web element.
    :return: Find element until it present on webpage and click on it.
    """
    while True:
        try:
            driver.find_element(By.XPATH, location_of_the_element).click()
            break
        except Exception as e:
            # print(e)
            pass


def find_element_send_text(location_of_the_element, type_message):
    """
        :param location_of_the_element: XPATH of te any web element.
        :return: Find element until it present on webpage and click on it.
        """
    while True:
        try:
            driver.find_element(By.XPATH, location_of_the_element).send_keys(type_message)
            break
        except Exception as e:
            # print(e)
            pass


def specific_clicker(ele):
    while True:
        try:
            element = driver.find_element(By.XPATH, ele)
            webdriver.ActionChains(driver).move_to_element_with_offset(element, 1, 0).click(element).perform()

            break
        except Exception as e:
            # print(e)
            pass


find_element_send_text("(//input)[1]", username)
find_element_send_text("(//input)[2]", password)
find_element_click("//div[text()='Log In']/..")
# //*[name()="svg" and @aria-label="Home"]
specific_clicker('//*[name()="svg" and @aria-label="Home"]')
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
driver.quit()
print("Thanks Now you can run the Bot...!")
