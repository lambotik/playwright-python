from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, link: str):
        self.page = page
        self.link = link

    def open(self):
        print('OPEN', self.link)
        return self.page.goto(self.link)

    def get_current_url(self):
        print(f'Current url: {self.page.url}')
        return self.page.url

    def click(self, locator: str):
        return self.page.locator(locator).click()

    def element_is_visible(self, locator):
        return self.page.wait_for_selector(locator)
