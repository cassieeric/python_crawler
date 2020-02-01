from appium import webdriver

desired_caps = {
                "platformName": "Android",
                "deviceName": "MHA_AL00",
                "appPackage": "com.tencent.mm",
                "appActivity": ".ui.LauncherUI"
}
server = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(server, desired_caps)
