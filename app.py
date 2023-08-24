from selene import be
from selene.support.shared import browser


def given_opened():
    if browser.element('#com.dma.author.connect:id/touch_outside').matching(be.visible):
        browser.element('#com.dma.author.connect:id/close_button').click()