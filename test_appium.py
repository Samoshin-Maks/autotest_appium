import unittest
from appium import webdriver
from appium_patch import monkey
webdriver.Remote = monkey.patch_all()
from selene.support.shared import browser
import app
desired_caps = dict(
    platformName='Android',
    platformVersion='8.0',
    automationName='uiautomator2',
    deviceName='pixel_3a_xl',
    app='C:\Users\artyo\Desktop\com.dma.author.android.x.connect-v1.0.0(3)-author-google-debug'
)

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def test_autorisation():

    app.given_opened()
    browser.element('#com.dma.author.connect:id/close_button').click()
    browser.element('#com.dma.author.connect:id/textinput_placeholder').click().type(79819740196)