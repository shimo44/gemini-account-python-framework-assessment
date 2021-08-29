class PasswordMgmt:
    def __init__(self, driver):
        self.url_forgot_password = "https://exchange.sandbox.gemini.com/signin/forgot?email="
        self.logo_gemini_brand = "//*[@id='gemini-logo-cyan_svg__Layer_1']"
        self.header_gemini_forgot_password = "//h1[contains(text(),'Forgot Password')]"

        self.text_password_reset_copy = "//span[contains(text(),'Please enter the email address associated with you')]"
        self.header_email_address_input = "//div[contains(text(),'Email Address')]"
        self.input_email_address = "//input[@data-testid='enterEmailInput']"
        self.cta_continue_button = "//button[@type='submit']"
        self.link_return_to_sign_in = "//a[@data-testid='returnToSignIn']"
        self.text_footer_copy = "//body/div[@id='container']/div[1]/div[1]/div[1]/footer[1]"

