from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import By, AppiumBy
import time as sl
desired_caps = dict(
    deviceName='Andriod',
    platformName='Android',
    appPackage='com.amazon.mShop.android.shopping',
    appActivity='com.amazon.mShop.home.HomeActivity',

)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)