import uiautomator
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
sl.sleep(10)
# driver.find_element(By.ID, "micp-aww-close").click()

el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.ViewAnimator/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.widget.TextView")
el1.click()
sl.sleep(3)

# Using UIAutomator(Java Function)
el3=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Skip sign in")')

# el3 = driver.find_element(by=AppiumBy.ID, value="com.amazon.mShop.android.shopping:id/skip_sign_in_button")
el3.click()
sl.sleep(5)

# Scroll down to element and click (Shop holiday gifts)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Shop holiday gifts").instance(0))').click()
sl.sleep(10)

driver.find_element(By.CLASS_NAME, "android.widget.TextView").click()
# el5.clear()

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID, 'com.amazon.mShop.android.shopping:id/rs_search_src_text')))

driver.find_element(by=AppiumBy.ID, value="com.amazon.mShop.android.shopping:id/rs_search_src_text").send_keys("bags")
sl.sleep(5)
el6 = driver.find_element(by=AppiumBy.ID, value="com.amazon.mShop.android.shopping:id/chrome_action_bar_search_icon")
el6.click()
driver.press_keycode(66)
driver.hide_keyboard()
sl.sleep(10)
driver.quit()