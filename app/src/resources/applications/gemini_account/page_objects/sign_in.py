"""
Author: Carl E Jones III
Title: Python-test suite for Gemini Account Web QA Testing
Date: 08/26/2021
Time: 4hrs(3 Development + 1 Troubleshooting)
License: Gemini QA Engineer Take Home Assessment, internal use only
"""
class SignIn:
    def __init__(self):
        self.url_sign_in = "https://exchange.sandbox.gemini.com/signin"
        self.logo_gemini_brand = "//*[@id='gemini-logo-cyan_svg__Layer_1']"
        self.header_gemini_sandbox_login = "//h1[contains(text(),'Gemini sandbox')]"
        self.tooltip_sandbox_login_purpose = "//body/div[@id='container']/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]"
        self.input_email_address = "//body/div[@id='container']/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/form[1]/label[1]/div[2]/input[1]"
        self.input_password = "//body/div[@id='container']/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/form[1]/label[2]/div[2]/input[1]"

        self.error_email_address_not_entered = "//body/div[@id='container']/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/form[1]/label[1]/div[3]"

        self.toggle_visible_password_eyeball = "//body/div[@id='container']/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/form[1]/label[2]/div[2]/span[1]/a[1]"

        self.text_remember_email_address = "//span[contains(text(),'Remember my email address')]"
        self.radio_remember_email_address = """//input[@name='rememberEmail']"""
        self.cta_sign_in_button = """//button[@type='submit']"""

        self.link_create_new_account = """//a[@data-testid='goToRegister']"""
        self.link_reset_your_password = "//a[@data-testid='goToResetPassword']"
