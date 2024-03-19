import time

import allure

from pages.elements_page import ElementsPage

url = 'https://demoqa.com/'


@allure.epic('Elements Page.')
@allure.link('https://demoqa.com/elements')
class TestElementsPage:
    @allure.title('test_check_elements_page')
    def test_check_elements_page_opened(self, browser):
        page = ElementsPage(browser, url)
        page.open()
        page.click_elements()
        current_url = page.get_current_url()
        assert current_url == "https://demoqa.com/elements", 'Opened wrong page.'

    @allure.step('test_fill_all_fields')
    def test_fill_all_fields(self, browser):
        page = ElementsPage(browser, url)
        page.open()
        page.click_elements()
        page.click_text_box()
        entered_data = page.fill_all_fields()
        table_data = page.get_value_from_the_table()
        assert entered_data == table_data

    @allure.step('test_check_box')
    def test_check_box(self, browser):
        page = ElementsPage(browser, url)
        page.open()
        page.click_random_checkboxes()
        page.get_checked_checkboxes()


