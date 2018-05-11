from selenium import webdriver


driver = webdriver.Firefox()

driver.get("https://web.whatsapp.com/")

target = '"'+input('Name:	') +'"'

msg = input('msg:	')

x_arg = '//span[contains(@title,' + target + ')]'
_title = driver.find_element_by_xpath(x_arg)
_title.click()


msg_box = driver.find_element_by_class_name("_2S1VP")

msg_box.send_keys(msg)

driver.find_element_by_class_name('_2lkdt').click()


driver.close()
