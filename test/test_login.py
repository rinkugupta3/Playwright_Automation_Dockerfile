# Run test with following command line:
# (venv) PS C:\Users\dhira\Desktop\Dhiraj HP Laptop\Projects\Playwright_Automation_DesignSetup>
# (venv) PS C:\Users\dhira\Desktop\Dhiraj HP Laptop\Projects\Playwright_Automation_DesignSetup> pytest test/test_login.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pages.login_page import LoginPage
from config.config import Config
from playwright.sync_api import sync_playwright

def logout(page):
    # Click on the user dropdown and logout
    page.locator('span', has_text='manda user').locator('i').click()
    page.get_by_role('menuitem', name='Logout').click()
    page.wait_for_load_state('networkidle')

def test_successful_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        screenshots_dir = 'screenshots'
        os.makedirs(screenshots_dir, exist_ok=True)

        try:
            # Navigate to the login page
            page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

            # Wait for login page to fully load
            page.wait_for_selector('input[name="username"]')
            page.screenshot(path=os.path.join(screenshots_dir, "before_login.png"))

            # Perform login
            login_page = LoginPage(page)
            login_page.goto()
            login_page.login(Config.USERNAME, Config.PASSWORD)

            page.wait_for_url('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')
            page.wait_for_load_state('networkidle')
            page.screenshot(path=os.path.join(screenshots_dir, "after_login.png"))

            # Perform logout
            logout(page)

            # Wait for redirect to login page and take a screenshot
            try:
                page.wait_for_url('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', timeout=30000)
                page.screenshot(path=os.path.join(screenshots_dir, "after_logout.png"))
            except PlaywrightTimeoutError:
                print("Timeout waiting for redirect to login page.")
                print("Current URL:", page.url)
                page.screenshot(path=os.path.join(screenshots_dir, "error.png"))

        except Exception as e:
            print(f"Error during login/logout test: {str(e)}")
            page.screenshot(path=os.path.join(screenshots_dir, "error.png"))
            raise

        finally:
            browser.close()

if __name__ == "__main__":
    test_successful_login()
