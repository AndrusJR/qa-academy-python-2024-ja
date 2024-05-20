import pytest
from src.system_under_test.ui.github_ui import GitHubUI
from src.system_under_test.api.github_api import GitHubAPIClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service=Service(executable_path="C:\Projects\Git_QA_academy\qa-academy-python-2024-ja\Web_drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# hook for pytest plugin
def pytest_html_report_title(report):
    report.title = "AQA Python Academy!"


# fixture for tests
@pytest.fixture
def git_hub_ui_app():
    service=Service(executable_path="C:\Projects\Git_QA_academy\qa-academy-python-2024-ja\Web_drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)


    # 1. Prestep. Navigate to GithubAPP
    githubui_app = GitHubUI(browser=driver)
    githubui_app.open()  # webdriver method - BAD

    # generators in python
    yield githubui_app

    # PostStep. Close the App
    githubui_app.close()  # webdriver method - BAD

@pytest.fixture
def git_hub_api_client():
    # create file with users data
    # _file = create_file({'user': 'serg'})
    git_hub_api_client = GitHubAPIClient()
    yield git_hub_api_client
    # remove file with users data
    # remove_file(_file)