from selene import be


def given_opened():
    if browser.element('#com.dma.author.connect:id/touch_outside').matching(be.visible):
        browser.element('#com.dma.author.connect:id/close_button')