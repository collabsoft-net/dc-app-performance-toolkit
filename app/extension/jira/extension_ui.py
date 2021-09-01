import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from util.conf import JIRA_SETTINGS

def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    project = random.choice(datasets['projects'])
    project_id = project[1]

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:view_vcs_page")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/VCSPage.jspa?s=projects&pid={project_id}")
            page.wait_until_visible((By.CSS_SELECTOR, "iframe[data-ac-polyfill]"))  # Wait for you app-specific UI element by ID selector
        sub_measure()

        @print_timing("selenium_app_custom_action:view_vcs_overview")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/VCSAdminPage.jspa?s=overview")
            page.wait_until_visible((By.CSS_SELECTOR, "iframe[data-ac-polyfill]"))  # Wait for you app-specific UI element by ID selector
        sub_measure()

        @print_timing("selenium_app_custom_action:view_vcs_settings")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/VCSAdminPage.jspa?s=settings")
            page.wait_until_visible((By.CSS_SELECTOR, "iframe[data-ac-polyfill]"))  # Wait for you app-specific UI element by ID selector
        sub_measure()

        @print_timing("selenium_app_custom_action:view_vcs_conflicts")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/VCSAdminPage.jspa?s=conflicts")
            page.wait_until_visible((By.CSS_SELECTOR, "iframe[data-ac-polyfill]"))  # Wait for you app-specific UI element by ID selector
        sub_measure()

        @print_timing("selenium_app_custom_action:view_vcs_audit_log")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/VCSAdminPage.jspa?s=auditLog")
            page.wait_until_visible((By.CSS_SELECTOR, "iframe[data-ac-polyfill]"))  # Wait for you app-specific UI element by ID selector
        sub_measure()

        @print_timing("selenium_app_custom_action:view_vcs_task_manager")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/VCSAdminPage.jspa?s=taskManager")
            page.wait_until_visible((By.CSS_SELECTOR, "iframe[data-ac-polyfill]"))  # Wait for you app-specific UI element by ID selector
        sub_measure()
    measure()
