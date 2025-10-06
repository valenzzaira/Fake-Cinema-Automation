from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage



class SelectShowTime(BasePage):
    """ Selección de día y horario"""

    #  Locators

    DIA_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[2]/button[4]")
    HORARIO_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[2]/div[1]/div[1]/a[3]/button[1]")

    def __init__(self, driver):
        super().__init__(driver)


    def wait_for_title_and_click(self):
        self.element_is_visible(self.DIA_BUTTON)
        self.click(self.DIA_BUTTON)



    def scroll_to_horarios(self):
        self.scroll_to_element(self.HORARIO_BUTTON)
        self.element_is_visible(self.HORARIO_BUTTON)

    def wait_and_click(self):
        self.scroll_to_horarios()
        self.click(self.HORARIO_BUTTON)

    def select_day(self):
        """Selecciona el día """
        self.wait_for_title_and_click()
        print("seleccionando dia...")

    def select_showtime(self):
        """Selecciona el horario """
        self.wait_and_click()
        print("seleccionando horario...")