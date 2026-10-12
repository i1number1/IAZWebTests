from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    SHOW_PASSWORD_BUTTON = (By.XPATH, '//button[.//span="Показать пароль"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@data-test-id="enter-action"]')
    QR_CODE_BUTTON = (By.XPATH, '//button[@label="Войти по QR-коду"]')
    REGISTRATION_BUTTON = (By.XPATH, '//*[@data-test-id="registration-action"]')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//button[@data-test-id="forgot-password-link"]')
    LOG_IN_VIA_VK = (By.XPATH, '//a[@title="Войти через VK ID"]')
    LOG_IN_VIA_MAIL = (By.XPATH, '//a[@title="Войти через Почту"]')
    LOG_IN_VIA_GOOGLE = (By.XPATH, '//a[@title="Войти через Google"]')
    LOG_IN_VIA_YANDEX = (By.XPATH, '//a[@title="Войти через Яндекс"]')
    LOG_IN_VIA_APPLE = (By.XPATH, '//a[@title="Войти через Apple"]')
    QR_CODE_TAB = (By.XPATH, '//a[@data-l="t,qr_tab"]')

class LoginPageHelper(BasePage):
    pass