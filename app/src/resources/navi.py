"""
Author: Carl E Jones III
Title: Python-test suite for Gemini Account Web QA Testing
Date: 08/26/2021
Time: 4hrs(3 Development + 1 Troubleshooting)
License: Gemini QA Engineer Take Home Assessment, internal use only
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Navigator:
    def __init__(self):
        self.chrome_options = Options()
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=self.chrome_options)

    def goto(self, url):
        try:
            self.browser.get(url)
            print("Passed: " + "Navigating to url - " + str(url))
        except Exception as e:
            print("Failed: " + "Navigating to url - " + str(url))
            print(str(e))
            raise Exception

    def type_by_xpath(self, desc, xpath, user_input):
        try:
            element = self.browser.find_element_by_xpath(xpath)
            if element.is_displayed():
                element.send_keys(user_input)
            print("Passed: " + str(desc))
        except Exception as e:
            print("Failed: " + str(desc))
            print(str(e))
            raise Exception

    def click_by_xpath(self, desc, xpath):
        try:
            element = self.browser.find_element_by_xpath(xpath)

            if element.is_displayed():
                element.send_keys(Keys.DOWN)
                element.send_keys(Keys.DOWN)
                sleep(2)

                element.click()
            print("Passed: " + str(desc))
        except Exception as e:
            print("Failed: " + str(desc))
            print(str(e))
            raise Exception

    def click_in_dropdown_by_xpath(self, desc, xpath):
        try:
            element = self.browser.find_elements_by_xpath(xpath)

            # if element.is_displayed():
                # select = Select(element)
                #
                # select.select_by_visible_text(text)
                # sleep(2)
            action = ActionChains(self.browser)
            action.click(on_element=element[0]).perform()

            print("Passed: " + str(desc))
        except Exception as e:
            print("Failed: " + str(desc))
            print(str(e))
            raise Exception

    def verify_element_by_xpath(self, desc, xpath):
        try:
            element = self.browser.find_element_by_xpath(xpath)
            if element.is_displayed():
                print("Passed: Element Exists.." + str(desc))
        except Exception as e:
            print("Failed: Element is not loading as expected into application - " + str(desc))
            print(str(e))
            raise Exception

    def verify_element_is_missing_by_xpath(self, desc, xpath):
        try:
            element = self.browser.find_element_by_xpath(xpath)
            if element.is_displayed():
                print("Failed: Element is loading into the application - " + str(desc))
                raise Exception
        except Exception as e:
            print("Passed: Element Does Not Exist.." + str(desc))
            print(str(e))


