# Run test with following command line:
# PS C:\Users\dhira\Desktop\Dhiraj HP Laptop\Projects\Playwright_Automation_DesignSetup>
# Playwright configured as "headless" mode by adding "True" and no browser will popup
# PS C:\Users\dhira\Desktop\Dhiraj HP Laptop\Projects\Playwright_Automation_DesignSetup> pytest test/test_login.py

import sys
import os

# Add the parent directory to the system path so Python can find modules from there.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pages.login_page import LoginPage
from config.config import Config
from playwright.sync_api import sync_playwright, Page


def navigate_to_login_page(page: Page):
    """
    Navigate to the login page and ensure it's fully loaded.
    """
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.wait_for_selector('input[name="username"]', timeout=10000)


def perform_login(page: Page):
    """
    Perform the login action on the web page.
    """
    page.fill('input[name="username"]', Config.USERNAME)
    page.fill('input[name="password"]', Config.PASSWORD)
    page.click('button[type="submit"]')

    # Wait until the URL indicates the dashboard and the network is idle
    page.wait_for_url('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index', timeout=30000)
    page.wait_for_load_state('networkidle')


def perform_logout(page: Page):
    """
    Perform the logout action on the web page.
    """
    try:
        print("Attempting to find and click on user dropdown...")

        # Locate the user dropdown-----page.locator('span i')
        """
            Locate the user dropdown element by capturing all dropdowns and selecting the right one.
            If there are multiple dropdowns, capture all and then select the one you need based on additional criteria like visibility or position
            selector can be used when the exact text or attributes of the element are not known or are changing dynamically.
            CSS Selector Breakdown
            span: This targets all <span> elements on the page.
            i: This targets all <i> elements that are children of the <span> elements.
        """
        user_dropdown = page.locator('span i')
        if user_dropdown.is_visible():
            user_dropdown.wait_for(state='visible', timeout=10000)
            user_dropdown.click()
            print("User dropdown clicked.")

            # Click the 'Logout' button
            page.get_by_role('menuitem', name='Logout').click()
            page.wait_for_load_state('networkidle')
        else:
            raise Exception("User dropdown not found.")

    except TimeoutError:
        print("TimeoutError: The element could not be found or interacted with in time.")
        page.screenshot(path=os.path.join('screenshots', 'logout_timeout_error.png'))
        raise


def test_successful_login():
    """
    Main test function to perform login and logout.
    """
    # Initialize Playwright and launch the browser
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=False)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Set up directory to save screenshots
        screenshots_dir = 'screenshots'
        os.makedirs(screenshots_dir, exist_ok=True)

        try:
            # Navigate to the login page and wait for it to load
            navigate_to_login_page(page)

            # Capture a screenshot before performing login
            page.screenshot(path=os.path.join(screenshots_dir, "before_login.png"))

            # Perform login and capture a screenshot
            perform_login(page)
            page.screenshot(path=os.path.join(screenshots_dir, "after_login.png"))

            # Perform logout and capture a screenshot
            perform_logout(page)

            # Wait for redirection to the login page after logout
            try:
                page.wait_for_url('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', timeout=30000)
                page.screenshot(path=os.path.join(screenshots_dir, "after_logout.png"))
            except TimeoutError:
                print("Timeout waiting for redirect to the login page.")
                print("Current URL:", page.url)
                page.screenshot(path=os.path.join(screenshots_dir, "error.png"))

        except Exception as e:
            print(f"Error during login/logout test: {str(e)}")
            page.screenshot(path=os.path.join(screenshots_dir, "error.png"))
            raise

        finally:
            browser.close()  # Ensure the browser is closed after the test


# Entry point for running the test directly
if __name__ == "__main__":
    test_successful_login()
