from time import sleep

from appium import webdriver

desired_caps = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "127.0.0.1:62001",
        "appPackage": "com.dianping.v1",
        "appActivity": "com.dianping.v1.NovaMainActivity",
}
#启动app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(2)
# driver.find_element_by_id("com.ibox.calculators:id/digit7").click()
# driver.find_element_by_id("com.ibox.calculators:id/plus").click()
# driver.find_element_by_id("com.ibox.calculators:id/digit3").click()
# driver.find_element_by_id("").click()com.ibox.calculators:id/equal