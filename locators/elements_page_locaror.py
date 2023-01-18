from selenium.webdriver.common.by import By

class TextBoxPageLocators:

    # FULL_NAME = (By.CSS_SELECTOR,"input[id='userName']")
    FULL_EMAIL = (By.CSS_SELECTOR,"input #email ")
    FULL_PASSWORD = (By.CSS_SELECTOR,"input[id='pass']")
    # CURRENT_ADDRESS = (By.CSS_SELECTOR,"input[id='currentAddress']")
    # PERMAMENT_ADDRESS = (By.CSS_SELECTOR,"input[id='permamentAddress']")
    SUBMIT_IF_HAVE = (By.LINK_TEXT, "value=['У меня уже есть аккаунт']")
    SUBMIT = (By.LINK_TEXT, "value=['Вход']")


    CREATED_FULL_NAME = (By.CSS_SELECTOR,'#output # name')
    CREATED_EMAIL = (By.CSS_SELECTOR,"'#output # Email'")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR,"input[id='currentAddress']")
    CREATED_PERMAMENT_ADDRESS =(By.CSS_SELECTOR,"output #permamentAdderess")