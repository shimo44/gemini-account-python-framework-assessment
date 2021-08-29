"""
Author: Carl E Jones III
Title: Python-test suite for Gemini Account Web QA Testing
Date: 08/26/2021
Time: 4hrs(3 Development + 1 Troubleshooting)
License: Gemini QA Engineer Take Home Assessment, internal use only
"""
class CreateAnAccount:
    def __init__(self):
        # Regular Account Creation #
        self.url_create_an_account_regular = "https://exchange.sandbox.gemini.com/register#"
        self.logo_gemini_brand = "//*[@id='gemini-logo-cyan_svg__Layer_1']"

        self.header_gemini_create_an_account_regular = "//h1[contains(text(),'Create an account')]"
        self.text_create_an_account_copy = "//h6[contains(text(),'Please enter your name as it appears on official d')]"

        self.header_input_first_name = ""
        self.input_first_name = ""
        self.header_input_middle_name = ""
        self.input_middle_name = ""
        self.header_input_last_name = ""
        self.input_last_name = ""
        self.header_input_email_address = ""
        self.input_email_address = "//body/div[@id='container']/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/form[1]/label[1]/div[2]/input[1]"
        self.header_input_password = ""
        self.input_password = "//body/div[@id='container']/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/form[1]/label[2]/div[2]/input[1]"

        self.toggle_visible_password_eyeball = "//body/div[@id='container']/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/form[1]/label[2]/div[2]/span[1]/a[1]"

        self.text_agree_to_ua_and_privacy_policy = "//span[contains(text(),'Remember my email address')]"
        self.radio_agree_to_ua_and_privacy_policy = """//input[@name='rememberEmail']"""
        self.link_user_agreement = ""
        self.link_privacy_policy = ""

        self.cta_sign_in_button = """//button[@type='submit']"""

        self.overlay_cookie_use_options = "//div[@id='cookiePolicyAgreement']"
        self.cta_overlay_cookie_use_ok = "//a[@data-testid='cookiePolicyAgreement-close']"

        self.link_account_sign_in = ""
        self.link_create_a_business_account = "//a[@data-testid='register-go-to-institution-register']"

        # Business Account Creation #
        self.url_create_an_account_institution = "https://exchange.sandbox.gemini.com/register/institution"

        self.icr_logo_gemini_brand = "//img[@alt='Gemini']"
        self.icr_header_gemini_create_an_account_institution = "//h3[contains(text(),'Institutional Client Registration')]"
        self.icr_text_create_an_account_copy_1 = "//p[contains(text(),'Welcome to Gemini! We are working hard to make Gem')]"
        self.icr_text_create_an_account_copy_2 = "//p[contains(text(),'Multiple people within an organization can registe')]"
        self.icr_text_create_an_account_copy_3 = "//p[contains(text(),'Upon completion, your information will be reviewed')]"
        self.icr_link_join_an_existing_institutional_account = "//a[@href='/register?type=institution']"

        self.icr_header_company_information = "//h5[contains(text(),'Company Information')]"
        self.icr_header_input_legal_business_name = "//div[contains(text(),'Legal Business Name')]"
        self.icr_input_legal_business_name = "//input[@name='company.legalName']"
        self.icr_header_dropdown_company_type = "//div[contains(text(),'Company type')]"
        self.icr_dropdown_company_type = "//div[@class='companyTypeDropdown css-2b097c-container']"
        # self.icr_dropdown_company_type = "//body/div[@id='container']/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/fieldset[1]/div[1]/div[2]/label[1]/div[2]/div[1]/div[1]"
        self.icr_dropdown_company_type_publicly_traded = "//*[text()='Publicly-traded Company']"

        self.icr_header_company_location = "//h5[contains(text(),'Company Location')]"
        self.icr_header_dropdown_country_of_business = "//div[contains(text(),'Country of Business')]"
        self.icr_dropdown_country_of_business = "//div[@class=' css-jbc2k3-control']"
        self.icr_dropdown_country_of_business_japan = "//*[text()='Japan']"
        self.icr_header_dropdown_state = "//body/div[@id='container']/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/fieldset[2]/div[1]/div[2]/label[1]/div[1]"
        self.icr_dropdown_state = "//div[@class='usStateDropdown css-2b097c-container']"

        self.icr_header_personal_information = "//body/div[@id='container']/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/span[1]/fieldset[1]/h5[1]"
        self.icr_header_input_legal_first_name = "//div[contains(text(),'Legal First Name')]"
        self.icr_input_first_name = "//body/div[@id='container']/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/span[1]/fieldset[1]/div[1]/div[1]/label[1]/div[2]/input[1]"
        self.icr_header_input_middle_name = "//body/div[@id='container']/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/span[1]/fieldset[1]/div[2]/div[1]/label[1]/div[2]"
        # self.icr_input_middle_name = "(//div[@class='css-79elbk e5i1odf0'])[3]"
        self.icr_input_middle_name = "//body/div[@id='container']/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/span[1]/fieldset[1]/div[1]/div[2]/label[1]/div[2]/input[1]"
        self.icr_header_input_last_name = "//div[contains(text(),'Legal Last Name')]"
        self.icr_input_last_name = "//input[@name='personal.legalName.lastName']"
        self.icr_header_input_email_address = "//div[contains(text(),'Your Email Address')]"
        # self.icr_input_email_address = "(//div[@class='css-79elbk e5i1odf0'])[5]"
        self.icr_input_email_address = "//input[@name='personal.email']"

        self.icr_text_submission_policy_copy = "//p[contains(text(),'Once submitted, a dedicated account representative')]"

        self.cta_sign_in_button = "//button[@type='submit']"

