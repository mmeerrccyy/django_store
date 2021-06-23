from selenium import webdriver

from test_login import login

driver = webdriver.Firefox()

login(driver)

driver.implicitly_wait(10)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/a[2]').click()

driver.implicitly_wait(10)

driver.find_element_by_xpath('//select[@name="category"]/option[text()="Телефони"]').click()
driver.find_element_by_id('id_name').send_keys('Nokia 3310')
driver.find_element_by_id('id_slug').send_keys('nokia-3310')
driver.find_element_by_id('id_description').send_keys('One of The Best Phone in The World! This is Nokia 3310!!!')
driver.find_element_by_id('id_price').send_keys('100500')
driver.find_element_by_id('id_stock').send_keys('1')
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/p/button').click()
