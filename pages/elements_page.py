import random
import time

from pages.base_page import BasePage


class ElementsPageLocators:
    LIST_CARDS = '//h5'
    CHECKBOXES = '//span[@class="rct-title"]'
    EXPAND_ALL = '//button[@title="Expand all"]'
    CHECKED_ITEMS = 'svg[class="rct-icon rct-icon-check"]'
    TITLE_LIST_TEXT = '//span[@class="rct-title"]'



class ElementsPage(BasePage):
    locators = ElementsPageLocators()

    def click_elements(self):
        self.page.get_by_text('Elements').click()

    def click_text_box(self):
        self.page.get_by_text('Text Box').click()

    def fill_all_fields(self):
        name = 'Dima'
        self.page.locator('//input[@id="userName"]').fill(name)
        email = 'lambotik@mail.ru'
        self.page.locator('//input[@id="userEmail"]').fill(email)
        cur_address = 'Vulica'
        self.page.locator('//textarea[@id="currentAddress"]').fill(cur_address)
        per_address = 'Permanent address'
        self.page.locator('//textarea[@id="permanentAddress"]').fill(per_address)
        self.page.click('//button[@id="submit"]')
        return [name, email, cur_address, per_address]

    def get_value_from_the_table(self):
        table_list = self.page.locator('//div[@id="output"]//p').all()
        ls = []
        for x in table_list:
            ls.append(x.text_content().rstrip(' ').split(':')[-1])
        return ls

    def click_random_checkboxes(self):
        self.click_elements()
        self.page.get_by_text('Check Box').click()
        self.click(self.locators.EXPAND_ALL)
        list_checkboxes = self.page.locator(self.locators.CHECKBOXES).all()
        for i in range(20):
            random_index = random.randint(1, 16)
            list_checkboxes[random_index].click()

    def get_checked_checkboxes(self):
        data = {}
        for c in self.page.locator(self.locators.CHECKED_ITEMS).all():
            print(c)



