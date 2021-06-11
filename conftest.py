import allure
import pytest
from selene.support.shared import browser


@allure.step('Инициализируем драйвер')
def step_driver():
    pass


@pytest.fixture(scope='module', autouse=True)
def setup_module():
    browser.config.base_url = "https://delo-prod.skblab.ru/login"


@allure.step('Закрываем драйвер')
def step_quit(quit):
    pass


@pytest.fixture(scope='module')
def teardown_module():
    browser.quit()


# @pytest.hookimpl()
# def pytest_exception_interact(node, call, report):
#     print("оу")
#     if report.failed:
#         print("hello")

from pathlib import Path
from _pytest.main import Session
from _pytest.nodes import Item
from _pytest.runner import CallInfo

FAILURES_FILE = Path() / "failures.txt"

@pytest.hookimpl()
def pytest_sessionstart(session: Session):
    if FAILURES_FILE.exists():
        FAILURES_FILE.unlink()
    FAILURES_FILE.touch()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call" and result.failed:
        try:
            with open(str(FAILURES_FILE), "a") as f:
                f.write(result.nodeid + "\n")
        except Exception as e:
            print("ERROR", e)
            pass
#
# @hookimpl(tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     print(item.execution_count)
