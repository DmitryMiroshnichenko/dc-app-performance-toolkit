
import random

from selenium.webdriver.common.by import By
from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from util.conf import JIRA_SETTINGS

"""
def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_view_user_story_map")
    def measure():

        @print_timing("selenium_view_user_story_map:load")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/projects/AANES?rapidView=61&selectedItem=com.bit.story-map__ausm-provided-link-to-panel")
            # page.wait_until_visible((By.ID, "app-header"))
            # WebDriverWait(page, 10).until(EC.presence_of_element_located((By.ID, "app-header"))
        sub_measure()
    measure()
"""

def app_specific_action_flower_global(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_view_flower_global")
    def measure():

        @print_timing("selenium_view_flower_global:load")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/FlowerBpm.jspa?p=repository")
            page.wait_for_page_loaded()
            # WebDriverWait(page, 10).until(EC.presence_of_element_located((By.ID, "app-header"))
        sub_measure()
    measure()

def app_specific_action_flower_issues(webdriver, datasets):
    issue_page = Issue(webdriver, issue_key=datasets['issue_key'])

    @print_timing("selenium_view_flower_issues")
    def measure():
        issue_page.go_to()
        issue_page.wait_for_page_loaded()

    measure()
