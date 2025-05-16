from BaseTest import BaseTest

class TestExample(BaseTest):
    def testHello(self,page):
        page.goto("https://www.google.com/")
        assert "Google" in page.title()