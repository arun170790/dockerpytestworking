import pytest
from selenium import webdriver
import os

@pytest.mark.parametrize("name",["arun", "hritesh", "kevin"])
@pytest.mark.google
def test_meth1(name) :
    # driver = webdriver.Chrome(os.path.dirname(__file__) + "/chromedriver")
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote('http://192.168.1.5:4444/wd/hub', options.to_capabilities())
    driver.get("https://natgrid-mxtst03.maximo.com")
    driver.maximize_window()
    driver.find_element_by_xpath("//input[@id='username']").send_keys(name)
    driver.close()
