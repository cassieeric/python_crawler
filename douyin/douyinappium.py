from appium import webdriver
import time
desired_caps = {
                "platformName": "Android",
                "deviceName": "VOG_AL00",
                "appPackage": "com.ss.android.ugc.aweme",
                "appActivity": ".main.MainActivity",
                "noReset": "true",
                "fullReset": "false",
}
server = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(server, desired_caps)
time.sleep(5)
driver.tap([(980, 100), (1000, 170)], 100)
time.sleep(1)
driver.tap([(324, 786), (459, 847)], 100)
time.sleep(1)
while True:
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/faw').click()
    time.sleep(2)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/kr').click()
    time.sleep(600)