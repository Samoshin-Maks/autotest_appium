from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser

desired_caps = dict(
    platformName='Android',
    platformVersion='8.0',
    automationName='uiautomator2',
    deviceName='pixel_3a_xl',
    app=r'C:\Users\artyo\Desktop\x-author-google-debug.apk'
)

def test_first():
    android_options = UiAutomator2Options()
    android_options.new_command_timeout = 15
    browser.config.driver_options = android_options

    by_id = lambda id: (AppiumBy.ID, f'com.dma.author.android.x.connect:id/{id}')

    browser.config.driver = driver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        options=android_options,
        )

    browser.element(by_id('continue_button')).click()
    browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat[1]/androidx.appcompat.widget.LinearLayoutCompat/androidx.appcompat.widget.LinearLayoutCompat/android.widget.EditText')).click().type('123@mail.ru')

