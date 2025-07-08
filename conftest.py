
import pytest
from datetime import datetime
import os
import json

'''@pytest.hookimpl(tryfirst=True)
def pyest_configure(config):
    # Add timestamp to report file name

    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"
   # print('report generated')'''

#Below is correct code from chatgpt

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Create report directory if it doesn't exist
    report_dir = "reports"
    #os.makedirs(report_dir, exist_ok=True)

    # Add timestamp to report file name
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = os.path.join(report_dir, f"report_{now}.html")

@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("/n setting up resources...")
    yield
    print("Tearing down resources....")

@pytest.fixture()
def load_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__),"data", "test_data.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data
