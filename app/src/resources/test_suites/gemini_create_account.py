"""
Author: Carl E Jones III
Title: Python-test suite for Gemini Account Web QA Testing
Date: 08/26/2021
Time: 4hrs(3 Development + 1 Troubleshooting)
License: Gemini QA Engineer Take Home Assessment, internal use only
"""
from resources.applications.gemini_account.page_objects.sign_in import SignIn
from resources.applications.gemini_account.page_objects.register import CreateAnAccount
from resources.navi import Navigator

import unittest

global driver
global sign_in
global create_account


class GeminiAccountTestSuite(unittest.TestCase):
    driver = Navigator()
    sign_in = SignIn()
    create_account = CreateAnAccount()

    def navigate_to_login(self):
        try:
            self.driver.goto(self.sign_in.url_sign_in)
            assert True
        except Exception as e:
            print(str(e))
            assert False

    def verify_sandbox_page_elements(self):
        try:
            self.driver.verify_element_by_xpath("Verifying - Gemini Brand Logo -is loading as expected into application.",
                                                self.sign_in.logo_gemini_brand)
            assert True
        except Exception as e:
            print(str(e))
            assert False

        try:
            self.driver.verify_element_by_xpath("Verifying - Sandbox Header - is loading as expected into application.",
                                                self.sign_in.header_gemini_sandbox_login)
            assert True
        except Exception as e:
            print(str(e))
            assert False

        try:
            self.driver.verify_element_by_xpath("Verifying - Sandbox purpose tooltip - is loading as expected into application.",
                                                self.sign_in.tooltip_sandbox_login_purpose)
            assert True
        except Exception as e:
            print(str(e))
            assert False

        try:
            self.driver.verify_element_by_xpath("Verifying - Email Address Input Field - is loading as expected into application.",
                                                self.sign_in.input_email_address)
            assert True
        except Exception as e:
            print(str(e))
            assert False

        try:
            self.driver.verify_element_by_xpath("Verifying - Password Input Field - is loading as expected into application.",
                                                self.sign_in.input_password)
            assert True
        except Exception as e:
            print(str(e))
            assert False

        try:
            self.driver.verify_element_is_missing_by_xpath("Verifying - Email Address Missing - error subtext is not loading into application.",
                                                self.sign_in.error_email_address_not_entered)
            assert True
        except Exception as e:
            print(str(e))
            assert False

    def create_isr_account(self):
        try:
            self.driver.click_by_xpath("Clicking - Create new account link..",
                                       self.sign_in.link_create_new_account)
            assert True
        except Exception as e:
            print(str(e))
            assert False

        try:
            self.driver.click_by_xpath("Clicking - OK for allowing site cookies..",
                                       self.create_account.cta_overlay_cookie_use_ok)
            assert True
        except Exception as e:
            print(str(e))
            assert False

        try:
            self.driver.click_by_xpath("Clicking - Create a business account link..",
                                       self.create_account.link_create_a_business_account)
            assert True
        except Exception as e:
            print(str(e))
            assert False


    def verify_isr_page_elements(self):
        try:
            self.driver.verify_element_by_xpath(
                "Verifying - ISR Gemini Logo - is loading as expected into application.",
                self.create_account.icr_logo_gemini_brand)
            assert True
        except Exception as e:
            print(str(e))
            assert False

    def negative_lead_data_submission(self):
        try:
            self.driver.type_by_xpath("Typing - Legal Business Name..",
                                       self.create_account.icr_input_legal_business_name, "Testoro Enterprises")
            assert True
        except Exception as e:
            print(str(e))
            assert False

        try:
            self.driver.click_in_dropdown_by_xpath("Opening - Company Type..",
                                       self.create_account.icr_dropdown_company_type)
            assert True
        except Exception as e:
            print(str(e))
            assert False

        try:
            self.driver.click_in_dropdown_by_xpath("Selecting - Company Type..",
                                       self.create_account.icr_dropdown_company_type_publicly_traded)
            assert True
        except Exception as e:
            print(str(e))
            assert False

        try:
            self.driver.click_in_dropdown_by_xpath("Selecting - Country of Business..",
                                                   self.create_account.icr_dropdown_country_of_business)
            assert True

        except Exception as e:
            print(str(e))
            assert False

        # try: #FIXME: Ran into issue with a valid selector for accessing values within dropdowns due to imlementation as Div vs Option or Selector
        #     self.driver.click_in_dropdown_by_xpath("Selecting - Country of Japan..",
        #                                            self.create_account.icr_dropdown_country_of_business_japan)
        #     assert True
        #
        # except Exception as e:
        #     print(str(e))
        #     assert False

        try:
            self.driver.type_by_xpath("Typing - legal first name..",
                                       self.create_account.icr_input_first_name, "Testoro")
            assert True
        except Exception as e:
            print(str(e))
            assert False

        try:
            self.driver.type_by_xpath("Typing - legal last name..",
                                       self.create_account.icr_input_last_name, "Nakamoto")
            assert True
        except Exception as e:
            print(str(e))
            assert False

        try:
            self.driver.type_by_xpath("Typing - email address..",
                                       self.create_account.icr_input_email_address, "dummylead8@cj.com")
            assert True
        except Exception as e:
            print(str(e))
            assert False

        try:
            self.driver.click_by_xpath("Clicking - Continue submission button..",
                                       self.create_account.cta_sign_in_button)
            assert True
        except Exception as e:
            print(str(e))
            assert False

    def passing_lead_data_submission(self):
        #FIXME: Unfinished due to selector issue for dropdown content in form
        pass



