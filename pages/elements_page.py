from pages.base_page import BasePage


class ElementsPageLocators:
    LIST_CARDS = '//h5'


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


