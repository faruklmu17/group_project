
def test_google_homepage(page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()