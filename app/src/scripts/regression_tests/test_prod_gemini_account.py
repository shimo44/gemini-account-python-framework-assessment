"""
Author: Carl E Jones III
Title: Python-test suite for Gemini Account Web QA Testing
Date: 08/26/2021
Time: 4hrs(3 Development + 1 Troubleshooting)
License: Gemini QA Engineer Take Home Assessment, internal use only
"""
import unittest
from time import sleep
from resources.test_suites.gemini_create_account import GeminiAccountTestSuite


class TestGeminiCreateAccount(unittest.TestCase):

    def test_sandbox_login(self):
        print("Sandbox Login Test")
        self.account_tests = GeminiAccountTestSuite()

        self.account_tests.navigate_to_login()
        sleep(2)

        self.account_tests.verify_sandbox_page_elements()
        sleep(2)

        # self.account_tests.driver.browser.quit()

    def test_create_isr_account(self):
        print("Creating an Institution Client account Test")
        self.account_tests = GeminiAccountTestSuite()

        self.account_tests.navigate_to_login()
        sleep(2)

        self.account_tests.create_isr_account()
        sleep(2)

        self.account_tests.verify_isr_page_elements()

        self.account_tests.negative_lead_data_submission()
        # self.account_tests.passing_lead_data_submission()

        self.account_tests.driver.browser.quit()


def __main__():
    unittest.main()




