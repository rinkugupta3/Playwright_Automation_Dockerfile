from playwright.sync_api import Page

def validate_page_title(page: Page, expected_title: str):
    assert page.title() == expected_title