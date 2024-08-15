#Run test with following command line:
#(venv) PS C:\Users\dhira\Desktop\Dhiraj HP Laptop\Projects\Playwright_Automation_DesignSetup>
#(venv) PS C:\Users\dhira\Desktop\Dhiraj HP Laptop\Projects\Playwright_Automation_DesignSetup> pytest tests/test_login.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pages.login_page import LoginPage
from config.config import Config
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='function')
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(Config.USERNAME, Config.PASSWORD)
    assert page.url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'