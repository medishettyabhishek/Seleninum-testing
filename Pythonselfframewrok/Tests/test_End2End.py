
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass


class testone(BaseClass):

     def test_End2End(self):
         products = self.driver.find_elements_by_css_selector("div[class='card h-100']")
         for product in products:
            Productname = product.find_element_by_xpath("div/h4/a").text
            if Productname == "Blackberry":
                product.find_element_by_xpath("div/button").click()

            self.driver.find_element_by_class_name("btn-primary").click()
            self.driver.find_element_by_class_name("btn-success").click()

            self.driver.find_element_by_id("country").send_keys('ind')

            wait = WebDriverWait(self.driver, 7)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
            self.driver.find_element_by_link_text("India").click()

            self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
            self.driver.find_element_by_css_selector("input[type='submit']").click()

            textmessage = self.driver.find_element_by_css_selector(".alert-success").text

            assert "Success!" in textmessage

            self.driver.get_screenshot_as_file("abhishek.png")
