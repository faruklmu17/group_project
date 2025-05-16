from base_test import BaseTest

class TestExample(BaseTest):
    def testHello(self,page):
        page.goto(page)
        assert "Google" in page.title()