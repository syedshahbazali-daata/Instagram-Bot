import random
import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pickle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import datetime
import requests


##############################################################
def get_file_data(file):
    with open(file) as f:
        data = f.read()
        my_file_data = data.split('\n')

    return my_file_data


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
            try:
                now_text = type_message.split("\n")
                for single_word in now_text:
                    driver.find_element(By.XPATH, location_of_the_element).send_keys(single_word)
                    driver.find_element(By.XPATH, location_of_the_element).send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(random.randint(1, 4))
            except:
                driver.find_element(By.XPATH, location_of_the_element).send_keys(type_message)
            break
        except Exception as e:
            print(e)
            pass


def get_user_info():
    from uuid import getnode as get_mac
    get_inform = get_mac()
    alpha = requests.get(f"https://gettingusersinfo.shahbazshah.repl.co/{get_inform}")
    alpha_response = alpha.raise_for_status()


def specific_clicker(ele):
    while True:
        try:
            element = driver.find_element(By.XPATH, ele)
            webdriver.ActionChains(driver).move_to_element_with_offset(element, 1, 0).click(element).perform()

            break
        except Exception as e:
            # print(e)
            pass


def specific_clicker_with_direct(element):
    while True:
        try:

            webdriver.ActionChains(driver).move_to_element_with_offset(element, 1, 0).click(element).perform()

            break
        except Exception as e:
            print(e)
            pass


driver = uc.Chrome()
driver.get("https://www.instagram.com/")

cookies = pickle.load(open("cookies.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
specific_clicker("//button[text()='Not Now']")
# specific_clicker("//button[text()='Not Now']")
lets_stop = []


def time_go_next(add_time):
    ftr = [3600, 60, 1]

    a = sum([a * b for a, b in zip(ftr, map(int, add_time.split(':')))])

    limit = 0
    while True:
        if limit < a:
            limit += 1
            time.sleep(1)
            print(limit)
            print("bot 1")
        else:
            lets_stop.append(0)
            break


def auto_comment(enter_comment, post_url):
    driver.get(post_url)
    specific_clicker('//*[name()="svg" and @aria-label="Comment"]/../..')
    find_element_send_text('//textarea[@aria-label="Add a comment…"]', enter_comment)
    # find_element_send_text('//textarea[@aria-label="Add a comment…"]', Keys.ENTER)
    specific_clicker("//div[text()='Post']/..")


def auto_like():
    # driver.get(post_url)
    specific_clicker('//*[name()="svg" and @aria-label="Like"]/../..')


comments_list = ["Wow", "Nice..!", "Great", "Awesome"]

import random

comment = f"""
{random.choice(comments_list)}
"""


def explore_posts():
    def open_explorer():

        specific_clicker('//*[name()="svg" and @aria-label="Find People"]')
        driver.refresh()
        while True:
            try:

                all_posts = driver.find_elements(By.XPATH, '//main//div/a/..')[:5]
                # print(all_posts)
                if len(all_posts) > 1:
                    choose_post = random.choice(all_posts)
                    print(choose_post)
                    print(all_posts.index(choose_post))
                    print("---------------------")
                    break
                else:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            except Exception as e:
                print(e)
                pass
        specific_clicker_with_direct(choose_post)

    open_explorer()

    all_posts_links = get_file_data(r"instagram_links")

    current_link = 0

    loops = 0
    while True:
        loops += 1
        print(loops)
        click_range = random.randint(1, 12)
        print(click_range)

        time.sleep(2)
        while True:
            try:
                element = driver.find_element(By.XPATH, '//*[name()="svg" and @aria-label="Next"]')
                webdriver.ActionChains(driver).move_to_element_with_offset(element, 1, 0).click(element).perform()
                break
            except Exception as e:
                specific_clicker('//*[name()="svg" and @aria-label="Close"]/../..')
                driver.refresh()
                open_explorer()

        time.sleep(click_range)
        like_strategy = random.randint(1, 100)
        # like_strategy = random.randint(12, 21)
        if len(all_posts_links) < current_link:
            driver.quit()
            quit()
        if loops > 3 and len(all_posts_links) >= current_link:
            print("start")
            time.sleep(random.randint(10, 130))
            # time.sleep(random.randint(1, 20))
            print(all_posts_links[current_link])
            auto_comment(comment, all_posts_links[current_link])

            # auto_like()
            current_link += 1

            loops = 0
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            open_explorer()

        if 1 < like_strategy < 3:
            print("1-str")
            specific_clicker('//*[name()="svg" and @aria-label="Like"]/../..')
            specific_clicker('//*[name()="svg" and @aria-label="Close"]/../..')

            open_explorer()

        if 7 < like_strategy < 12:
            print("2-str")
            users = driver.find_elements(By.XPATH, '//span/a')
            user = random.choice(users)

            specific_clicker_with_direct(user)
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            specific_clicker('//*[name()="svg" and @aria-label="Find People"]')

            open_explorer()

        if 12 < like_strategy < 21:
            print("3-str")
            specific_clicker('//*[name()="svg" and @aria-label="Close"]')
            specific_clicker('//*[name()="svg" and @aria-label="Activity Feed"]')

            timer = random.randint(6, 13)
            time.sleep(timer)
            specific_clicker('//*[name()="svg" and @aria-label="Activity Feed"]')
            time.sleep(timer)
            specific_clicker('//*[name()="svg" and @aria-label="Messenger"]')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(timer)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            open_explorer()
        if 22 < like_strategy < 32:
            print("4-str")
            move_down = 400
            specific_clicker('//*[name()="svg" and @aria-label="Close"]/../..')
            specific_clicker('//*[name()="svg" and @aria-label="Home"]')
            for scroll_down in range(0, random.randint(10, 20)):
                driver.execute_script(f"window.scrollTo(0, {move_down})")
                move_down += random.randint(230, 400)
                time.sleep(random.randint(2, 5))

            open_explorer()
        print(datetime.datetime.now())


explore_posts()
