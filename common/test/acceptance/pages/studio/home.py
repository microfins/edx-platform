"""
Home page for Studio when logged in.
"""
from bok_choy.page_object import PageObject

from common.test.acceptance.pages.studio import BASE_URL


class HomePage(PageObject):
    """
    Home page for Studio when logged in.
    """

    url = BASE_URL + "/home"

    def is_browser_on_page(self):
        self.wait_for_element_presence(
            '.page-header',
            'page header is present'
        )
        return 'Studio Home' == self.q(css='.page-header')[0].text
